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

let currentRestaurantIndex = 0;
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
        displayRestaurant(currentRestaurantIndex);
    } catch (error) {
        console.error('Error fetching restaurant data:', error);
    }
}

function displayRestaurant(index) {
    if (restaurants.length === 0) return;

    const restaurant = restaurants[index];
    const restaurantId = restaurant.id || 'No ID';
    const restaurantName = restaurant.tags.name || 'Unnamed Restaurant';

    document.getElementById('restaurantId').textContent = restaurantId;
    document.getElementById('restaurantName').textContent = restaurantName;

    document.getElementById('prevButton').disabled = index === 0;
    document.getElementById('nextButton').disabled = index === restaurants.length - 1;
}

document.getElementById('prevButton').addEventListener('click', () => {
    if (currentRestaurantIndex > 0) {
        currentRestaurantIndex--;
        displayRestaurant(currentRestaurantIndex);
    }
});

document.getElementById('nextButton').addEventListener('click', () => {
    if (currentRestaurantIndex < restaurants.length - 1) {
        currentRestaurantIndex++;
        displayRestaurant(currentRestaurantIndex);
    }
});

fetchRestaurantData();
