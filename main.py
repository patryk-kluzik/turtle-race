from turtle import Turtle, Screen
import random

screen = Screen()
width = 500
height = 400
screen.setup(width=width, height=height)

is_race_on = False
winner = ''

colours = ["green", "yellow", "red", "blue", "brown",  "orange"]
turtles = [Turtle("turtle") for i in range(len(colours))]


user_bet = screen.textinput(title="Place your bet", prompt=f"Who do you bet to win ( {', '.join(colours)} )").lower()

counter = 0
padding = 100
space_between = (height-padding) / (len(colours)-1)
y_axis = (height - padding)/2
for turtle in turtles:
    turtle.penup()
    turtle.color(colours[counter])
    turtle.goto(x=-235, y=y_axis)
    y_axis -= space_between
    counter += 1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= (width/2)-30:
            is_race_on = False
            winner = turtle.color()[0]

if user_bet == '':
    print("You failed to make a choice")
elif winner == user_bet:
    print(f"You won, You bet {user_bet} and {winner} won!")
else:
    print(f"You loose! You bet on {user_bet} but {winner} won.")
screen.exitonclick()
