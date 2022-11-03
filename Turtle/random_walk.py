import turtle as t
import random

tim = t.Turtle()

options = [1, 2, 3, 4]
angle = 90
length = 100

colors = ["DarkGreen", "DarkBlue", "DarkOrange", "DarkRed", "Purple", "Pink"]

tim.width(20)
tim.speed("fast")

def random_walk(steps):
    for _ in range (steps):
        option = random.choice(options)
        tim.color(random.choice(colors))
        tim.left(angle * option)
        tim.forward(100)

#random_walk(50)

directions = [0, 90, 180, 270]

def better_random_walk(steps):
    for _ in range (steps):
        tim.color(random.choice(colors))
        tim.forward(50)
        tim.setheading(random.choice(directions))

better_random_walk(100)