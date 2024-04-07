import os

import shutil


def rename_and_move_files(file_list, destination_folder):
    if not file_list:
        print("No files to rename.")
        return

    num_files = len(file_list)
    digits = len(str(num_files - 1))

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for i, file_name in enumerate(file_list):
        file_extension = os.path.splitext(file_name)[1]
        new_name = f"{str(i).zfill(digits)}{file_extension}"
        try:
            new_path = os.path.join(destination_folder, new_name)
            shutil.move(file_name, new_path)
            print(f"Moved and renamed {file_name} to {new_path}")
        except Exception as e:
            print(f"Failed to move and rename {file_name}: {str(e)}")


#
# # Example usage:
# file_list = ["file1.txt", "file2.txt", "file3.txt"]  # Add your list of files here

def load_png_images_from_folder(folder_path):
    png_images = []
    for filename in os.listdir(folder_path):
        # if filename.endswith('.png'):
        png_images.append(os.path.join(folder_path, filename))
    return png_images


rename_and_move_files(load_png_images_from_folder("Blink"), "Blink")
