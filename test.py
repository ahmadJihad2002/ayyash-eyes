import logging
import os
import time

import turtle

import keyboard

screenHeight = 1.0
screenWidth = 1.0
wn = turtle.Screen()
wn.setup(screenWidth, screenHeight)
wn.title("Animation Demo")
wn.bgcolor("black")
turtle.penup()

# Directory path
directory = 'thinking'

# Get the list of files in the directory
files = os.listdir(directory)
filtered_files = [file for file in files if not file.startswith('.DS_Store')]
print(filtered_files)
# filtered_files = sorted(filtered_files, key=lambda x: int(x.split('_')[1].split('.')[0]))
# filtered_files = sorted(filtered_files, key=lambda x: int(x.split('.')[0]))
filtered_files = sorted(filtered_files)
print(filtered_files)
for image in filtered_files:
    wn.register_shape(directory + "/" + image)

#
# image_folder = "Blink"
# win = pygame.display.set_mode((1000, 1000))
# pygame.display.set_caption("Jump Game")
# image_files = sorted(os.listdir(image_folder))

# Assuming the images are named in the sequence you want
# Load the GIF images

frame_count = {'blink': 47,
               'thinking': 23,
               # 'happy':60, 'sad':47,'dizzy':67,'excited':24,'neutral':61,'happy2':20,'angry':20,'happy3':26,'bootup3':124,'blink2':20
               }


def show(emotion="thinking", count=4):
    for j in range(frame_count[emotion]):
        print(j)

        turtle.shape(directory + "/" + filtered_files[j])
        # time.sleep(0.05)

        wn.delay(100)
        # image = Image.open('Blink-0/' + str(i) + '.png')

        # win.blit(image, (0, 0))
        # pygame.display.update()


def show_thinking(emotion="blink", count=4):
    for j in range(frame_count[emotion]):
        print(j)

        turtle.shape(directory + "/" + filtered_files[j])
        time.sleep(0.05)
        # wn.delay(50)
        # image = Image.open('Blink-0/' + str(i) + '.png')
        # win.fill((0, 0, 0))
        # win.blit(image, (0, 0))
        # pygame.display.update()


#

if __name__ == "__main__":
    # while True:
    #     if keyboard.is_pressed('space'):
            show()
