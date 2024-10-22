import os
from PIL import Image
import subprocess

def compress_webp(webp_file):
    """Compress WEBP file using cwebp."""
    compressed_file = f"{os.path.splitext(webp_file)[0]}_compressed.webp"
    # Run the cwebp command to compress the file
    subprocess.run(["cwebp", "-q", "80", webp_file, "-o", compressed_file])  # Adjust quality as needed
    return compressed_file

def compress_animated_webp(webp_file):
    """Compress animated WEBP file and retain animation."""
    with Image.open(webp_file) as img:
        frames = []
        for frame in range(img.n_frames):
            img.seek(frame)
            frames.append(img.copy())
        
        # Save frames as a compressed WEBP animation
        compressed_file = f"{os.path.splitext(webp_file)[0]}_compressed.webp"
        frames[0].save(compressed_file, save_all=True, append_images=frames[1:], loop=0)
        return compressed_file

def process_webp_files():
    """Process all WEBP files in the current directory."""
    for filename in os.listdir('.'):
        if filename.lower().endswith('.webp'):
            print(f"Processing {filename}...")
            compressed_file = compress_animated_webp(filename)
            print(f"Compressed file saved as {compressed_file}")

if __name__ == "__main__":
    process_webp_files()
