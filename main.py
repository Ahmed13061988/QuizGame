import time
import turtle
import pandas
import csv

import pandas as pd

score = 0
is_game_on = True
answers = []

while is_game_on:
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pandas.read_csv("50_states.csv")
    states = data["state"].tolist()
    answer = turtle.textinput(title=f"{score}/50Guess The State", prompt="What's another state's name?").capitalize()
    if answer in states:
        if answer in answers:
            print("you got that already")
        else:
            answers.append(answer)
            score += 1
    else:
        is_game_on = False
        print("There is no state like that, you lose!")

# states = data[data.state == answer]
# series_states = states.squeeze()
# state = series_states.iloc[0]
# x = series_states.iloc[1]
# y = series_states.iloc[2]
# print(state, x, y)

# turtle.write(answer)
# turtle.goto(x, y)


turtle.mainloop()
