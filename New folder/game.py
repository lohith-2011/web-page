import turtle
import time
import sys

password = turtle.textinput("password","enter the license key ")

if password == "mia2024":

    jj = turtle.Turtle()
    jjspeech = turtle.Turtle()
    mia = turtle.Turtle()
    miaspeech = turtle.Turtle()
    w = turtle.Turtle()
    image = turtle.Turtle()
    screen = turtle.Screen()
    p = turtle.Turtle()
    pan = turtle.Turtle()

    def pos():
        x = p.pos()
        print(x)

    pan.penup()
    pan.hideturtle()
    pan.goto(365.00,-350.00)


    screen.addshape("jesus.gif")
    screen.addshape("cross.gif")
    screen.addshape("bra1.gif")
    screen.addshape("bra2.gif")
    screen.addshape("bra3.gif")
    screen.addshape("tits1.gif")
    screen.addshape("tits2.gif")
    screen.addshape("vest1.gif")
    screen.addshape("vest2.gif")
    screen.addshape("kilafat.gif")
    screen.addshape("unknown.gif")
    screen.addshape("back.gif")
    screen.addshape("panty1.gif")
    screen.addshape("panty2.gif")
    screen.addshape("pointer.gif")
    screen.addshape("zoom.gif")
    screen.addshape("pp.gif")
    screen.addshape("butt0.gif")
    screen.addshape("butt1.gif")
    screen.addshape("butt2.gif")
    screen.addshape("library-background.gif")
    screen.addshape("pussy0.gif")
    screen.addshape("pussy1.gif")
    screen.addshape("pussy2.gif")
    screen.addshape("mast0.gif")
    screen.addshape("mast1.gif")
    screen.addshape("mast2.gif")
    screen.addshape("final.gif")


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
            screen.setup(width=800,height=800)
            screen.bgcolor("white")
            screen.addshape("full.gif")
            screen.addshape("up.gif")
            screen.bgpic("library-background.gif")
            
            mia.shape("kilafat.gif")
            mia.hideturtle()
            image.shape("full.gif")
            image.penup()
            image.goto(500,0)
            mia.penup()
            mia.goto(-400,300)
            mia.showturtle()
            miaspeech.penup()
            miaspeech.hideturtle()
            miaspeech.goto(-500,300)

            jj.speed(100000)
            jj.penup()
            jj.goto(-400,0)
            jj.shape("unknown.gif")
            jjspeech.hideturtle()
            jjspeech.penup()
            jjspeech.goto(-500,0)

            w.hideturtle()
            w.penup()
            w.goto(-800,-300)

            miaspeech.write("I think I am the hottest woman in the world.\n do you agree with me?",font=("Cascadia Mono",16,"bold"))
            scarf = turtle.textinput("the hottest ","yes/no")

            if scarf == "yes":
                jjspeech.write("Yes you are the hottest and \n sexiest woman on eath",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                jjspeech.clear()
                miaspeech.clear()
                image.shape("up.gif")
                miaspeech.write("you knew about me very well, \n you are making me blush",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
            else:
                jjspeech.write("No you ugly piece of shit!",font=("Cascadia Mono",20,"bold"))
                image.shape('full.gif')
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
                image.shape("vest1.gif")
                time.sleep(2)
                image.shape("vest2.gif")
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
                image.shape("full.gif")
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
                image.shape("bra1.gif")
                time.sleep(1)
                image.shape("bra3.gif")
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
                image.shape("bra2.gif")
                time.sleep(1)
                image.shape("tits1.gif")
                time.sleep(1)
                image.shape("tits2.gif")
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
            image.shape("back.gif")

            miaspeech.write("I usually don't like jeans pant\n couls you help me remove it?",font=("Cascadia Mono",20,"bold"))
            w.clear()
            w.write("move the pointer to mia's left buttock's top",font=("Cascadia Mono",20,"bold"))

            p.shape("pointer.gif")
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
                    image.shape("panty1.gif")
                    time.sleep(1)
                    image.shape("panty2.gif")
                    miaspeech.clear()
                    w.clear()
                    miaspeech.write("Ahh! you touched there!\n I am feeling sexy now",font=("Cascadia Mono",20,"bold"))
                    time.sleep(3)
                    miaspeech.clear()
                    break

            
            panty = turtle.textinput("want to see something cool?","yes/no")

            if panty =="yes":
                image.shape("zoom.gif")
                time.sleep(1)
                miaspeech.write("As you wish, I wil remove it!",font=("Cascadia Mono",20,"bold"))
                image.shape("butt0.gif")
                time.sleep(1)
                image.shape("butt1.gif")
                time.sleep(1)
                image.shape("butt2.gif")
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
            image.shape("pp.gif")
            miaspeech.clear()
            jjspeech.write("ok let's check what you want",font=("Cascadia Mono",20,"bold"))
            miaspeech.write("in this image, \n there are three sizes given\n small or average or large\n what is your size?",font=("Cascadia Mono",20,"bold"))
            psize = turtle.textinput("peniis size","small or average or large")
            screen.addshape("check.gif")

            if psize =="average":
                miaspeech.clear()
                jjspeech.clear()
                miaspeech.write("Quite expected, you are \n eligible to fuck me!",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                miaspeech.write("Don't lie to me \n i will check now ",font=("Cascadia Mono",20,"bold"))
                jjspeech.write("Yes go ahead!",font=("Cascadia Mono",20,"bold"))
                w.write("One time when checking like this a guy fucked mia in mouth",font=("Cascadia Mono",20,"bold"))
                image.shape("check.gif")
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
                image.shape("check.gif")
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
                miaspeech.write("Just a time waste!\n you kutty kunjan! get lost!",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                miaspeech.clear()
                w.write("this game is going to end in 3 seconds",font=("Cascadia Mono",20,"bold"))
                time.sleep(3)
                sys.exit()

            miaspeech.clear()
            jjspeech.clear()
            miaspeech.write("let me show you something special",font=("Cascadia Mono",20,"bold"))
            jjspeech.write("I am waiting for it mia",font=("Cascadia Mono",20,"bold"))

            image.shape("pussy0.gif")
            time.sleep(2)
            image.shape("pussy1.gif")
            time.sleep(2)
            image.shape("pussy2.gif")
            time.sleep(2)

            jjspeech.clear()
            miaspeech.clear()
            jjspeech.write("You are gorgeous Mia!",font=("Cascadia Mono",20,"bold"))
            image.shape("mast0.gif")
            time.sleep(1)
            image.shape("mast1.gif")
            time.sleep(1)
            image.shape("mast1.gif")
            time.sleep(1)
            image.shape("final.gif")
            time.sleep(1)
            jjspeech.clear()

        else:
            w.clear()
            mia.shape("jesus.gif")

            jj.penup()
            jj.goto(-400,0)
            jj.shape("cross.gif")

            image.penup()
            image.goto(400,0)
            image.shape("cross.gif")

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

    def emergency_exit():
        sys.exit()

    turtle.onkeypress(pos,"p")
    turtle.onkeypress(init,"y")  
    turtle.onkeypress(emergency_exit,"e")
    turtle.listen() 

else:
    turtle.write("invalid license key",font=("Cascadia Mono",20,"bold"))
    time.sleep(4)
    sys.exit()

turtle.done()