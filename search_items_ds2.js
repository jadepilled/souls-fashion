let items = [];  // To store items loaded from JSON
let colorDistanceThreshold = 100;  // Default threshold value
let activeFilters = new Set(); // To track active filters

// Fisher-Yates Shuffle algorithm to randomize the order of items
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];  // Swap elements
  }
  return array;
}

// Fetch the typed_items_for_web.json file and store its data
async function fetchItems() {
  try {
      const response = await fetch('pages/ds2/typed_items_for_web.json');
      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }
      items = await response.json();
      
      // Shuffle items before displaying
      items = shuffle(items);
      
      displayItems(items);  // Display all items initially
  } catch (error) {
      console.error('Error loading items:', error);
  }
}

// Function to convert hex to RGB
function hexToRgb(hex) {
  let bigint = parseInt(hex.slice(1), 16);
  let r = (bigint >> 16) & 255;
  let g = (bigint >> 8) & 255;
  let b = bigint & 255;
  return [r, g, b];
}

// Function to calculate Euclidean distance between two RGB colors
function calculateDistance(color1, color2) {
  let rDiff = color1[0] - color2[0];
  let gDiff = color1[1] - color2[1];
  let bDiff = color1[2] - color2[2];
  return Math.sqrt(rDiff * rDiff + gDiff * gDiff + bDiff * bDiff);
}

// Function to calculate weighted color distance
function calculateWeightedDistance(inputColor, primaryColor, secondaryColors, secondaryWeight) {
  let primaryRgb = hexToRgb(primaryColor);
  let inputRgb = hexToRgb(inputColor);
  
  // Calculate Euclidean distance for primary color
  let primaryDistance = calculateDistance(inputRgb, primaryRgb);
  
  // Calculate average distance for secondary colors
  let secondaryDistances = secondaryColors.map(secondaryColor => {
      let secondaryRgb = hexToRgb(secondaryColor);
      return calculateDistance(inputRgb, secondaryRgb);
  });

  let avgSecondaryDistance = secondaryDistances.reduce((a, b) => a + b, 0) / secondaryDistances.length;

  // Combine primary and secondary distances with weighting
  let combinedDistance = (1 - secondaryWeight) * primaryDistance + secondaryWeight * avgSecondaryDistance;

  return combinedDistance;
}

// Function to find the closest items based on input color, secondary weight, and search query
function findMatchingItems(inputColor, secondaryWeight, query) {
  const lowerQuery = query.toLowerCase();

  return items.map(item => {
      // Calculate color distance
      let distance = calculateWeightedDistance(inputColor, item.primaryColor, item.secondaryColors, secondaryWeight);

      // Check if the item name matches the search query
      const nameMatch = item.name.toLowerCase().includes(lowerQuery);

      // Check if the item matches any active filters
      const typeMatch =
        activeFilters.size === 0 || activeFilters.has(item.type);

      // Include items that match by name, type, and have a color distance below the threshold
      return {
        ...item,
        distance: distance,
        nameMatch: nameMatch,
        typeMatch: typeMatch,
      };
    })
    .filter(
      item =>
        item.nameMatch &&
        item.typeMatch &&
        item.distance <= colorDistanceThreshold
    )
    .sort((a, b) => a.distance - b.distance);
}

// Display items in the grid
function displayItems(filteredItems) {
  const itemGrid = document.getElementById('itemGrid');
  itemGrid.innerHTML = ''; // Clear the current grid

  filteredItems.forEach(item => {
    const itemCard = createItemCard(item);
    itemGrid.appendChild(itemCard);
  });
}

// Function to create item cards with click event for search
function createItemCard(item) {
  const card = document.createElement('div');
  card.classList.add('item-card');

  const img = document.createElement('img');
  img.src = `pages/ds2/icons/${item.image}`;
  img.alt = item.name;

  const title = document.createElement('p');
  title.textContent = item.name;

  const colorBar = document.createElement('div');
  colorBar.classList.add('color-bar');
  const primaryColorDiv = document.createElement('div');
  primaryColorDiv.style.backgroundColor = item.primaryColor;
  const secondaryColorDiv1 = document.createElement('div');
  secondaryColorDiv1.style.backgroundColor = item.secondaryColors[0];
  const secondaryColorDiv2 = document.createElement('div');
  secondaryColorDiv2.style.backgroundColor = item.secondaryColors[1];
  colorBar.appendChild(primaryColorDiv);
  colorBar.appendChild(secondaryColorDiv1);
  colorBar.appendChild(secondaryColorDiv2);

  card.appendChild(img);
  card.appendChild(title);
  card.appendChild(colorBar);

  // Add click event to set the item's primary color for the search
  card.addEventListener('click', () => {
    document.getElementById('favcolor').value = item.primaryColor;
    updateMatchingItems();  // Trigger the search with the selected item's primary color
});

  return card;
}

// Add event listener for color picker, name input, slider, and color distance threshold slider
document.getElementById('favcolor').addEventListener('change', function() {
  updateMatchingItems();
});

document.getElementById('searchInput').addEventListener('input', function() {
  updateMatchingItems();
});

document.getElementById('secondaryWeightSlider').addEventListener('input', function() {
  document.getElementById('sliderValue').textContent = this.value;
  updateMatchingItems();
});

document.getElementById('colorThresholdSlider').addEventListener('input', function() {
  colorDistanceThreshold = parseFloat(this.value);
  document.getElementById('colorThresholdValue').textContent = this.value;
  updateMatchingItems();
});

// Function to update matching items based on the current color, slider value, and query
function updateMatchingItems() {
  const selectedColor = document.getElementById('favcolor').value;
  const secondaryWeight = parseFloat(document.getElementById('secondaryWeightSlider').value);
  const query = document.getElementById('searchInput').value;  // Get the search query

    // Find items that match both color and name and have color distance below the threshold
    const matchingItems = findMatchingItems(selectedColor, secondaryWeight, query);
    displayItems(matchingItems);
}

// Function to toggle filters
function toggleFilter(buttonId, filterType) {
  const button = document.getElementById(buttonId);

  // Toggle the active state
  if (activeFilters.has(filterType)) {
    activeFilters.delete(filterType); // Remove filter if it's already active
    button.classList.remove("active"); // Update button style
  } else {
    activeFilters.add(filterType); // Add filter to active filters
    button.classList.add("active"); // Update button style
  }
  updateMatchingItems(); // Refresh items based on current filters
}

document
  .getElementById("headFilter")
  .addEventListener("click", () => toggleFilter("headFilter", "head"));
document
  .getElementById("chestFilter")
  .addEventListener("click", () => toggleFilter("chestFilter", "chest"));
document
  .getElementById("handsFilter")
  .addEventListener("click", () => toggleFilter("handsFilter", "hands"));
document
  .getElementById("legsFilter")
  .addEventListener("click", () => toggleFilter("legsFilter", "legs"));
document
  .getElementById("weaponsFilter")
  .addEventListener("click", () => toggleFilter("weaponsFilter", "weapons"));
document
  .getElementById("shieldsFilter")
  .addEventListener("click", () => toggleFilter("shieldsFilter", "shields"));

document.getElementById("clearFilter").addEventListener("click", () => {
  activeFilters.clear(); // Clear all active filters

  // Select all buttons within 'filter-button' class to remove the active state
  document
    .querySelectorAll(".filter-buttons button")
    .forEach(button => button.classList.remove("active"));

  updateMatchingItems();
});

// Fetch items on page load
window.onload = fetchItems;
