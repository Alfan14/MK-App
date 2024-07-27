import requests

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area[name="Magetan"]->.mt;
(
  node["amenity"="restaurant"](area.mt);
  way["amenity"="restaurant"](area.mt);
  relation["amenity"="restaurant"](area.mt);
);
out center;
"""
response = requests.get(overpass_url, params={'data': overpass_query})
data = response.json()

# Print restaurant data
for element in data['elements']:
    print(element)