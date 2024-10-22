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

    // Adjust image path to match the icons folder with item type, ensuring proper casing
    const img = document.createElement('img');
    img.src = `icons/${item.type}/${item.image}`; // Use type to access the correct folder
    img.alt = item.name;
    img.onerror = () => {
        img.src = 'icons/placeholder.png'; // Fallback to placeholder image if not found
    };

    const title = document.createElement('p');
    title.textContent = item.name;

    const colorBar = document.createElement('div');
    colorBar.classList.add('color-bar');
    if (item.primaryColor) {
        const primaryColorDiv = document.createElement('div');
        primaryColorDiv.style.backgroundColor = item.primaryColor;
        colorBar.appendChild(primaryColorDiv);
    }
    item.secondaryColors.forEach(color => {
        const secondaryColorDiv = document.createElement('div');
        secondaryColorDiv.style.backgroundColor = color;
        colorBar.appendChild(secondaryColorDiv);
    });

    card.appendChild(img);
    card.appendChild(title);
    card.appendChild(colorBar);

    card.addEventListener('click', () => {
        displaySimilarItems(item);
    });

    return card;
}

function displayItems(filteredItems) {
    const itemGrid = document.getElementById('itemGrid');
    itemGrid.innerHTML = ''; // Clear the current grid

    if (filteredItems.length === 0) {
        itemGrid.innerHTML = '<p>No items found matching the criteria.</p>';
        return;
    }

    filteredItems.forEach(item => {
        const itemCard = createItemCard(item);
        itemGrid.appendChild(itemCard);
    });
}

function searchItems(query) {
    const lowerQuery = query.toLowerCase();
    const selectedFilters = Array.from(document.querySelectorAll('.filters input:checked')).map(input => input.value);

    return items.filter(item => {
        const nameMatch = item.name.toLowerCase().includes(lowerQuery);
        const primaryColorMatch = item.primaryColor && item.primaryColor.toLowerCase().includes(lowerQuery);
        const secondaryColorMatch = item.secondaryColors.some(color => color.toLowerCase().includes(lowerQuery));
        const typeMatch = selectedFilters.includes(item.type);
        return (nameMatch || primaryColorMatch || secondaryColorMatch) && typeMatch;
    });
}

function displaySimilarItems(selectedItem) {
    const similarItemsContainer = document.getElementById('similarItems');
    const similarItemGrid = document.getElementById('similarItemGrid');
    similarItemGrid.innerHTML = ''; // Clear previous similar items

    const similarItems = items.filter(item => {
        return item !== selectedItem && // Avoid selecting itself
               (item.primaryColor === selectedItem.primaryColor ||
                item.secondaryColors.some(color => selectedItem.secondaryColors.includes(color)));
    });

    if (similarItems.length > 0) {
        similarItems.forEach(item => {
            const itemCard = createItemCard(item);
            similarItemGrid.appendChild(itemCard);
        });
        similarItemsContainer.style.display = 'block';
    } else {
        similarItemsContainer.style.display = 'none';
    }
}

document.getElementById('searchInput').addEventListener('input', () => {
    const query = document.getElementById('searchInput').value;
    const filteredItems = searchItems(query);
    displayItems(filteredItems);
});

document.querySelectorAll('.filter-checkbox').forEach(checkbox => {
    checkbox.addEventListener('change', () => {
        const query = document.getElementById('searchInput').value;
        const filteredItems = searchItems(query);
        displayItems(filteredItems);
    });
});

// Fetch items on page load
window.onload = fetchItems;
