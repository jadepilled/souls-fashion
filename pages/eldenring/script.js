// Sample database of Elden Ring items (with item names and colors in hex format)
const itemDatabase = [
    { name: 'Maliketh’s Armor', category: 'Chest', color: '#5c4033' },
    { name: 'Raging Wolf Helm', category: 'Head', color: '#808080' },
    { name: 'Crucible Tree Armor', category: 'Chest', color: '#d4af37' },
    { name: 'Lion Greatbow', category: 'Weapon', color: '#785a28' },
    { name: 'Brass Shield', category: 'Shield', color: '#b87333' }
];

// Search function to find items based on user input
function searchItems() {
    const searchQuery = document.getElementById("item-search").value.toLowerCase();
    const searchResults = document.getElementById("search-results");
    
    // Clear previous results
    searchResults.innerHTML = '';
    
    // Filter items by search query
    const results = itemDatabase.filter(item => item.name.toLowerCase().includes(searchQuery));
    
    if (results.length > 0) {
        results.forEach(item => {
            const itemElement = document.createElement("p");
            itemElement.textContent = `${item.name} (Category: ${item.category}, Color: ${item.color})`;
            searchResults.appendChild(itemElement);
        });
    } else {
        searchResults.innerHTML = "<p>No items found.</p>";
    }
}

// Function to find items based on a hex color code input
function findByColor() {
    const colorInput = document.getElementById("color-input").value.trim();
    const recommendationsDiv = document.getElementById("recommendations");
    
    // Clear previous recommendations
    recommendationsDiv.innerHTML = '';

    // Check if input is a valid hex code
    if (!/^#[0-9A-F]{6}$/i.test(colorInput)) {
        recommendationsDiv.innerHTML = '<p>Invalid color code. Please enter a valid hex code (e.g., #RRGGBB).</p>';
        return;
    }

    // Find items with similar color
    const recommendations = itemDatabase.filter(item => item.color.toLowerCase() === colorInput.toLowerCase());
    
    if (recommendations.length > 0) {
        recommendations.forEach(item => {
            const itemElement = document.createElement("p");
            itemElement.textContent = `${item.name} (Category: ${item.category}, Color: ${item.color})`;
            recommendationsDiv.appendChild(itemElement);
        });
    } else {
        recommendationsDiv.innerHTML = "<p>No items found with this color.</p>";
    }
}
