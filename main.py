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
    answer = turtle.textinput(title=f"{score}/50 Guess The State", prompt="What's another state's name?").title()

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
    elif answer == "Exit":
        is_game_on = False
        print("you are leaving")
        states_to_learn = list(set(states).difference(answers))
        states_dict = {
            "state": states_to_learn
        }
        final = pandas.DataFrame(states_dict)
        final.to_csv("learn.csv")

    else:
        is_game_on = False
        states_to_learn = set(states).difference(answers)
        states_to_learn.to_csv("/learn")
        print("There is no state like that, you lose!")


