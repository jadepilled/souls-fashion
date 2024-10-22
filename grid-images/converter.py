import os
from PIL import Image
import subprocess

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

def compress_webp(webp_file):
    """Compress WEBP file using cwebp."""
    compressed_file = f"{os.path.splitext(webp_file)[0]}_compressed.webp"
    subprocess.run(["cwebp", "-q", "80", webp_file, "-o", compressed_file])  # Adjust quality as needed
    return compressed_file

def convert_and_compress(apng_directory):
    """Convert all animated PNG files in a directory to WEBP and compress them."""
    for filename in os.listdir(apng_directory):
        if filename.lower().endswith('.apng') or filename.lower().endswith('.png'):
            apng_file = os.path.join(apng_directory, filename)
            webp_file = os.path.splitext(apng_file)[0] + ".webp"
            print(f"Converting {apng_file} to {webp_file}...")
            convert_apng_to_webp(apng_file, webp_file)

            print(f"Compressing {webp_file}...")
            compressed_file = compress_webp(webp_file)
            print(f"Compressed file saved as {compressed_file}")

if __name__ == "__main__":
    apng_dir = input("Enter the directory containing animated PNG files: ")
    convert_and_compress(apng_dir)
