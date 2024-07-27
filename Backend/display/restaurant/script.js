// URL of the Overpass API endpoint
const overpassUrl = 'https://overpass-api.de/api/interpreter';

// Overpass QL query to get all restaurants in London
const overpassQuery = `
[out:json];
area[name="Magetan"]->.mt;
(
  node["amenity"="restaurant"](area.mt);
  way["amenity"="restaurant"](area.mt);
  relation["amenity"="restaurant"](area.mt);
);
out center;
`;


// Function to fetch data from the Overpass API
async function fetchRestaurantData() {
    try {
        // Make the API request
        const response = await fetch(overpassUrl, {
            method: 'POST',
            body: overpassQuery,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });

        // Parse the JSON response
        const data = await response.json();

        // Display the data on the web page
        displayRestaurants(data.elements);
    } catch (error) {
        console.error('Error fetching restaurant data:', error);
    }
}

// Function to display restaurant data
function displayRestaurants(restaurants) {
    const restaurantContainer = document.getElementById('restaurants');

    // Create an unordered list to hold the restaurant names
    const list = document.createElement('ul');

    restaurants.forEach(restaurant => {
        const listItem = document.createElement('li');
        listItem.textContent = restaurant.tags.name || 'Unnamed Restaurant';
        list.appendChild(listItem);
    });

    // Append the list to the restaurant container
    restaurantContainer.appendChild(list);
}

// Fetch and display the restaurant data when the page loads
fetchRestaurantData();
