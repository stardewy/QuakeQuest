#Issue: The map image and graph are not displaying properly. The cords are right, but it won't plot properly.

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# Load the map image
map_image = mpimg.imread('central_visayas.jpg')

# Check the shape of the map image
print(f"Map image shape: {map_image.shape}")

# Station data with coordinates (longitude, latitude) and distances in km
stations = {
    "Tagbilaran": {"coords": np.array([123.999, 9.374]), "distance": 50},  # Tagbilaran, Bohol
    "Cebu": {"coords": np.array([123.990, 10.560]), "distance": 60},       # Cebu City, Cebu
    "Dumaguete": {"coords": np.array([123.399, 8.579]), "distance": 70}    # Dumaguete, Negros Oriental
}

# Epicenter location near Sagbayan, Bohol
epicenter = np.array([124.285, 9.579])  # (longitude, latitude)

# Create a plot with the map image
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(map_image, extent=[121.5, 126, 8, 12])  

# Plot each station and draw a circle around it
for station, data in stations.items():
    lon, lat = data["coords"]  # Ensures correct order for (longitude, latitude)
    distance_km = data["distance"]

    # Plot the station point
    ax.plot(lon, lat, 'ro', markersize=5, label=station if station not in ax.get_legend_handles_labels()[1] else "")
    
    # Convert distance to degrees (1 degree ~ 111 km)
    distance_deg = distance_km / 111
    circle = plt.Circle((lon, lat), distance_deg, color='blue', alpha=0.3, edgecolor='blue')
    ax.add_patch(circle)

# Plot the epicenter
epicenter_lat, epicenter_lon = epicenter
ax.plot(epicenter_lon, epicenter_lat, 'go', markersize=8, label="Approximate Epicenter")

# Set plot labels and title
ax.set_title("Stations and Approximate Epicenter on Philippine Map")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()
plt.grid()
plt.show()
