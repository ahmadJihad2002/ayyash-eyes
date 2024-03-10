
# screen dimentions 165 x 102
import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

# Register shapes
wn.register_shape("1.gif")
wn.register_shape("2.gif")

class Face(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.shape("1.gif")
		self.color("green")
		self.frame = 0
		self.frames = ["1.gif", "2.gif"]

	def animate(self):
		self.frame += 1
		if self.frame >= len(self.frames):
			self.frame = 0
		self.shape(self.frames[self.frame])
		# Set timer
		wn.ontimer(self.animate, 10)




player = Face()
player.animate()



while True:
	wn.update()
	print("Main Loop")

wn.mainloop()