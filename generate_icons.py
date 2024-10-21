import os
import json
from PIL import Image, ImageDraw

def create_palette_image(image_path, palette, output_path):
    """
    Creates a 500x500 image with the original image (scaled) and a color bar at the bottom,
    with a black background.
    
    Arguments:
    - image_path: Path to the original image.
    - palette: Dictionary containing the primary and secondary colors (in RGB).
    - output_path: Path to save the generated image.
    """
    # Load and resize the original image
    original_img = Image.open(image_path)
    original_img.thumbnail((500, 380))  # Leave room for the color bar
    
    # Create a new blank 500x500 image with a black background
    new_img = Image.new("RGB", (500, 500), (0, 0, 0))  # Black background
    
    # Paste the original image on top (centered)
    img_w, img_h = original_img.size
    new_img.paste(original_img, ((500 - img_w) // 2, 0))
    
    # Create the color bar (120px high)
    draw = ImageDraw.Draw(new_img)
    
    # Get the primary and secondary colors
    primary_color = palette['primary_color']['rgb']
    secondary_colors = [color['rgb'] for color in palette['secondary_colors'][:3]]
    
    # Define bar dimensions
    bar_height = 120
    color_width = 500 // 4  # Since we have 1 primary and 3 secondary colors
    
    # Draw the primary color (first quarter of the bar)
    draw.rectangle([0, 380, color_width, 500], fill=tuple(primary_color))
    
    # Draw the secondary colors (next three quarters)
    for i, color in enumerate(secondary_colors):
        draw.rectangle([color_width * (i + 1), 380, color_width * (i + 2), 500], fill=tuple(color))
    
    # Save the resulting image
    new_img.save(output_path)
    print(f"Image saved at {output_path}")

def process_images_from_json(json_file, images_folder, output_folder):
    """
    Processes the images and their color palettes from the JSON file and generates new images.
    
    Arguments:
    - json_file: Path to the JSON file with color data.
    - images_folder: Path to the folder containing the images.
    - output_folder: Path to save the generated images.
    """
    # Load the color data from the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Process each image and its colors
    for subfolder, images in data.items():
        for image_info in images:
            image_name = image_info['image']
            palette = {
                "primary_color": image_info['primary_color'],
                "secondary_colors": image_info['secondary_colors']
            }
            image_path = os.path.join(images_folder, subfolder, image_name)
            
            # Create the subfolder in the output folder if it doesn't exist
            output_subfolder = os.path.join(output_folder, subfolder)
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            
            output_path = os.path.join(output_subfolder, f"processed_{image_name}")
            
            # Generate the palette image
            try:
                create_palette_image(image_path, palette, output_path)
            except Exception as e:
                print(f"Error processing {image_name}: {e}")

def main():
    # Define paths
    images_folder = os.path.join(os.getcwd(), 'images')
    json_file = 'colors_extracted.json'
    output_folder = 'processed_images'
    
    # Process the images and generate the output
    process_images_from_json(json_file, images_folder, output_folder)
    print("Image processing complete.")

if __name__ == "__main__":
    main()
