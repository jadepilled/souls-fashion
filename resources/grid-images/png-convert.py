import os
from PIL import Image

def convert_apng_to_webp(apng_file, output_file):
    """Convert animated PNG to WEBP while retaining animation."""
    with Image.open(apng_file) as img:
        # Ensure the file is an animated PNG
        if not img.is_animated:
            raise ValueError(f"{apng_file} is not an animated PNG.")
        
        # Create a list of frames
        frames = []
        for frame in range(img.n_frames):
            img.seek(frame)
            # Append the frame to the list
            frames.append(img.copy())

        # Save frames as a WEBP animation
        frames[0].save(output_file, save_all=True, append_images=frames[1:], loop=0)

def convert_apng_files():
    """Convert all animated PNG files in the current directory to WEBP."""
    for filename in os.listdir('.'):
        if filename.lower().endswith('.apng') or filename.lower().endswith('.png'):
            apng_file = os.path.join('.', filename)
            webp_file = os.path.splitext(apng_file)[0] + ".webp"
            print(f"Converting {apng_file} to {webp_file}...")
            try:
                convert_apng_to_webp(apng_file, webp_file)
                print(f"Successfully converted to {webp_file}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    convert_apng_files()
