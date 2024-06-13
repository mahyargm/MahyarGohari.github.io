import os
from PIL import Image
import glob

# Create the 'tn' directory if it doesn't exist
os.makedirs('tn/images', exist_ok=True)
# Loop through all .jpg and .png files in the 'images' directory
for file_path in glob.glob('images/*', recursive=True):
    # Get the filename without the directory path
    filename = os.path.basename(file_path)
    output_file = os.path.join('tn/images/', filename)

    # Check if the output file already exists
    if not os.path.exists(output_file):

        # Open the input image
        with Image.open(file_path) as img:
            # Create a thumbnail image
            img.thumbnail((160, 160))
            # Save the thumbnail image
            img.save(output_file)
            print(f"Created thumbnail for {filename}")
