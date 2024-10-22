import os
from PIL import Image
import json

# Define the folders
input_folder = "images"
output_folder = "icons"
json_file = "colors_extracted.json"

# Create output folder structure
def create_output_subfolders():
    for folder in ["Chest", "Hands", "Head", "Legs", "Shields", "Weapons"]:
        os.makedirs(os.path.join(output_folder, folder), exist_ok=True)

# Resize images to 200x200px and save them into the corresponding subfolder
def resize_images():
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                input_path = os.path.join(root, file)
                
                # Determine the relative folder path to maintain subfolder structure
                relative_folder = os.path.relpath(root, input_folder)
                output_subfolder = os.path.join(output_folder, relative_folder)
                os.makedirs(output_subfolder, exist_ok=True)
                
                output_path = os.path.join(output_subfolder, file)
                
                # Open and resize image
                with Image.open(input_path) as img:
                    img = img.resize((200, 200), Image.LANCZOS)
                    img.save(output_path)

# Generate item list from the colors_extracted.json file
def generate_item_list():
    items = []
    with open(json_file, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error loading JSON file: {e}")
            return

    # Make sure `data` is a list of dictionaries
    if not isinstance(data, list):
        print("Invalid JSON format: Expected a list of items.")
        return

    for item_data in data:
        if isinstance(item_data, dict):
            # Ensure all necessary keys exist in item_data
            if all(key in item_data for key in ["name", "type", "primaryColor", "secondaryColors"]):
                item = {
                    "name": item_data["name"],
                    "image": f'icons/{item_data["type"]}/{item_data["name"]}.png',  # Path for resized 200x200px icons
                    "primaryColor": item_data["primaryColor"]["hex"],
                    "secondaryColors": [color["hex"] for color in item_data["secondaryColors"]]
                }
                items.append(item)
            else:
                print(f"Skipping item due to missing keys: {item_data}")
        else:
            print(f"Invalid item format: {item_data}")

    # Write the item list to a JSON file (or use directly in your HTML script)
    with open("items_for_web.json", "w") as outfile:
        json.dump(items, outfile, indent=4)

    print("Items list generated and saved to items_for_web.json")

def main():
    create_output_subfolders()
    resize_images()
    generate_item_list()

if __name__ == "__main__":
    main()
