import cv2
import numpy as np

class Face(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.motion_speed = 1
        self.size = 1
        self.shapesize(self.size)
        self.speed(self.motion_speed)

        self.x_position = 0
        self.y_position = 0

    def animate(self):
        # self.motion_speed =random.randint(1, 10)
        while True:
            self.motion_speed = speed_data[i + 1 % len(speed_data)]

        self.goto(self.x_position, self.y_position)



