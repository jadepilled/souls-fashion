import os
from PIL import Image

def extract_first_frame(input_path, output_path):
    # Open the animated WEBP file
    with Image.open(input_path) as img:
        # Check if the image is animated
        if img.is_animated:
            # Seek to the first frame
            img.seek(0)
        # Save the first frame as a separate image
        img.save(output_path, format="WEBP")  # Saving as WEBP format

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Loop through all files in the directory
for filename in os.listdir(current_directory):
    # Process only .webp files
    if filename.lower().endswith(".webp"):
        input_path = os.path.join(current_directory, filename)
        # Create output file name with "_placeholder" suffix
        output_path = os.path.join(current_directory, f"{os.path.splitext(filename)[0]}_placeholder.webp")
        
        # Extract and save the first frame
        extract_first_frame(input_path, output_path)
        print(f"Extracted first frame from {filename} and saved as {output_path}")
