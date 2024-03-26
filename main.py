# screen dimentions 165 x 102

import time
import turtle
import random
import threading

#  max value for method gotTo x, and y
maxPoint = 120
minPoint = -120

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

# wn.register_shape("1.gif")
# wn.register_shape("2.gif")
# wn.register_shape("3.gif")
print('done')
randomLooking = True

# speed_pattern = [20, 19, 17, 15, 14, 13, 11, 10, 7, 4, 3, 1]
# speed_pattern = [9, 10, 30, 60, 50, ]
speed_pattern = [3, 10, 20, 50, 40,15 ]

i = 0

wn.tracer(0)


# # Object current coordinates
# x = 0
# y = 0


class Face(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.currentFace = 'normal.gif'
        self.shape(self.currentFace)
        self.penup()
        self.motion_speed = 6

        self.speed(self.motion_speed)

        self.x_position = 0
        self.y_position = 0
        self.currentLook = (1, 1)

    def look_right_up(self):
        for speed in speed_pattern:
            if self.x_position < maxPoint or self.y_position < maxPoint:

                if self.currentLook == (1, 1):
                    break
                elif self.currentLook == (-1, 1):
                    self.x_position += speed
                elif self.currentLook == (1, -1):
                    self.y_position += speed
                elif self.currentLook == (-1, -1):
                    self.y_position += speed
                    self.y_position += speed
                self.goto(self.x_position, self.y_position)
                wn.update()

        self.x_position = maxPoint
        self.y_position = maxPoint
        self.goto(self.x_position, self.y_position)
        self.currentLook = (1, 1)
        wn.update()

    def look_left_up(self):
        for speed in speed_pattern:
            if self.x_position > minPoint or self.y_position < maxPoint:

                if self.currentLook == (1, 1):
                    self.x_position -= speed
                elif self.currentLook == (-1, 1):
                    break
                elif self.currentLook == (1, -1):
                    self.x_position -= speed
                    self.y_position += speed
                elif self.currentLook == (-1, -1):
                    self.y_position += speed

                self.goto(self.x_position, self.y_position)
                wn.update()

        self.x_position = minPoint
        self.y_position = maxPoint
        self.goto(self.x_position, self.y_position)
        self.currentLook = (-1, 1)
        wn.update()

    def look_right_down(self):
        for speed in speed_pattern:
            if self.x_position < maxPoint or self.y_position > minPoint:

                if self.currentLook == (1, 1):
                    self.y_position -= speed
                elif self.currentLook == (-1, 1):
                    self.x_position += speed
                    self.y_position -= speed
                elif self.currentLook == (1, -1):
                    break
                elif self.currentLook == (-1, -1):
                    self.x_position += speed
                print(self.x_position)

                self.goto(self.x_position, self.y_position)
                wn.update()

        self.x_position = maxPoint
        self.y_position = minPoint
        self.goto(self.x_position, self.y_position)
        self.currentLook = (1, -1)
        wn.update()

    def look_left_down(self):
        for speed in speed_pattern:
            if self.x_position > minPoint or self.y_position > minPoint:

                if self.currentLook == (1, 1):
                    self.y_position -= speed
                    self.x_position -= speed
                elif self.currentLook == (-1, 1):
                    self.y_position -= speed
                elif self.currentLook == (1, -1):
                    self.x_position -= speed
                elif self.currentLook == (-1, -1):
                    break

                self.goto(self.x_position, self.y_position)
                wn.update()

        self.x_position = minPoint
        self.y_position = minPoint
        self.goto(self.x_position, self.y_position)
        self.currentLook = (-1, -1)
        wn.update()

    def look_down(self):
        for speed in speed_pattern:
            if self.x_position != minPoint or self.y_position > minPoint:

                if self.currentLook == (1, 1):
                    self.y_position -= speed
                    self.x_position -= speed
                elif self.currentLook == (-1, 1):
                    self.y_position -= speed
                elif self.currentLook == (1, -1):
                    self.x_position -= speed
                elif self.currentLook == (-1, -1):
                    break

                self.goto(self.x_position, self.y_position)
                wn.update()

        self.x_position = 0
        self.y_position = minPoint
        self.goto(self.x_position, self.y_position)
        self.currentLook = (-1, -1)
        wn.update()
    # # Set timer
    # wn.ontimer(self.movement(), 50)

    def animation(self):
        while True:
            x = random.randint(self.x_position, self.x_position + 5)
            y = random.randint(self.y_position, self.y_position + 5)
            self.goto(x, y)
            time.sleep(random.uniform(0.1, 0.5))
            wn.update()

    # def normal(self):
    #     while True:
    #         self.shape('normal.gif')
    #
    #         time.sleep(1)
    #
    #         wn.update()

    # wn.ontimer(self.normal, 50)

    # wn.ontimer(self.transaction('2.gif'), 1000)

    def transaction(self, nextFace):

        self.currentFace = nextFace
        self.shape(nextFace)
        self.shapesize()
        time.sleep(0.1)

        # Turn on turtle animation for future updates


class behavoure:
    def __init__(self):
        self.face = Face()
        pass

    def angry(self):

        self.face.look_left_up()

        pass


if __name__ == "__main__":
    face = Face()


    # face.normal()

    while True:
        time.sleep(0.1)

        face.look_right_down()
        time.sleep(0.1)

        # face.look_left_down()
        # time.sleep(0.1)
        #
        # face.look_left_up()
        # time.sleep(0.1)

        face.look_right_up()

        if randomLooking:

            face.transaction(nextFace=facesList[(len(facesList) + i) % len(facesList)])
            i += 1
        else:
            continue

        wn.update()
        print('done')
        maxPoint = random.randint(70, 140)
        minPoint = -1 * maxPoint
