import turtle
import math


def DE(turt, initX, initY, A, B, thickness = 2, half = "full"):
    yPos = initY - B
    x = initX
    turt.pensize(thickness)
    turt.penup()
    turt.goto(initX, yPos)
    turt.pendown()

    while yPos < initY - B + (2 * B):
        if half == "top":
            if yPos < initY:
                turt.penup()
            else:
                turt.pendown()
        if half == "bot":
            if yPos > initY:
                turt.penup()
            else:
                turt.pendown()
        if half == "left":
            if x >= initX:
                turt.penup()
            else:
                turt.pendown()
        if half == "right":
            if x < initX:
                turt.penup()
            else:
                turt.pendown()
        x = math.sqrt(A ** 2 - ((A ** 2 * (yPos - initY) ** 2)/(B ** 2))) + initX
        turt.goto(x, yPos)
        yPos += 0.5
        
    while yPos >= initY - B:
        if half == "top":
            if yPos < initY:
                turt.penup()
            else:
                turt.pendown()
        if half == "bot":
            if yPos > initY:
                turt.penup()
            else:
                turt.pendown()
        if half == "left":
            if x > initX:
                turt.penup()
            else:
                turt.pendown()
        if half == "right":
            if x <= initX:
                turt.penup()
            else:
                turt.pendown()
        x = -1 * (math.sqrt(A ** 2 - ((A ** 2 * (yPos - initY) ** 2)/(B ** 2)))) + initX
        turt.goto(x, yPos)
        yPos -= 0.5
    screen.update()
    

artist = turtle.Turtle()
artist.ht()
'''
DE(artist, 0, 0, 200, 100, 4)
artist.seth(20)
artist.color("blue")
DE(artist, 0, 0, 200, 100, 4)
'''
screen = turtle.Screen()
screen.tracer(100)

for i in range(0,100):
    if i % 7 == 0:
        artist.color("black")
        #DE(artist, 0, -1, 200, 100, 4)
        #screen.update()
    else:
        artist.color("grey")
    DE(artist, 0, i, 200, 100, 4, "bot")
    artist.color("dark green")
    DE(artist, 0, i, 200, 100, 4, "top")
    screen.update()

artist.color("black")
DE(artist, 0, 101, 200, 100, 4)
screen.update()

    
