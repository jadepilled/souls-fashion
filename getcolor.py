import os
import json
from PIL import Image

def rgb_to_hex(rgb_color):
    """Converts an RGB tuple to HEX."""
    return "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])

def is_near_black_or_white_or_transparent(rgb_color, threshold=20):
    """Checks if the given RGB color is near black, white, or transparent."""
    return (
        (all(c <= threshold for c in rgb_color[:3])) or  # Near black
        (all(c >= (255 - threshold) for c in rgb_color[:3])) or  # Near white
        (len(rgb_color) == 4 and rgb_color[3] == 0)  # Transparent
    )

def extract_quantized_colors(image_path, num_colors=8):
    """
    Extracts quantized colors from the image, ignoring black, white, and transparent pixels.
    Returns the primary color and up to 3 secondary colors.
    """
    with Image.open(image_path) as img:
        # Ensure the image is in RGBA mode to handle transparency
        img = img.convert("RGBA")
        
        # Resize the image to speed up processing
        img = img.resize((100, 100))

        # Get a quantized version of the image with the required number of colors
        quantized_img = img.quantize(colors=num_colors)
        
        # Get the color palette (ignoring the alpha channel)
        palette = quantized_img.getpalette()[:num_colors * 3]
        palette_colors = [tuple(palette[i:i+3]) for i in range(0, len(palette), 3)]
        
        # Get the color counts and sort them by frequency
        color_counts = quantized_img.getcolors()
        color_counts.sort(reverse=True, key=lambda x: x[0])  # Sort by frequency

        # Filter out black, white, and transparent colors
        valid_colors = []
        for count, color_idx in color_counts:
            color = palette_colors[color_idx]
            if not is_near_black_or_white_or_transparent(color):
                valid_colors.append(color)
        
        # Ensure we have at least 4 valid colors
        if len(valid_colors) < 4:
            valid_colors = valid_colors + [(255, 255, 255)] * (4 - len(valid_colors))  # Add white as filler

        # Return the primary color and 3 secondary colors
        primary_color = valid_colors[0]
        secondary_colors = valid_colors[1:4]  # Take up to 3 secondary colors
        
        return primary_color, secondary_colors

def process_images_in_folder(root_folder):
    """
    Processes all images in the root folder and subfolders.
    Extracts primary and secondary colors for each image.
    Returns a dictionary containing all results.
    """
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
                    primary_color, secondary_colors = extract_quantized_colors(file_path)
                    
                    # Convert colors to HEX and structure results
                    primary_color_hex = rgb_to_hex(primary_color)
                    secondary_colors_hex = [rgb_to_hex(color) for color in secondary_colors]
                    
                    # Append the result to the respective subfolder
                    results[relative_subdir].append({
                        "image": file,
                        "primary_color": {
                            "rgb": list(primary_color),
                            "hex": primary_color_hex
                        },
                        "secondary_colors": [
                            {
                                "rgb": list(color),
                                "hex": rgb_to_hex(color)
                            }
                            for color in secondary_colors
                        ]
                    })
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return results

def save_results_to_json(results, output_file):
    """Saves the extracted color data to a JSON file."""
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
