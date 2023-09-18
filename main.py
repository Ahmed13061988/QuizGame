import time
import turtle
import pandas

score = 0
is_game_on = True
answers = []

while is_game_on:
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    screen.tracer(6)
    data = pandas.read_csv("50_states.csv")
    states = data["state"].tolist()
    answer = turtle.textinput(title=f"{score}/50Guess The State", prompt="What's another state's name?").capitalize()
    if answer in states:
        if answer in answers:
            print("you got that already")
        else:
            state_data = data[data.state == answer]
            t = turtle.Turtle()
            answers.append(answer)
            score += 1
            t.hideturtle()
            t.penup()
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer, align="center")
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
