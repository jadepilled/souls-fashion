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

function displayItems(filteredItems) {
    const itemGrid = document.getElementById('itemGrid');
    itemGrid.innerHTML = ''; // Clear the current grid

    filteredItems.forEach(item => {
        const itemCard = createItemCard(item);
        itemGrid.appendChild(itemCard);
    });
}

function searchItems(query) {
    const lowerQuery = query.toLowerCase();

    return items.filter(item => {
        const nameMatch = item.name.toLowerCase().includes(lowerQuery);
        const primaryColorMatch = item.primaryColor.toLowerCase().includes(lowerQuery);
        const secondaryColorMatch = item.secondaryColors.some(color => color.toLowerCase().includes(lowerQuery));
        return nameMatch || primaryColorMatch || secondaryColorMatch;
    });
}

document.getElementById('searchInput').addEventListener('input', (e) => {
    const query = e.target.value;
    const filteredItems = searchItems(query);
    displayItems(filteredItems);
});

// Fetch items on page load
window.onload = fetchItems;
