from turtle import Turtle, Screen

text = Turtle()
pen = Turtle()
screen = Screen()

# Write instructions text on the screen
text.hideturtle()
text.penup()
text.goto(-50, 350)
text.write("ARROW KEYS to move\nC to clear screen")

movement_state = {"up": False,
                  "down": False,
                  "right": False,
                  "left": False}

def move(direction):
    movement_state[direction] = True

def move_stop(direction):
    movement_state[direction] = False

def clear_screen():
    pen.penup()
    pen.clear()
    pen.home()
    pen.pendown()
    
def game_loop():
    if movement_state["up"]:
        pen.forward(10)
    if movement_state["down"]:
        pen.backward(10)
    if movement_state["right"]:
        pen.right(15)
    if movement_state["left"]:
        pen.left(15)
        
    screen.ontimer(game_loop, 50)

screen.listen()

screen.onkeypress(key="Up", fun = lambda: move("up"))
screen.onkeyrelease(key="Up", fun = lambda: move_stop("up"))

screen.onkeypress(key="Down", fun = lambda: move("down"))
screen.onkeyrelease(key="Down", fun = lambda: move_stop("down"))

screen.onkeypress(key="Right", fun = lambda: move("right"))
screen.onkeyrelease(key="Right", fun = lambda: move_stop("right"))

screen.onkeypress(key="Left", fun = lambda: move("left"))
screen.onkeyrelease(key="Left", fun = lambda: move_stop("left"))

screen.onkey(key="c", fun=clear_screen)

game_loop()

screen.exitonclick() 