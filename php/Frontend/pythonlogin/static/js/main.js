document.getElementById('menuButton').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.display === 'none' || sidebar.style.display === '') {
        sidebar.style.display = 'block';
    } else {
        sidebar.style.display = 'none';
    }
});

// Close sidebar when clicking outside of it
document.addEventListener('click', function(event) {
    var sidebar = document.getElementById('sidebar');
    var menuButton = document.getElementById('menuButton');

    // Check if the click is outside the sidebar and menu button
    if (!sidebar.contains(event.target) && event.target !== menuButton) {
        sidebar.style.display = 'none';
    }
});

//Cards 
const overpassUrl = 'https://overpass-api.de/api/interpreter';
const overpassQuery = `
[out:json];
area[name="Magetan"]->.magetan;
(
  node["amenity"="restaurant"](area.magetan);
  way["amenity"="restaurant"](area.magetan);
  relation["amenity"="restaurant"](area.magetan);
);
out center;
`;

let currentPage = 0;
const itemsPerPage = 12;
let restaurants = [];
let currentRestaurants = [];

// Fetch restaurant data from the server
async function fetchRestaurantData() {
    try {
        const response = await fetch(overpassUrl, {
            method: 'POST',
            body: overpassQuery,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });

        const data = await response.json();
        restaurants = data.elements;
        currentRestaurants = restaurants; // Initialize currentRestaurants
        renderPage(currentPage);
    } catch (error) {
        console.error('Error fetching restaurant data:', error);
    }
}

// Render the restaurant data for the current page
// Ensure these variables are defined at the appropriate scope
const modal = document.getElementById('modal');
const modalDetails = document.getElementById('modalDetails');
const modalClose = document.querySelector('.modal-close');

function renderPage(page) {
    const startIndex = page * itemsPerPage;
    const endIndex = Math.min(startIndex + itemsPerPage, currentRestaurants.length);
    const container = document.getElementById('cardContainer');
    container.innerHTML = '';

    for (let i = startIndex; i < endIndex; i++) {
        const restaurant = currentRestaurants[i];
        const restaurantName = restaurant.tags.name || 'Unnamed Restaurant';
        const restaurantPhone = restaurant.tags.phone || 'N/A';
        const restaurantLat = restaurant.lat || 0;
        const restaurantLon = restaurant.lon || 0;
        const restaurantLink = `https://www.openstreetmap.org/?mlat=${restaurantLat}&mlon=${restaurantLon}&zoom=16`;
        const restaurantRating = restaurant.tags.rating || (Math.random() * 5).toFixed(1);
        const restaurantImage = `https://picsum.photos/300/200?random=${i}`;

        const card = document.createElement('div');
        card.className = 'card';
        card.style.cursor = 'pointer';
        card.innerHTML = `
            <img src="${restaurantImage}" alt="${restaurantName}" />
            <h2>${restaurantName}</h2>
            <p>Telephone: ${restaurantPhone}</p>
            <p>Rating: ${restaurantRating}</p>
            <p><a href="${restaurantLink}" target="_blank"><i class="fas fa-map-marker-alt"></i> ${restaurantName}</a></p>
        `;
        // Add click event to open modal with specific details
        card.addEventListener('click', () => {
            modalDetails.innerHTML = `
                <img src="${restaurantImage}" alt="${restaurantName}" style="width: 100%;" />
                <h2>${restaurantName}</h2>
                <p>Telephone: ${restaurantPhone}</p>
                <p>Rating: ${restaurantRating}</p>
                <button id="popup-route-button" class="route-button"><a href="${restaurantLink}" target="_blank"><i class="fas fa-map-marker-alt"></i> Cari rute terdekat</a></button>
            `;
            modal.style.display = 'block';
        });

        container.appendChild(card);
    }

    container.style.display = 'flex';

    // Ensure modalClose is defined
    if (modalClose) {
        modalClose.onclick = function() {
            modal.style.display = 'none';
        };
    }

    // Close modal when clicking outside of the modal content
    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };

    const prevButton = document.getElementById('prevPageButton');
    const nextButton = document.getElementById('nextPageButton');
    
    if (prevButton) {
        prevButton.disabled = page === 0;
    }
    if (nextButton) {
        nextButton.disabled = endIndex === currentRestaurants.length;
    }
}

// Event listeners for pagination buttons
document.getElementById('prevPageButton').addEventListener('click', () => {
    if (currentPage > 0) {
        currentPage--;
        renderPage(currentPage);
    }
});

document.getElementById('nextPageButton').addEventListener('click', () => {
    if ((currentPage + 1) * itemsPerPage < currentRestaurants.length) {
        currentPage++;
        renderPage(currentPage);
    }
});

// Search restaurants based on input
function searchRestaurants() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    currentRestaurants = restaurants.filter(restaurant =>
        (restaurant.tags.name || '').toLowerCase().includes(query) ||
        (restaurant.tags.phone || '').toLowerCase().includes(query)
    );
    currentPage = 0;
    renderPage(currentPage);
}

// Set up event listener for the search input
document.getElementById('searchInput').addEventListener('input', searchRestaurants);

// Fetch and render data initially
fetchRestaurantData();

//pop up 
