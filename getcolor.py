import cv2
import numpy as np
from sklearn.cluster import KMeans
import os
import json

def get_dominant_colors(image_path, num_colors=3):
    # Load the image with an alpha channel if present
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Check if the image has an alpha channel (transparency)
    if image.shape[2] == 4:  # Check if the image has 4 channels (RGBA)
        # Separate the color and alpha channels
        b_channel, g_channel, r_channel, a_channel = cv2.split(image)
        # Create a mask for non-transparent pixels
        mask = a_channel > 0  # Keep only non-transparent pixels
        # Combine channels for non-transparent pixels
        pixels = image[mask][:, :3]  # Only take RGB channels
    else:
        # If no alpha channel, use all pixels
        pixels = image.reshape(-1, 3)

    # Use KMeans to cluster the pixel colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    dominant_colors = kmeans.cluster_centers_.astype(int)
    return dominant_colors

def distinct_colors(colors, threshold=50):
    distinct = [colors[0]]
    for color in colors[1:]:
        if all(np.linalg.norm(color - np.array(c)) > threshold for c in distinct):
            distinct.append(color)
        if len(distinct) == 3:
            break
    return distinct

def process_images(image_folder):
    results = {}
    for root, dirs, files in os.walk(image_folder):
        for filename in files:
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                image_path = os.path.join(root, filename)
                print(f"Processing: {filename} in {root}")

                dominant_colors = get_dominant_colors(image_path)
                distinct_dominant_colors = distinct_colors(dominant_colors)

                # Convert the color arrays to standard Python types for JSON serialization
                results[os.path.relpath(image_path, image_folder)] = [
                    tuple(int(color) for color in color_array) for color_array in distinct_dominant_colors
                ]
                print(f"{filename}: {distinct_dominant_colors}")

    return results

# Specify your main image folder (with subfolders)
image_folder = "images"  # Adjust this to point to your images folder
results = process_images(image_folder)

# Save the results to a JSON file
with open('armor_colors.json', 'w') as outfile:
    json.dump(results, outfile, indent=4)
