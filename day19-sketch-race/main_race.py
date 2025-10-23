from turtle import Turtle, Screen
import random

screen = Screen()

screen_width = 600
screen_height = 400

finish_X = screen_width / 2 - 40
start_X = - finish_X

screen.setup(screen_width, screen_height)

# Draws a finish line
def draw_finish_line():
    screen.clear()
    finish_line = Turtle(visible=False)
    finish_line.penup()
    finish_line.goto(finish_X, screen_height / 2)
    finish_line.pendown()
    finish_line.goto(finish_X, -screen_height / 2)

colors = ["blue", "green", "yellow", "orange", "red", "purple"]
turtles = []
turt_amount = 6

# Creates and evenly spreads the turtles on the start line
def setup_race():
    draw_finish_line()
    turtles.clear()

    for i in range(turt_amount):
        new_turt = Turtle(shape="turtle")
        turtles.append(new_turt)
        
        new_turt.color(colors[i])
        new_turt.penup()
        new_turt.goto(start_X, (screen_height / 2 - 30) - (i * (screen_height / turt_amount)))

# START THE RACE

money = 10
game_loop = True

while game_loop:
    setup_race()
    chosen = screen.textinput(title = "Pick a turtle", prompt = "Which turtle do you want to bet on?")
    bet = screen.numinput(title = "Make a bet", prompt = f"You have ${int(money)}.\nHow much do you want to bet?", minval=1, maxval=money)
    
    race_on = True

    while race_on:
        for turtle in turtles:
            step = random.randint(0, 15)
            turtle.forward(step)
            
            if turtle.xcor() >= finish_X :
                winner = turtles.index(turtle)
                race_on = False

    winner_color = colors[winner]

    if(winner_color == chosen):
        money += bet * 2
        input_continue = screen.textinput(title = "YOU WON!", prompt = f"CONGRATULATIONS! The {winner_color} turtle won!\nYou have ${int(money)}.\nPlay again?")
    else:
        money -= bet
        if money == 0:
            screen.textinput(title="GAME OVER", prompt= f"The {winner_color} turtle won.\nYou lost all your money.")
            input_continue = "no"
            game_loop = False
        else:
            input_continue = screen.textinput(title = "You lost...", prompt = f"The {winner_color} turtle won.\nYou have ${int(money)}.\nPlay again?")
    
    if input_continue.casefold() == "no" or input_continue.casefold() == "n":
        game_loop = False
    elif input_continue.casefold() == "yes" or input_continue.casefold() == "y":
        print("Restarting...")

screen.clear()
screen.exitonclick()