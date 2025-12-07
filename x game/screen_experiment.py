import turtle
import time
import random


screen = turtle.Screen()
basket = turtle.Turtle()
object1 = turtle.Turtle()
scoreboard = turtle.Turtle()
screen.addshape("yellow.gif")
screen.addshape("basket.gif")
screen.addshape("star.gif")

scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0,300)

score = 0

screen.bgpic("yellow.gif")
basket.penup()

turtle.title("Screen experiment")

turtle.setup(width = 810, height=847, startx =0,starty=0)
turtle.screensize(canvwidth = 800,canvheight= 800)
basket.goto(0,-380)
basket.shape("basket.gif")

object1.penup()
object1.goto(-380,380)
object1.shape("star.gif")

def right():
    basket.forward(5)
def left():
    basket.backward(5)

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")

turtle.listen()
def move():
    y = object1.ycor()
    object1.sety(y-3)

while True:
    screen.update()
    move()

    if object1.ycor()<-400:
        object1.hideturtle()
        x=random.randint(-380,380)
        object1.goto(x,380)
        object1.showturtle()

    if basket.distance(object1)<40:
        object1.hideturtle()
        score = score + 1
        scoreboard.clear()
        scoreboard.write("score:{}".format(score),font=("castellar",24,"bold"))    
        x=random.randint(-380,380)
        object1.goto(x,380)
        object1.showturtle()

    if object1.ycor()<-395:
        score = score - 1

    if score == -5: 
        scoreboard.clear()
        scoreboard.write("game over",font=("castellar",24,"bold"))
        break

turtle.done()