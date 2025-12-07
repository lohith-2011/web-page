import turtle
import time
import sys
import random, threading

def emergency_exit():
    sys.exit()


password = turtle.textinput("password","enter the license key ")

if password == "mia2024":

    jj = turtle.Turtle()
    jjspeech = turtle.Turtle()
    mia = turtle.Turtle()
    miaspeech = turtle.Turtle()
    w = turtle.Turtle()
    wi = turtle.Turtle()
    image = turtle.Turtle()
    p = turtle.Turtle()
    pan = turtle.Turtle()
    screen = turtle.Screen()
    basket = turtle.Turtle()
    object1 = turtle.Turtle()
    scoreboard = turtle.Turtle()
    screen.addshape("47.gif")
    screen.addshape("21.gif")
    screen.addshape("20.gif")

    w.penup()
    wi.penup()

    def pos():
        x = p.pos()
        print(x)

    pan.penup()
    pan.hideturtle()
    pan.goto(365.00,-350.00)


    screen.addshape("14.gif")
    screen.addshape("10.gif")
    screen.addshape("3.gif")
    screen.addshape("4.gif")
    screen.addshape("5.gif")
    screen.addshape("40.gif")
    screen.addshape("41.gif")
    screen.addshape("44.gif")
    screen.addshape("45.gif")
    screen.addshape("13.gif")
    screen.addshape("42.gif")
    screen.addshape("2.gif")
    screen.addshape("27.gif")
    screen.addshape("28.gif")
    screen.addshape("30.gif")
    screen.addshape("48.gif")
    screen.addshape("31.gif")
    screen.addshape("6.gif")
    screen.addshape("7.gif")
    screen.addshape("8.gif")
    screen.addshape("23.gif")
    screen.addshape("32.gif")
    screen.addshape("33.gif")
    screen.addshape("34.gif")
    screen.addshape("24.gif")
    screen.addshape("25.gif")
    screen.addshape("26.gif")
    screen.addshape("11.gif")
    screen.addshape("15.gif")
    screen.addshape("20.gif")
    screen.addshape("46.gif")
    screen.addshape("22.gif")
    screen.addshape("49.gif")


    w.penup()
    w.goto(-500,0)
    w.write("this game contains nudity and adult contents,\n no entry for under 18.\n do still want to procreed?",font=("Cascadia Mono",30,"bold"))
    w.goto(-100,-200)
    w.color("red")
    w.write("press  y",font=("Cascadia Mono",30,"bold"))
    w.color("black")

    def init():
        

        age = turtle.textinput("are you over 18 years old?","yes/no")

        if age == "yes":
            w.clear()
            wi.shape("15.gif")
            wi.hideturtle()
            w.speed(1000)
            w.goto(-500,100)
            w.write("HELP: \n read the instructions carefully \n and follow them to continue ",font=("Cascadia Mono",30,"bold"))
            time.sleep(3)
            w.clear()
            w.goto(-500,50)
            w.write("give all the input in lowercase only and that to \n without space and any other character.\n if you are in problamatic situation\n press 'x' to exit the game immediatly.",font=("Cascadia Mono",30,"bold"))
            time.sleep(5)
            w.clear()

            jj.speed(100000)
            jj.penup()
            jj.goto(-400,0)
            jj.shape("42.gif")
            jjspeech.hideturtle()
            jjspeech.penup()
            jjspeech.goto(-500,0)
            
            screen.setup(width=2424,height=1400)
            screen.screensize(canvheight=1400,canvwidth=2424)
            screen.bgcolor("white")
            screen.addshape("12.gif")
            screen.addshape("43.gif")
            screen.bgpic("46.gif")
            

            jjspeech.write("She must be whore! \n She had fucked a lot of people!",font=("castellar",30,"bold"))
            time.sleep(3)
            jjspeech.clear()
            jjspeech.write("Must see her nude in live even once in life!",font=("castellar",30,"bold"))
            time.sleep(3)
            jjspeech.clear()
            jjspeech.write("I think she in the library \n I shall go there!",font=("Cascadia Mono",30,"bold"))

            mia.shape("14.gif")
            mia.hideturtle()
            image.shape("12.gif")
            image.penup()
            image.goto(500,0)
            mia.penup()
            mia.goto(-400,300)
            mia.showturtle()
            miaspeech.penup()
            miaspeech.hideturtle()
            miaspeech.goto(-500,300)

            
            w.penup()
            w.hideturtle()
            w.goto(-800,-300)
            wi.goto(-400,-300)
            wi.showturtle()
            w.write("you are going to the library.",font=("castel1ar",30,"bold"))
            screen.bgpic("22.gif")


            miaspeech.write("I think I am the hottest woman in the world.\n do you agree with me?",font=("Cascadia Mono",16,"bold"))
            scarf = turtle.textinput("the hottest ","yes/no")

            if scarf == "yes":
                jjspeech.write("Yes you are the hottest and \n sexiest woman on eath",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                jjspeech.clear()
                miaspeech.clear()
                image.shape("43.gif")
                miaspeech.write("you knew about me very well, \n you are making me blush",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
            else:
                jjspeech.write("No you ugly piece of shit!",font=("Cascadia Mono",20,"bold"))
                image.shape('12.gif')
                miaspeech.write("you didn't knew me at all, \n I don't want you anymore",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                jjspeech.clear()
                scarf = turtle.textinput("hottest woman","yes/no")

            miaspeech.write("I am now wearing a 'black' coat \n its very hot here\n can you make me free?",font=("Cascadia Mono",20,"bold"))
            w.write("free mia by entering the coat's color",font=("Cascadia Mono",20,"bold"))
            color = turtle.textinput("color","enter colour of her coat")

            if color == "black":
                w.clear()
                jjspeech.write("Yes of course my mia",font=("Cascadia Mono",20,"bold"))
                image.shape("44.gif")
                time.sleep(2)
                image.shape("45.gif")
                miaspeech.clear()
                miaspeech.write("it is free now , can you make \n me even more free",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                jjspeech.clear()
            else:
                jjspeech.write("Sorry Mia I am color blind",font=("Cascadia Mono",20,"bold"))
                miaspeech.write("I will not fuck a color blind",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                jjspeech.clear()
                jjspeech.write("give me another chance mia",font=("Cascadia Mono",20,"bold"))
                image.shape("12.gif")
                w.write("are you grazy don't make mia angry\n enter the color correctly \n as per instructions",font=("Cascadia Mono",20,"bold"))
                time.sleep(2)
                w.clear()
                miaspeech.clear()
                jjspeech.clear()
                color = turtle.textinput("color","enter colour of her coat")
            
            miaspeech.write("This vest does not suit me \n would you buy me a new one?",font=("Cascadia Mono",20,"bold"))
            time.sleep(3)
            miaspeech.clear()
            miaspeech.write("If you buy me one, \n I will remove this!",font=("Cascadia Mono",20,"bold"))

            bra = turtle.textinput("this vest doesn't suit me!","yes/no")

            if bra =="yes":
                miaspeech.clear()
                jjspeech.write("I will buy you anything \n for you mia",font=("Cascadia Mono",20,"bold"))
                miaspeech.write("here my dear I'll remove \n it as said",font=("Cascadia Mono",20,"bold"))
                time.sleep(2)
                image.shape("4.gif")
                time.sleep(1)
                image.shape("3.gif")
                time.sleep(1)
                image.shape("5.gif")
                time.sleep(2)
                miaspeech.clear()
                jjspeech.clear()
            else:
                jjspeech.write("sorry mia I don't have \n that much money",font=("Cascadia Mono",20,"bold"))
                w.write("this poor should not play with mia ",font=("Cascadia Mono",20,"bold"))
                w.clear()
                w.write("this game will get closed in 5seconds" ,font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                w.clear()
                sys.exit()
                
            miaspeech.write("My breast size is '34' \n use it to buy me a bra too",font=("Cascadia Mono",20,"bold"))
            w.write("ENTER Mia's breast size to remove it",font=("Cascadia Mono",20,"bold"))
            time.sleep(3)
            w.clear()

            

            tits = turtle.textinput("bra measurement","enter the size of het breast in cm ")
            
            if tits == "34":
                miaspeech.clear()
                miaspeech.write("You have a good memeory power",font=("Cascadia Mono",20,"bold"))
                image.shape("4.gif")
                time.sleep(1)
                image.shape("40.gif")
                time.sleep(1)
                image.shape("41.gif")
                miaspeech.clear()
                
            else:
                image.shape("down.gif")
                miaspeech.write("won't you buy me one?")
                bra = turtle.textinput("bra measurement","enter the size of het breast in cm ")
                miaspeech.clear()
            
            w.write("You have sucessfully undressed her upperbody.\nlet's finish her lower parts",font=("Cascadia Mono",20,"bold")) 

            miaspeech.write("don't see me like that !\n I am feelng nervous \n I'll turn around",font=("Cascadia Mono",20,"bold"))
            time.sleep(3)
            miaspeech.clear()
            image.shape("2.gif")

            miaspeech.write("I usually don't like jeans pant\n couls you help me remove it?",font=("Cascadia Mono",20,"bold"))
            w.clear()
            w.write("move the pointer to mia's left buttock's top",font=("Cascadia Mono",20,"bold"))

            p.shape("30.gif")
            p.penup()
            pan.write("move here")

            def north():
                p.setheading(90)
                p.forward(5)
                p.speed(100)
                p.setheading(0)
            def south():
                p.setheading(270)
                p.forward(5)
                p.speed(100)
                p.setheading(0)
            def east():
                p.setheading(0)
                p.forward(5)
                p.speed(100)
                p.setheading(0)
            def west():
                p.setheading(180)
                p.forward(5)
                p.speed(100)
                p.setheading(0)

            turtle.onkeypress(north,"Up")
            turtle.onkeypress(south,"Down")
            turtle.onkeypress(east,"Right")
            turtle.onkeypress(west,"Left")

            turtle.listen()
            while True:
                screen.update()
                if p.distance(pan) < 100:
                    image.shape("27.gif")
                    time.sleep(1)
                    image.shape("28.gif")
                    miaspeech.clear()
                    w.clear()
                    miaspeech.write("Ahh! you touched there!\n I am feeling sexy now",font=("Cascadia Mono",20,"bold"))
                    time.sleep(3)
                    miaspeech.clear()
                    break
            p.hideturtle()
            pan.hideturtle()

            miaspeech.write("want to see something sexy?",font=("Cascadia Mono",20,"bold"))
            panty = turtle.textinput("want to see something cool?","yes/no")

            if panty =="yes":
                image.shape("48.gif")
                time.sleep(1)
                miaspeech.clear()
                miaspeech.write("As you wish, I wil remove it!",font=("Cascadia Mono",20,"bold"))
                image.shape("6.gif")
                time.sleep(1)
                image.shape("7.gif")
                time.sleep(1)
                image.shape("8.gif")
                jjspeech.write("You are erotic mia!",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                miaspeech.write("I am fully prepared to fuck you",font=("Cascadia Mono",20,"bold"))
                time.sleep(1)
                jjspeech.clear()
                jjspeech.write("I am waiting for it!",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)

            else:
                miaspeech.write("if that is all you want to see\n this had ended.",font=("Cascadia Mono",20,"bold"))
                w.write("this game is going to end in 3 seconds",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                sys.exit()

            miaspeech.clear()
            jjspeech.clear()
            miaspeech.write("Before you fuck me\n let me check your penis size",font=("Cascadia Mono",20,"bold"))
            image.shape("31.gif")
            miaspeech.clear()
            jjspeech.write("ok let's check what you want",font=("Cascadia Mono",20,"bold"))
            miaspeech.write("in this image,  there are three sizes given\n small or average or large\n what is your size?",font=("Cascadia Mono",20,"bold"))
            psize = turtle.textinput("peniis size","small or average or large")
            screen.addshape("9.gif")

            if psize =="average":
                miaspeech.clear()
                jjspeech.clear()
                miaspeech.write("Quite expected, you are \n eligible to fuck me!",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                miaspeech.write("Don't lie to me \n i will check now ",font=("Cascadia Mono",20,"bold"))
                jjspeech.write("Yes go ahead!",font=("Cascadia Mono",20,"bold"))
                w.write("One time when checking like this a guy fucked mia in mouth",font=("Cascadia Mono",20,"bold"))
                image.shape("9.gif")
                time.sleep(3)
                miaspeech.clear()
                jjspeech.clear()
                miaspeech.write("I got mood after seeing yours! \n see me fucking myself",font=("Cascadia Mono",20,"bold"))
                jjspeech.write("Shall I help you mia?",font=("Cascadia Mono",20,"bold"))

            elif psize == "large":
                miaspeech.clear()
                jjspeech.clear()
                miaspeech.write("I am shocked, you are \n eligible to fuck me!",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                miaspeech.write("Don't lie to me \n i will check now ",font=("Cascadia Mono",20,"bold"))
                jjspeech.write("Yes go ahead!")
                w.write("One time when checking like this a guy fucked mia in mouth",font=("Cascadia Mono",20,"bold"))
                image.shape("9.gif")
                time.sleep(3)
                miaspeech.clear()
                jjspeech.clear()
                miaspeech.write("I got mood after seeing yours! \n see me fucking myself",font=("Cascadia Mono",20,"bold"))
                jjspeech.write("Shall I help you mia?",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                miaspeech.write("you naughty!",font=("Cascadia Mono",20,"bold"))
                

            else:
                miaspeech.clear()
                jjspeech.clear()
                miaspeech.write("Just a time waste!\n you little kid! get lost!",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                w.write("this game is going to end in 3 seconds",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                sys.exit()


            w.clear()
            miaspeech.clear()
            jjspeech.clear()
            mia.hideturtle()
            screen.bgpic(picname='nopic')
            p.hideturtle()
            jj.hideturtle()
            pan.hideturtle()
            image.hideturtle()
            miaspeech.hideturtle()
            jjspeech.hideturtle()
            w.hideturtle()
            wi.hideturtle()

            scoreboard = turtle.Turtle()

            w.write("collect the falling objects to make mia happpy!",font=("Cascadia Mono",20,"bold"))
            time.sleep(5)
            w.clear()
            scoreboard.penup()
            scoreboard.goto(0,300)
            score = 0

            screen.bgpic("47.gif")
            basket.penup()

            turtle.title("Screen experiment")

            turtle.setup(width = 810, height=847, startx =0,starty=0)
            turtle.screensize(canvwidth = 800,canvheight= 800)
            basket.goto(0,-380)
            basket.shape("21.gif")

            object1.penup()
            object1.goto(-380,380)
            object1.shape("20.gif")

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

                if score>9:
                    scoreboard.clear()
                    scoreboard.write("you win!",font=("castellar",24,"bold"))
                    break

            p.showturtle()
            jj.showturtle()
            mia.showturtle()
            image.showturtle()
            screen.bgpic("23.gif")
            w.showturtle()

            miaspeech.write("let me show you something special",font=("Cascadia Mono",20,"bold"))
            jjspeech.write("I am waiting for it mia",font=("Cascadia Mono",20,"bold"))

            image.shape("32.gif")
            time.sleep(2)
            image.shape("33.gif")
            time.sleep(2)
            image.shape("34.gif")
            time.sleep(2)

            w.clear()
            miaspeech.clear()
            jjspeech.clear()
            mia.hideturtle()
            screen.bgpic(picname='nopic')
            p.hideturtle()
            jj.hideturtle()
            pan.hideturtle()
            image.hideturtle()
            miaspeech.hideturtle()
            jjspeech.hideturtle()
            w.hideturtle()
            wi.hideturtle()

            screen.screensize(canvwidth=1424,canvheight=800)
            screen.setup(width=1424,height=800)
            screen.title("locator")
            ship = turtle.Turtle()
            planet = turtle.Turtle()
            scoreboard = turtle.Turtle()
            ship.speed(1000)
            screen.addshape("39.gif")
            screen.addshape("38.gif")
            screen.addshape("35.gif")
            screen.addshape("36.gif")
            screen.addshape("37.gif")
            screen.addshape("29.gif")


            score = 0
            scoreboard.hideturtle()
            scoreboard.penup()
            scoreboard.goto(0,200)
            scoreboard.color("green")

            planet.speed(1)
            planet.shape("29.gif")

            screen.bgpic("39.gif")
            ship.shape("38.gif")
            ship.penup()

            def move():
                def up():
                    ship.shape("38.gif")
                    ship.seth(90)
                    ship.fd(10)
                    ship.seth(0)

                def down():
                    ship.shape("35.gif")
                    ship.seth(270)
                    ship.fd(10)
                    ship.seth(0)

                def right():
                    ship.shape("rocket_right.gif")
                    ship.fd(10)

                def left():
                    ship.shape("36.gif")
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

            if score > 10:
                p.showturtle()
                jj.showturtle()
                mia.showturtle()
                image.showturtle()
                screen.bgpic("23.gif")
                w.showturtle()

                jjspeech.clear()
                miaspeech.clear()
                jjspeech.write("You are gorgeous Mia!",font=("Cascadia Mono",20,"bold"))
                image.shape("24.gif")
                time.sleep(1)
                image.shape("25.gif")
                time.sleep(1)
                image.shape("26.gif")
                time.sleep(1)
                image.shape("11.gif")
                time.sleep(1)
                jjspeech.clear()

        else:
            w.clear()
            mia.shape("13.gif")

            jj.penup()
            jj.goto(-400,0)
            jj.shape("10.gif")

            image.penup()
            image.goto(400,0)
            image.shape("10.gif")

            w.penup()
            w.speed(1000)
            w.goto(-500,-300)
            w.speed(1)
            w.write("you should not be here my child",font=("Cascadia Mono",20,"bold"))
            w.setheading(270)
            w.forward(25)
            w.setheading(0)
            w.write("you are blessed by the lord. praise the lord and go away!",font=("Cascadia Mono",20,"bold"))
            w.hideturtle()
            time.sleep(2)
            sys.exit()



    turtle.onkeypress(pos,"p")
    turtle.onkeypress(init,"y")
    turtle.onkeypress(emergency_exit,"x")  
    turtle.listen() 

else:
    turtle.write("invalid license key",font=("Cascadia Mono",20,"bold"))
    time.sleep(4)
    sys.exit()


turtle.done()