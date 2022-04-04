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
used_states = []
state_to_learn = []
all_states = data["state"].to_list()

while correct_answer < number_of_states:
    input = screen.textinput(title=f"{correct_answer}/{number_of_states} Guess the state:",
                             prompt="What's another state name?").capitalize()

    if input == "Exit":

        for state in all_states:
            if not state in used_states:
                state_to_learn.append(state)
        df_learn_state = pandas.DataFrame(state_to_learn)
        df_learn_state.to_csv("states_to_learn.csv")
        break
    if not len(data[data["state"] == input]) == 0:
        correct_answer += 1
        state_name = turtle.Turtle()
        state_name.penup()
        state_data = data[data["state"] == input]
        state_name.setpos(int(state_data.x), int(state_data.y))
        state_name.write(input)
        state_name.hideturtle()
        used_states.append(input)
