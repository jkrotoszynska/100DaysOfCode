import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("50_states.csv")
state_column = data.state.to_list()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if answer_state in state_column:
        print("true!")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_xy = data[data.state == answer_state]
        t.goto(int(state_xy.x), int(state_xy.y))
        t.write(answer_state)

def get_mouse_click_coor(x,y):
    print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

screen.exitonclick()