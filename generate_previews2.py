import os
import json

# Define the folders
input_folder = "images"   # Folder containing subfolders with images
json_file = "colors_extracted.json"   # The JSON file containing color data
output_file = "items_for_web.json"    # Output JSON file to be used by the HTML page

# Function to generate the item list
def generate_item_list():
    items = []

    # Load color data from colors_extracted.json
    with open(json_file, "r") as f:
        try:
            color_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error loading JSON file: {e}")
            return

    # Traverse the images folder and associate colors from color_data
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                # Get the relative folder to categorize the item (Chest, Head, etc.)
                relative_folder = os.path.relpath(root, input_folder)
                item_name = os.path.splitext(file)[0]   # Item name based on file name (without extension)
                
                # Search for matching color data by filename
                color_info = None
                if relative_folder in color_data:
                    for item_data in color_data[relative_folder]:
                        if item_data["image"] == file:
                            color_info = item_data
                            break
                
                # Create item object with image path and color info
                item = {
                    "name": item_name,
                    "image": f"{relative_folder}/{file}",  # Image path (relative to 'images' folder)
                    "primaryColor": color_info["primary_color"]["hex"] if color_info else "#000000",
                    "secondaryColors": [color["hex"] for color in color_info["secondary_colors"]] if color_info else ["#000000", "#000000"]
                }
                items.append(item)

    # Write the item list to a JSON file
    with open(output_file, "w") as outfile:
        json.dump(items, outfile, indent=4)

    print(f"Item list generated and saved to {output_file}")

def main():
    generate_item_list()

if __name__ == "__main__":
    main()
