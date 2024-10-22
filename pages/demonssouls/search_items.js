let items = [];  // To store items loaded from JSON

// Fetch the items_for_web.json file and store its data
async function fetchItems() {
    try {
        const response = await fetch('items_for_web.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        items = await response.json();
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

// Function to find the closest items based on input color
function findMatchingItems(inputColor) {
    let inputRgb = hexToRgb(inputColor);

    return items.map(item => {
        let itemRgb = hexToRgb(item.primaryColor);
        let distance = calculateDistance(inputRgb, itemRgb);
        return { ...item, distance: distance };
    }).sort((a, b) => a.distance - b.distance);
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

// Function to create item cards
function createItemCard(item) {
    const card = document.createElement('div');
    card.classList.add('item-card');

    const img = document.createElement('img');
    img.src = `icons/${item.image}`;
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

    return card;
}

// Add event listener for color picker
document.getElementById('favcolor').addEventListener('change', function(e) {
    const selectedColor = e.target.value;
    const matchingItems = findMatchingItems(selectedColor);
    displayItems(matchingItems);
});

// Fetch items on page load
window.onload = fetchItems;
