import os
import random
import tkinter as tk
from PIL import Image, ImageTk

image_dimensions =(14400,9060)


class ImageMonitor:
    def __init__(self, master, image_folder):
        self.master = master
        self.image_folder = image_folder
        self.image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
        self.image_files = sorted(self.image_files, key=lambda x: int(x.split('.')[0]))
        print(self.image_files)
        self.current_index = 0

        self.load_image()
        self.create_widgets()
        self.display_image()

    def load_image(self):
        image_path = os.path.join(self.image_folder, self.image_files[self.current_index])
        image = Image.open(image_path)
        image.thumbnail(image_dimensions)
        self.photo = ImageTk.PhotoImage(image,size=(random.randint(100,5000),random.randint(200,5000),))

    def create_widgets(self):
        self.label = tk.Label(self.master, image=self.photo)
        self.label.pack()

    def display_image(self):
        self.load_image()
        self.label.configure(image=self.photo)
        self.current_index = (self.current_index + 1) % len(self.image_files)
        self.master.after(1, self.display_image)  # Change the delay here (in milliseconds)


def main():
    root = tk.Tk()
    root.title("Image Monitor")
    root.attributes('-fullscreen', True)

    # Specify the path to the folder containing images
    image_folder = "./Happy"  # Change this to your image folder path

    if not os.path.exists(image_folder):
        print(f"Image folder '{image_folder}' not found.")
        root.destroy()
        return

    monitor = ImageMonitor(root, image_folder)

    root.mainloop()


if __name__ == "__main__":
    main()
