  // Initialize the map
  const map = L.map('map').setView([-7.655491885214246, 111.32793437715695], 13);

  // Add a Thunderforest tile layer
  const thunderforestApiKey = '066192e99e7848caa48bb145d293c73f';
  L.tileLayer(`https://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png?apikey=${thunderforestApiKey}`, {
      maxZoom: 19,
      attribution: 'Maps © Thunderforest, Data © OpenStreetMap contributors'
  }).addTo(map);

  // Function to fetch food places
  async function fetchFoodPlaces() {
      // Define the amenities to search for
      const amenities = 'restaurant|cafe|bar';

      // Create the Overpass API query
      const query = `
          [out:json];
          area[name="Magetan"]->.searchArea;
          node["amenity"~"${amenities}"](area.searchArea);
          out;
      `;
      
      // URL for the Overpass API request
      const url = `https://overpass-api.de/api/interpreter?data=${encodeURIComponent(query)}`;

      try {
          // Fetch data from the Overpass API
          const response = await fetch(url);
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          const data = await response.json();

          // Display food places on the map
          displayFoodPlaces(data);
      } catch (error) {
          console.error('Error fetching data:', error);
      }
  }

  // Function to display food places on the map
  function displayFoodPlaces(data) {
      data.elements.forEach(place => {
          const marker = L.marker([place.lat, place.lon]).addTo(map);
          marker.bindPopup(`<b>${place.tags.name || 'Unknown'}</b><br>${place.tags.amenity}`);
      });
  }

  // Fetch and display food places when the page loads
  fetchFoodPlaces();