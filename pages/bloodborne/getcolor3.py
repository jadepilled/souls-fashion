import os
import json
from PIL import Image

def rgb_to_hex(rgb_color):
    """Converts an RGB tuple to HEX."""
    return "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])

def color_brightness(rgb_color):
    """Returns the brightness of an RGB color using a weighted sum method."""
    return (0.299 * rgb_color[0] + 0.587 * rgb_color[1] + 0.114 * rgb_color[2]) / 255

def color_saturation(rgb_color):
    """Returns the saturation of an RGB color."""
    r, g, b = rgb_color
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    return (max_val - min_val) / max_val if max_val != 0 else 0

def is_near_black_or_white_or_transparent(rgb_color, threshold=30):
    """Checks if the given RGB color is near black, white, or transparent."""
    return (
        (all(c <= threshold for c in rgb_color[:3])) or  # Near black
        (all(c >= (255 - threshold) for c in rgb_color[:3])) or  # Near white
        (len(rgb_color) == 4 and rgb_color[3] == 0)  # Transparent
    )

def extract_quantized_colors(image_path, num_colors=8):
    """
    Extracts quantized colors from the image, prioritizing bright or saturated colors.
    If less saturated colors dominate, they are chosen to reflect the palette.
    Returns the primary color and up to 2 secondary colors.
    """
    with Image.open(image_path) as img:
        img = img.convert("RGBA")
        img = img.resize((100, 100))
        quantized_img = img.quantize(colors=num_colors)
        palette = quantized_img.getpalette()[:num_colors * 3]
        palette_colors = [tuple(palette[i:i+3]) for i in range(0, len(palette), 3)]
        color_counts = quantized_img.getcolors()
        color_counts.sort(reverse=True, key=lambda x: x[0])

        # Filter out black, white, and transparent colors
        valid_colors = []
        for count, color_idx in color_counts:
            color = palette_colors[color_idx]
            if not is_near_black_or_white_or_transparent(color):
                valid_colors.append((color, count))

        # If fewer than 3 valid colors, add white as a placeholder
        if len(valid_colors) < 3:
            valid_colors += [((255, 255, 255), 0)] * (3 - len(valid_colors))

        # Prioritize colors by both brightness/saturation and area occupied
        valid_colors.sort(key=lambda c: (color_brightness(c[0]), color_saturation(c[0]), c[1]), reverse=True)
        primary_color = valid_colors[0][0]
        secondary_colors = [color[0] for color in valid_colors[1:3]]

        return primary_color, secondary_colors

def process_images_in_folder(root_folder):
    """Processes all images in the folder and extracts bright/saturated primary and secondary colors."""
    results = {}
    for subdir, _, files in os.walk(root_folder):
        relative_subdir = os.path.relpath(subdir, root_folder)
        if relative_subdir not in results:
            results[relative_subdir] = []
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(subdir, file)
                try:
                    primary_color, secondary_colors = extract_quantized_colors(file_path)
                    primary_color_hex = rgb_to_hex(primary_color)
                    secondary_colors_hex = [rgb_to_hex(color) for color in secondary_colors]
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
    """Saves the color data to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

def main():
    images_folder = os.path.join(os.getcwd(), 'images')
    output_file = 'colors_extracted.json'
    results = process_images_in_folder(images_folder)
    save_results_to_json(results, output_file)
    print(f"Colors extracted and saved to {output_file}")

if __name__ == "__main__":
    main()
