import geojson
from shapely.geometry import shape, box

# Load your existing GeoJSON Feature Collection
with open('data/geojson/inundation.geojson', 'r') as f:
    geojson_data = geojson.load(f)

# Extract the geometries from the features
geometries = [shape(feature.geometry) for feature in geojson_data['features']]

# Calculate the bounding box for all geometries
combined_bbox = box(
    min([geom.bounds[0] for geom in geometries]),
    min([geom.bounds[1] for geom in geometries]),
    max([geom.bounds[2] for geom in geometries]),
    max([geom.bounds[3] for geom in geometries])
)

# Create a GeoJSON feature for the bounding box
bounding_box_feature = geojson.Feature(
    geometry=combined_bbox.__geo_interface__,
    properties={"name": "Bounding Box"}
)

# Add the bounding box feature to the Feature Collection
geojson_data['features'].append(bounding_box_feature)

# Save the enhanced GeoJSON to a new file
with open('data/geojson/inundation-bbox.geojson', 'w') as f:
    geojson.dump(geojson_data, f)

print("Bounding box feature added successfully.")

