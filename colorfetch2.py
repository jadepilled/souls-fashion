import os
import json
from colorthief import ColorThief

def rgb_to_hex(rgb_color):
    """Converts an RGB tuple to HEX."""
    return "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])

def extract_colors(image_path, num_colors=6):
    """Extracts the most common colors from the image using ColorThief."""
    color_thief = ColorThief(image_path)
    
    # Get the dominant color (primary)
    primary_color = color_thief.get_color(quality=1)
    
    # Get the palette excluding transparency
    palette = color_thief.get_palette(color_count=num_colors)
    
    # Ensure transparency is not included (discard fully transparent colors)
    filtered_palette = [color for color in palette if color[3:] != (0,)]
    
    # Return both primary and the remaining top secondary colors
    return primary_color, filtered_palette[:5]

def process_images_in_folder(root_folder):
    """Processes all images in the root folder and its subfolders."""
    results = {}
    
    # Walk through all directories and subdirectories
    for subdir, _, files in os.walk(root_folder):
        relative_subdir = os.path.relpath(subdir, root_folder)
        
        # Initialize a list for images in this subfolder
        if relative_subdir not in results:
            results[relative_subdir] = []
        
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(subdir, file)
                
                # Extract colors from the image
                try:
                    primary_color, secondary_colors = extract_colors(file_path)
                    
                    # Convert colors to HEX and structure results
                    primary_color_hex = rgb_to_hex(primary_color)
                    secondary_colors_hex = [rgb_to_hex(color) for color in secondary_colors]
                    
                    results[relative_subdir].append({
                        "image": file,
                        "primary_color": {
                            "rgb": primary_color,
                            "hex": primary_color_hex
                        },
                        "secondary_colors": [
                            {
                                "rgb": color,
                                "hex": rgb_to_hex(color)
                            }
                            for color in secondary_colors
                        ]
                    })
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return results

def save_results_to_json(results, output_file):
    """Saves the extracted results to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

def main():
    # Define the folder where images are stored and the output file
    images_folder = os.path.join(os.getcwd(), 'images')
    output_file = 'colors_extracted.json'
    
    # Process all images in the folder
    results = process_images_in_folder(images_folder)
    
    # Save the results to a JSON file
    save_results_to_json(results, output_file)
    print(f"Colors extracted and saved to {output_file}")

if __name__ == "__main__":
    main()
