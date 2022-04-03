import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)

data = pandas.read_csv("50_states.csv")
number_of_states = len(data["state"])
correct_answer = 0

while correct_answer < number_of_states:
    input = screen.textinput(title=f"{correct_answer}/{number_of_states} Guess the state:",
                             prompt="What's another state name?").capitalize()

    if not len(data[data["state"] == input]) == 0:
        correct_answer +=1
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.setpos(data[data["state"] == input].x[0], data[data["state"] == input].y[0])
        state_name.write(input)
