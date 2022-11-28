from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
       super().__init__()
       self.shape("square")
       self.penup()
       self.color(COLORS[random.randint(0,5)])
       self.shapesize(stretch_wid=1, stretch_len=3)
       gen_y = random.randint(-250,250)
       self.goto(290, gen_y)

    def running(self):
        self.forward()