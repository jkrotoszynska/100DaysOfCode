from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DeepPink")

# square
def square():
    for x in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)

#dashed line
def dashed_line():
    for x in range(10):
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        

#square()
dashed_line()

screen = Screen()
screen.exitonclick()