import os
from PIL import Image, ImageDraw

def create_image_with_colors(image_path, primary_color, secondary_colors, output_path):
    """Creates a 500x500 image with a centered image and a 120px bottom bar showing the primary and secondary colors."""
    with Image.open(image_path) as img:
        # Resize image to fit within 500x380
        img.thumbnail((500, 380))
        
        # Create a new image with a black background
        result_img = Image.new("RGB", (500, 500), "black")
        
        # Calculate coordinates to center the image
        img_width, img_height = img.size
        x_offset = (500 - img_width) // 2
        y_offset = (380 - img_height) // 2
        
        # Paste the original image at the calculated position
        result_img.paste(img, (x_offset, y_offset))

        # Create the 120px bottom bar
        draw = ImageDraw.Draw(result_img)
        bar_height = 120
        color_box_width = 500 // 3

        # Draw the primary color and two secondary colors in the bar
        draw.rectangle([(0, 380), (color_box_width, 500)], fill=primary_color)
        draw.rectangle([(color_box_width, 380), (2 * color_box_width, 500)], fill=secondary_colors[0])
        draw.rectangle([(2 * color_box_width, 380), (500, 500)], fill=secondary_colors[1])

        # Save the resulting image
        result_img.save(output_path)
        print(f"Image saved to {output_path}")

def process_images(input_folder, output_folder, color_data):
    """Processes all images in the input folder and creates a 500x500 image with color bars."""
    for subdir, _, files in os.walk(input_folder):
        relative_subdir = os.path.relpath(subdir, input_folder)
        output_subdir = os.path.join(output_folder, relative_subdir)
        
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)
        
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(subdir, file)
                output_path = os.path.join(output_subdir, file)

                # Find the color data for this image
                subfolder_colors = color_data.get(relative_subdir, [])
                image_colors = next((item for item in subfolder_colors if item["image"] == file), None)
                
                if image_colors:
                    primary_color = tuple(image_colors["primary_color"]["rgb"])
                    secondary_colors = [tuple(c["rgb"]) for c in image_colors["secondary_colors"][:2]]

                    # Create the image with color bar
                    create_image_with_colors(image_path, primary_color, secondary_colors, output_path)

def load_colors_from_json(json_file):
    """Loads the color data from the JSON file."""
    import json
    with open(json_file, 'r') as f:
        return json.load(f)

def main():
    input_folder = os.path.join(os.getcwd(), 'images')
    output_folder = os.path.join(os.getcwd(), 'processed_images')
    json_file = 'colors_extracted.json'

    # Load the color data from the JSON file
    color_data = load_colors_from_json(json_file)

    # Process images and create 500x500 images with color bars
    process_images(input_folder, output_folder, color_data)

if __name__ == "__main__":
    main()
