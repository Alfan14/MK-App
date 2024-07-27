const map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM(),
      }),
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([longitude, latitude]), // Center on the city
      zoom: 12,
    }),
  });
  
  // Fetch and display food places
  fetch('https://your-api.com/get-food-places?city=YourCity')
    .then(response => response.json())
    .then(data => {
      const features = data.places.map(place => {
        return new ol.Feature({
          geometry: new ol.geom.Point(ol.proj.fromLonLat([place.longitude, place.latitude])),
          name: place.name,
        });
      });
  
      const vectorSource = new ol.source.Vector({
        features: features,
      });
  
      const vectorLayer = new ol.layer.Vector({
        source: vectorSource,
      });
  
      map.addLayer(vectorLayer);
    })
    .catch(error => console.error('Error fetching food places:', error));