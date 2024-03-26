import time

import pygame
import os

# Get the paths to the GIF images
image_folder = "images"  # Replace this with the folder containing your GIF images
pygame.init()


class Face:
    def __init__(self):

        self.win = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("Jump Game")
        image_files = sorted(os.listdir(image_folder))  # Assuming the images are named in the sequence you want
        # Load the GIF images
        self.images = [pygame.image.load(os.path.join(image_folder, file)) for file in image_files]
        # player_img = pygame.image.load('1.gif')  # Replace 'player.png' with your image file path

        # Stores if player is jumping or not
        self.isjump = False

        # Force (v) up and mass m.
        self.v = 10
        self.m = 1

        # Indicates pygame is running
        self.run = True
        self.x = 0
        self.y = 0

        self.currentFace = self.images[0]

        self.i = 0

    def reg_all_shapes(self):
        pass

    def animation(self):
        while True:
            self.win.fill((0, 0, 0))

            # Calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
            F = (1 / 2) * self.m * (self.v ** 2)

            # Change in the y-coordinate
            self.y -= F

            # Decreasing velocity while going up and become negative while coming down
            v = self.v - 1

            # Object reached its maximum height
            if v < 0:
                # Negative sign is added to counter negative velocity
                m = -1

            # Object reached its original state
            if v == -11:
                # Making isjump equal to False
                isjump = False

                # Setting original values to v and m
                v = 10
                m = 1

            # Creates time delay of 10ms

            pygame.time.delay(10)

            # It refreshes the window
            pygame.display.update()

    def normal(self):
        self.win.fill((0, 0, 0))
        self.win.blit(self.currentFace, (self.x, self.y))
        self.currentFace = self.images[(len(self.images) + self.i) % len(self.images)]
        self.i += 1

        pygame.display.update()

        self.animation()

        time.sleep(.5)


face = Face()
face.normal()
face.animation()
