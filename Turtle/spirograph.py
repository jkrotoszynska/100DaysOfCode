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


def spirograph(numbers):
    angle = 360 / numbers
    for x in range(1,numbers):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(x*angle)

screen = t.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)

spirograph(80)

screen.exitonclick()