from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colours = ["green", "yellow", "red", "blue", "brown"]
turtles = [Turtle() for i in range(len(colours))]

user_bet = screen.textinput(title="Place your bet", prompt=f"Who do you bet to win ( {', '.join(colours)} )").lower()

for turtle in turtles:




#tim.goto(x=-235, y=0)

screen.exitonclick()