# screen dimentions 165 x 102

import time
import turtle
import random

screenHeight = 1.0
screenWidth = 1.0
wn = turtle.Screen()
wn.setup(screenWidth, screenHeight)
wn.title("Animation Demo")
wn.bgcolor("black")

facesList = ['normal.gif', 'angry.gif', 'happy.gif', 'skeptic.gif', 'surprised.gif']
# wn.tracer(0)  # Turn off animation
for face in facesList:
    wn.register_shape(face)

wn.register_shape("1.gif")
wn.register_shape("2.gif")
wn.register_shape("3.gif")
print('done')
randomLooking = True

speed_data = [1, 3, 5, 10, 5, 3, 1]


i = 0


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



        # self.goto(0, 0)
        # self.goto(-100, -200)
        # Set timer
        wn.ontimer(self.animate, 50)

    def normal(self):
        self.currentFace = '1.gif'
        self.shape('1.gif')

        time.sleep(0.1)
        # wn.ontimer(self.normal, 50)
        wn.ontimer(self.transaction('2.gif'), 1000)

    def angry(self):
        self.currentFace = '2.gif'
        self.shape('1.gif')
        time.sleep(0.1)
        wn.ontimer(self.normal, 50)

    def transaction(self, nextFace):
        self.currentFace = nextFace
        self.shape(nextFace)
        time.sleep(0.1)

        # Turn on turtle animation for future updates


face = Face()
face.normal()
face.animate()
i = 0
while True:

    if randomLooking:
        face.y_position = random.randint(-100, 100)
        face.x_position = random.randint(-100, 100)
        face.transaction(nextFace=facesList[(len(facesList) + i) % len(facesList)])
        i += 1
    else:
        continue

    wn.update()
    print('done')
