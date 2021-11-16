from turtle import Screen, Turtle
import turtle
import pandas

MAP_US = "blank_states_img.gif"

screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.addshape(MAP_US)

map_image = Turtle()
map_image.shape(MAP_US)

writer = Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
dataset = data.state
states = dataset.to_list()

states_correct = 0
count_states = len(states)
while states_correct < count_states:
    awnser_state = screen.textinput(
        title=f"{states_correct}/{50} States Correct", prompt="What's another state's name?").title()

    if awnser_state == "Exit":
        new_data = pandas.DataFrame(states)
        new_data.to_csv("states_to_learn.csv")
        break

    if awnser_state in states:
        state_row = data[dataset == awnser_state]
        writer.goto((int(state_row.x), int(state_row.y)))
        writer.write(awnser_state.upper())
        states.remove(awnser_state)
        states_correct += 1

    if states_correct == 50:
        writer.home()
        writer.write("Discovered America! 🇺🇸", align="center", font=("Courier", 42, "bold"))


turtle.mainloop()
