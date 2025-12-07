import turtle
import time
import random
import threading

screen = turtle.Screen()

screen.screensize(canvwidth=1424,canvheight=800)
screen.setup(width=1424,height=800)
screen.title("locator")
ship = turtle.Turtle()
planet = turtle.Turtle()
scoreboard = turtle.Turtle()
ship.speed(1000)
screen.addshape("space.gif")
screen.addshape("rocket_up.gif")
screen.addshape("rocket_down.gif")
screen.addshape("rocket_left.gif")
screen.addshape("rocket_right.gif")
screen.addshape("planet.gif")


score = 0
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0,200)
scoreboard.color("green")

planet.speed(1)
planet.shape("planet.gif")

screen.bgpic("space.gif")
ship.shape("rocket_up.gif")
ship.penup()

def move():
    def up():
        ship.shape("rocket_up.gif")
        ship.seth(90)
        ship.fd(10)
        ship.seth(0)

    def down():
        ship.shape("rocket_down.gif")
        ship.seth(270)
        ship.fd(10)
        ship.seth(0)

    def right():
        ship.shape("rocket_right.gif")
        ship.fd(10)

    def left():
        ship.shape("rocket_left.gif")
        ship.bk(10)

    turtle.onkeypress(up,"Up")
    turtle.onkeypress(down,"Down")
    turtle.onkeypress(right,"Right")
    turtle.onkeypress(left,"Left")
    turtle.listen()

def planet_mover():
    while True:
        screen.update()
        planet.penup()
        x =random.randint(-500,500)
        y= random.randint(-100,100)
        planet.goto(x,y)
        time.sleep(5)
    

        if ship.distance(planet) < 192:
            global score
            score += 1
            print("Score:",score)
        
        if score > 10:
            planet.hideturtle()
            ship.shape("rocket_right.gif")
            ship.goto(440,220)
            break
           
def scorer():
    while True:
        time.sleep(0.2)
        scoreboard.clear()
        scoreboard.write("Score:{}".format(score),align="center",font=("arial",16,"bold"))

        if score > 10:
            scoreboard.clear()
            scoreboard.write("You Have Won The game!",font=("arial",24,"bold"))
            threading.current_thread()._stop()
            break
            


t0 = threading.Thread(target = move)
t1 = threading.Thread(target = planet_mover)
t2 = threading.Thread(target = scorer)
t0.start()
t1.start()
t2.start()

turtle.done()