from PIL import Image
import os

def convert_png_to_webp():
    total_space_saved = 0  # To accumulate total space saved

    # Walk through all subdirectories and files
    for root, _, files in os.walk('.'):
        for filename in files:
            if filename.lower().endswith('.png'):
                file_path = os.path.join(root, filename)
                webp_path = file_path.rsplit('.', 1)[0] + '.webp'

                try:
                    # Get the initial file size
                    initial_size = os.path.getsize(file_path)

                    # Open the PNG image
                    with Image.open(file_path) as img:
                        # Convert and save as WebP
                        img.save(webp_path, 'WEBP', quality=85)  # Adjust quality if needed
                        
                        # Get the new WebP file size
                        new_size = os.path.getsize(webp_path)
                        
                        # Calculate the space saved and add to total
                        space_saved = initial_size - new_size
                        total_space_saved += space_saved
                        print(f"Converted: {file_path} | Saved {space_saved} bytes")
                    
                    # Optionally delete the original PNG file
                    os.remove(file_path)
                
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    # Print total space saved
    print(f"\nTotal space saved: {total_space_saved} bytes")

# Run the conversion function in the current directory
convert_png_to_webp()
