import turtle as t
import random

turtle = t.Turtle()

t.colormode(255)
turtle.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

screen = t.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)

spirograph(10)

screen.exitonclick()