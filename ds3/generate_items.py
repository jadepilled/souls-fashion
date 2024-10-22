import os
import json

# Paths to the images folder, icons folder, colors file, and the output JSON file
images_folder = "images"
icons_folder = "icons"
colors_file = "colors_extracted.json"
output_file = "items_for_web.json"

# Load the extracted colors from the JSON file
with open(colors_file, 'r') as color_file:
    colors_data = json.load(color_file)

# Iterate over each subfolder and generate item data
items = []
for item_type, item_list in colors_data.items():
    for item in item_list:
        item_name = os.path.splitext(item['image'])[0].replace('_', ' ').title()
        primary_color = item['primary_color']['hex']
        secondary_colors = [color['hex'] for color in item['secondary_colors']]

        # Adjust image path to point to the icons folder with subfolder type, maintaining proper casing
        item_data = {
            "name": item_name,
            "type": item_type,
            "image": f"{item_type}/{item['image']}",
            "primaryColor": primary_color,
            "secondaryColors": secondary_colors
        }
        items.append(item_data)

# Write the items data to the JSON file
with open(output_file, 'w') as json_file:
    json.dump(items, json_file, indent=4)

print(f"Items data successfully written to {output_file}")
