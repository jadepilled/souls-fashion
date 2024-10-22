// Assuming colors_extracted.json is structured with primary and secondary colors for each item
let items = []; // This will be populated with the items and their colors

// Load the colors from colors_extracted.json
fetch('colors_extracted.json')
    .then(response => response.json())
    .then(data => {
        items = data;
    });

// Function to handle item click
function handleItemClick(item) {
    const similarItems = findSimilarItems(item);
    displaySimilarItems(similarItems);
}

// Function to find similar items based on primary and secondary colors
function findSimilarItems(selectedItem) {
    // Array to store items with matching colors
    const similarPrimary = [];
    const similarSecondary = [];

    items.forEach(item => {
        // Check primary color similarity
        if (item.primaryColor === selectedItem.primaryColor && item.name !== selectedItem.name) {
            similarPrimary.push(item);
        }
        // Check secondary color similarity
        else if (item.secondaryColor === selectedItem.secondaryColor && item.name !== selectedItem.name) {
            similarSecondary.push(item);
        }
    });

    // Prioritize items with similar primary colors first
    return [...similarPrimary, ...similarSecondary];
}

// Function to display similar items in the UI
function displaySimilarItems(similarItems) {
    const similarItemsGrid = document.getElementById('similarItemsGrid');
    similarItemsGrid.innerHTML = ''; // Clear previous similar items

    similarItems.forEach(item => {
        const itemCard = document.createElement('div');
        itemCard.classList.add('item-card');
        itemCard.innerHTML = `
            <img src="icons/${item.type}/${item.image}" alt="${item.name}">
            <p>${item.name}</p>
        `;
        similarItemsGrid.appendChild(itemCard);
    });
}

// Function to display items when the search results are shown
function displayItems(items) {
    const itemGrid = document.getElementById('itemGrid');
    itemGrid.innerHTML = ''; // Clear previous items

    items.forEach(item => {
        const itemCard = document.createElement('div');
        itemCard.classList.add('item-card');
        itemCard.innerHTML = `
            <img src="icons/${item.type}/${item.image}" alt="${item.name}">
            <p>${item.name}</p>
        `;

        // Add click event to handle item selection
        itemCard.addEventListener('click', () => handleItemClick(item));

        itemGrid.appendChild(itemCard);
    });
}

// Call displayItems() function to populate items initially
// Assuming there's logic in search_items.js to filter the items by search query
