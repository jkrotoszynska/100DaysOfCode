import turtle as t
import random

tim = t.Turtle()

options = [1, 2, 3, 4]
angle = 90
length = 100

colors = ["DarkGreen", "DarkBlue", "DarkOrange", "DarkRed", "Purple", "Pink"]

def random_walk(steps):
    for i in range (steps):
        option = random.choice(options)
        tim.width(20)
        tim.color(random.choice(colors))
        tim.left(angle * option)
        tim.forward(100)

random_walk(50)