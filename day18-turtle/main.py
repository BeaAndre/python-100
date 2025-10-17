from turtle import Turtle, Screen
from random import randint
import colorgram

tim = Turtle()
screen = Screen()

screen.title("Turtle Drawings")

tim.shape("turtle")
tim.color("green")
tim.speed(100)

def randomColor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

## POLYGONS

screen.colormode(255)
tim.pensize(5)

figures = 8
sides = 3

for _ in range(figures):
    tim.pencolor(randomColor())
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)
    sides += 1

tim.clear()

# RANDOM WALK - RIGHT ANGLES

directions = [0, 90, 180, 270]
tim.setposition(0, 0)
tim.pensize(10)

for _ in range(100):
    tim.pencolor(randomColor())
    if(randint(1,2) == 1):
        tim.right(directions[randint(0,3)])
    else:
        tim.left(directions[randint(0,3)])
    tim.forward(randint(0, 50))
    
tim.clear()
tim.penup()

# RANDOM WALK - ANY ANGLE

tim.setposition(0, 0)
tim.pendown()

for _ in range(100):
    tim.pencolor(randomColor())
    tim.right(randint(0, 360))
    tim.forward(randint(0, 50))
    
screen.clearscreen()
screen.colormode(255)

# CIRCLES

tim.home()
tim.pensize(3)

color_step = 20

for _ in range(18):
    tim.pencolor(randomColor())
    tim.circle(100)
    tim.right(20)

screen.clearscreen()

# COLORGRAM

screen.colormode(255)
tim.hideturtle()
tim.penup()

colors = []
extracted_colors = colorgram.extract('day18-turtle/test_img.png', 4)

for color in extracted_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors.append((r, g, b))

increment = 1
dots_amount = 8
distance = 35

tim.dot(20, colors[randint(0, 3)])

for _ in range(4):
    for times in range(dots_amount):
        tim.home()
        tim.left(360 / dots_amount * times )
        tim.forward(distance * increment)
        tim.dot(20, colors[randint(0, 3)])
    dots_amount += 5
    increment += 1

screen.exitonclick()
# END