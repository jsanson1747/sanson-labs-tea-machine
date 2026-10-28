####################
# Sanson Labs Logo #
####################

import turtle
from utils import playWavSound
import time
from menudoodle import MenuDoodle

def logo(screen):
    def makeTurtles():
        a = turtle.RawTurtle(screen)
        a.penup()
        a.hideturtle()
        
        b = turtle.RawTurtle(screen)
        b.penup()
        b.hideturtle()
        b.shape("triangle")
        b.color("grey")
        b.turtlesize(4.5, 4.5, 1)
        
        c = turtle.RawTurtle(screen)
        c.penup()
        c.hideturtle()
        c.shape("triangle")
        c.color("grey")
        c.turtlesize(4.5, 4.5, 1)
        
        d = turtle.RawTurtle(screen)
        d.penup()
        d.hideturtle()
        d.shape("triangle")
        d.color("grey")
        d.turtlesize(4.5, 4.5, 1)
        
        e = turtle.RawTurtle(screen)
        e.penup()
        e.hideturtle()
        e.shape("triangle")
        e.color("grey")
        e.turtlesize(4.5, 4.5, 1)
        
        f = turtle.RawTurtle(screen)
        f.penup()
        f.hideturtle()
        f.shape("triangle")
        f.color("grey")
        f.turtlesize(4.5, 4.5, 1)
        
        g = turtle.RawTurtle(screen)
        g.penup()
        g.hideturtle()
        g.shape("triangle")
        g.color("grey")
        g.turtlesize(4.5, 4.5, 1)

        h = turtle.RawTurtle(screen)
        h.penup()
        h.hideturtle()
        h.fillcolor("black")
        h.shape("circle")

        I = turtle.RawTurtle(screen)
        I.penup()
        I.hideturtle()
        I.fillcolor("lime")
        I.shape("circle")

        j = turtle.RawTurtle(screen)
        j.penup()
        j.hideturtle()

        k = turtle.RawTurtle(screen)
        k.penup()
        k.hideturtle()
        
        
        return a, b, c, d, e, f, g, h, I, j, k

    def Hex(turt,angle,color):
        screen.tracer(40)
        turt.pencolor(color)
        turt.setheading(angle)
        turt.pensize(3)
        for j in range(0, 101):
            turt.begin_fill()
            for i in range(6):
                turt.forward(j)
                turt.right(360 / 6)
            turt.end_fill()
        
    def drawHex(angle):
        Black_Hex.penup()
        Black_Hex.goto(-50, 85)
        Black_Hex.pendown()
        Hex(Black_Hex,angle,"black")
        screen.update()

    def initSecondaryTurtStage(a, b, c, d, e, f):
        dist = 400
        
        a.goto(0, 0)
        a.left(60)
        a.forward(dist)
        a.right(180)

        b.goto(0,0)
        b.forward(dist)
        b.right(180)

        c.goto(0,0)
        c.right(60)
        c. forward(dist)
        c.right(180)

        d.goto(0,0)
        d.right(120)
        d.forward(dist)
        d.right(180)

        e.goto(0,0)
        e.right(180)
        e.forward(dist)
        e.right(180)

        f.goto(0,0)
        f.right(240)
        f.forward(dist)
        f.right(180)
        
        screen.update()

        return dist

    def AssembleGreyHex(dist):
        Tri1.showturtle()
        Tri2.showturtle()
        Tri3.showturtle()
        Tri4.showturtle()
        Tri5.showturtle()
        Tri6.showturtle()
        
        dist -= 55
        screen.tracer(40)

        for i in range(0, (dist//2) - 59):
            Tri1.forward(3)
            Tri2.forward(3)
            Tri3.forward(3)
            Tri4.forward(3)
            Tri5.forward(3)
            Tri6.forward(3)

    def drawCircle(turt, limit):
        screen.tracer(3)
        turt.showturtle()
        size = 0.1
        while size <= limit:
            turt.turtlesize(size, size, 0)
            size += 0.1
        
    def printText(turt, text, x , y, color, limitSize):
        screen.tracer(30)
        size = 1
        turt.penup()
        turt.goto(x,y)
        turt.color(color)
        while size <= limitSize:
            turt.clear()
            turt.write(text, None, "center", font = ("Agency FB", size, "bold"))
            size += 1
        screen.update()

    def moveToCorner():
        image = "LogoForShrinkage.gif"
        wn.register_shape(image)

        IMAGE = turtle.Turtle(shape = image)
        IMAGE.penup()
        
        screen.update()
        Black_Hex.clear()
        Tri1.clear()
        Tri2.clear()
        Tri3.clear()
        Tri4.clear()
        Tri5.clear()
        Tri6.clear()
        Outline.clear()
        Circle.clear()
        Top_Text.clear()
        Bottom_Text.clear()
        screen.update()

        screen.tracer(1)
        IMAGE.goto(270, 220)
        screen.update()

    def genGeorgeCircle():
        drawCircle(Outline, 9)
        drawCircle(Circle, 8.5)

    
    ((Black_Hex, Tri1, Tri2, Tri3, Tri4, Tri5, Tri6, Outline, Circle, Top_Text, Bottom_Text)) = makeTurtles()
    drawHex(0)
    dist = initSecondaryTurtStage(Tri1, Tri2, Tri3, Tri4, Tri5, Tri6)
    AssembleGreyHex(dist)

    drawCircle(Outline, 7.4)
    drawCircle(Circle, 6.8)
    
    
    Tri1.stamp()
    Tri2.stamp()
    Tri3.stamp()
    Tri4.stamp()
    Tri5.stamp()
    Tri6.stamp()

    Tri1.hideturtle()
    Tri2.hideturtle()
    Tri3.hideturtle()
    Tri4.hideturtle()
    Tri5.hideturtle()
    Tri6.hideturtle()

    
    Outline.stamp()
    Circle.stamp()
    Outline.hideturtle()
    Circle.hideturtle()

    printText(Top_Text, "SANSON", 1, -4, "black", 28)
    printText(Bottom_Text, "LABS", 1, -49, "black", 28)
    screen.update()

    playWavSound("./sounds/GeorgeBootUp.wav")
    time.sleep(1.5)
    
    Black_Hex.clear()
    Tri1.clear()
    Tri2.clear()
    Tri3.clear()
    Tri4.clear()
    Tri5.clear()
    Tri6.clear()
    Outline.clear()
    Circle.clear()
    Top_Text.clear()
    Bottom_Text.clear()
    screen.update()

if __name__ == "__main__":
    doodler =  MenuDoodle()
    screen = doodler.getScreen()
    
    logo(screen)