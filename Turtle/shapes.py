import turtle as t
import random

tim = t.Turtle()

colors = ["Yellow", "Green", "Pink", "Blue", "Orange", "Red", "Purple"]

def shape(num_sides):
    angle = 360 / num_sides
    for x in range(num_sides):
        tim.forward(100)
        tim.left(angle)

def draw():
    for i in range(4,11):
        tim.color(random.choice(colors))
        shape(i)

draw()