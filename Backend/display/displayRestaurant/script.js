const overpassUrl = 'https://overpass-api.de/api/interpreter';
const overpassQuery = `
[out:json];
area[name="London"]->.london;
(
  node["amenity"="restaurant"](area.london);
  way["amenity"="restaurant"](area.london);
  relation["amenity"="restaurant"](area.london);
);
out center;
`;

let currentPage = 0;
const itemsPerPage = 12;
let restaurants = [];

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
        renderPage(currentPage);
    } catch (error) {
        console.error('Error fetching restaurant data:', error);
    }
}

function renderPage(page) {
    const startIndex = page * itemsPerPage;
    const endIndex = Math.min(startIndex + itemsPerPage, restaurants.length);
    const container = document.getElementById('cardContainer');
    container.innerHTML = '';

    for (let i = startIndex; i < endIndex; i++) {
        const restaurant = restaurants[i];
        const restaurantId = restaurant.id || 'No ID';
        const restaurantName = restaurant.tags.name || 'Unnamed Restaurant';
        const restaurantPhone = restaurant.tags.phone || 'N/A';
        const restaurantLat = restaurant.lat || 0;
        const restaurantLon = restaurant.lon || 0;
        const restaurantLink = `https://www.openstreetmap.org/?mlat=${restaurantLat}&mlon=${restaurantLon}&zoom=16`;
        const restaurantRating = restaurant.tags.rating || (Math.random() * 5).toFixed(1);
        const restaurantImage = `https://via.placeholder.com/300?text=${encodeURIComponent(restaurantName)}`;

        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <img src="${restaurantImage}" alt="${restaurantName}" />
             <h2>${restaurantName}</h2>
            <p>ID: ${restaurantId}</p>
            <p>Telephone: ${restaurantPhone}</p>
            <p>Rating: ${restaurantRating}</p>
            <p>Location: <a href="${restaurantLink}" target="_blank">View ${restaurantName} on Map</a></p>
        `;
        container.appendChild(card);
    }

    document.getElementById('prevPageButton').disabled = page === 0;
    document.getElementById('nextPageButton').disabled = endIndex === restaurants.length;
}

document.getElementById('prevPageButton').addEventListener('click', () => {
    if (currentPage > 0) {
        currentPage--;
        renderPage(currentPage);
    }
});

document.getElementById('nextPageButton').addEventListener('click', () => {
    if ((currentPage + 1) * itemsPerPage < restaurants.length) {
        currentPage++;
        renderPage(currentPage);
    }
});

fetchRestaurantData();
