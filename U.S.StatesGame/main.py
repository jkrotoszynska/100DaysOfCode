import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("50_states.csv")
state_column = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(state_column):
    count = len(guessed_states)
    answer_state = screen.textinput(title = f"{count}/50 States Correct", prompt = "What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_column if state not in guessed_states]
        # missing_states = []
        # for state in state_column:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_column:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_xy = data[data.state == answer_state]
            t.goto(int(state_xy.x), int(state_xy.y))
            t.write(answer_state)

