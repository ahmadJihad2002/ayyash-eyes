from PIL import Image
import os

folder_path = 'think/PNG'
output_directory = 'thinking'


def convert_images_to_gif(image_list, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through each image in the list
    for i, image_path in enumerate(image_list):
        # Open the image
        image = Image.open(image_path)

        # Construct the output file path
        output_file_path = os.path.join(output_directory, f'image_{i}.gif')

        # Convert image to GIF and save
        image.save(output_file_path, 'GIF')


def load_png_images_from_folder(folder_path):
    png_images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            png_images.append(os.path.join(folder_path, filename))
    return png_images




# Example usage

png_images = load_png_images_from_folder(folder_path)
print(png_images)
# Example usage

convert_images_to_gif(png_images, output_directory)




# renaming
