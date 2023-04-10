import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
score = 0
correct_answers = []


game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{score}/50 States Correct",
                              prompt="What's the state's name?").title()
    if answer == "Exit":
        game_is_on = False

    if answer in states and answer not in correct_answers:
        t = turtle.Turtle()
        t.penup()
        t.ht()
        state_xcor = int(data[data["state"] == answer].x)
        state_ycor = int(data[data["state"] == answer].y)
        t.goto((state_xcor, state_ycor))
        t.write(answer)
        correct_answers.append(answer)
        score += 1
        screen.title("{score}/50 States Correct")
    if len(correct_answers) == 50:
        game_is_on = False


states_to_learn = [state for state in states if state not in correct_answers]
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")


turtle.mainloop()
