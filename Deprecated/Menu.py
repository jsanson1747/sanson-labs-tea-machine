########################################
# Menu GUI For Sanson Labs Tea Machine #
########################################

import turtle
import tkinter as tk
import math

def drawBox(turt, x, y, h, w, thickness):
    turt.penup()
    turt.pensize(thickness)
    turt.goto(x, y)
    turt.seth(-90)
    turt.pendown()
    for i in range(2):
        turt.forward(h)
        turt.left(90)
        turt.forward(w)
        turt.left(90)
    turt.penup()

def drawEllipse(turt, initX, initY, A, B, thickness, half = "full"):
    #                                                  #
    #    ((x^2)/A^2) + ((y^2)/B^2) = 1                 #
    #                                                  #
    #    x = math.sqrt(A**2 - ((A**2*y**2)/(B**2)))    #
    #                                                  #
    yPos = initY - B
    x = initX
    turt.penup()
    turt.pensize(thickness)
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
    
    
    
    


    

def Menu(screen):
    #Init Turtles
    artist = turtle.RawTurtle(screen)
    artist.penup()
    artist.ht()

    


    #drawEllipse(artist, 0, 0, 200, 100, 5)
    
    drawBox(artist, -360, 200, 300, 200, 4)
    
    #Draw Tea Mug
    drawEllipse(artist, -260, 100, 30, 10, 4)
    artist.penup()
    artist.goto(-290, 100)
    artist.pendown()
    artist.seth(-90)
    artist.forward(50)
    drawEllipse(artist, -260, 50, 30, 10, 4, "bot")
    artist.penup()
    artist.goto(-230, 50)
    artist.pendown()
    artist.seth(90)
    artist.forward(50)
    drawEllipse(artist, -230, 72, 16, 16, 6, "right")
    screen.update()
    
    
    
        
    


if __name__ == "__main__":
    GUI = tk.Tk()
    GUI.overrideredirect(1)
    canvas = tk.Canvas(master = GUI, width = 800, height = 480)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")
    #screen.tracer(10)
    
    Menu(screen)
    

