import turtle
import pandas


screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states =[]
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 State correct",prompt="Whats another state's name?").title()
    print(answer_state)

    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)




screen.exitonclick()