##################################
# GUI for Sanson Labs TeaMachine #
##################################

#Import Dependencies
import turtle
from TurtleLetterUtils import fillLetter
import time
import subprocess
from menudoodle import MenuDoodle

#########################################################

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

    subprocess.run(["aplay", "./GeorgeBootUp.wav"], shell=False)
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


#########################################################

def T(text):
    text.penup()
    text.goto(-300, 130)
    text.pendown()
    text.seth(20)
    text.forward(200)
    text.seth(270)
    text.forward(30)
    text.seth(200)
    text.forward(85)
    text.seth(270)
    text.forward(200)
    text.seth(200)
    text.forward(30)
    text.seth(90)
    text.forward(200)
    text.seth(200)
    text.forward(85)
    text.seth(90)
    text.forward(30)
    text.penup()

def e(x, y, scale, text):
    text.goto(x, y)
    text.pendown()
    text.seth(90)
    text.forward(100 * scale)
    text.seth(20)
    text.forward(70 * scale)
    text.seth(270)
    text.forward(20 * scale)
    text.seth(200)
    text.forward(50 * scale)
    text.seth(270)
    text.forward(20 * scale)
    text.seth(20)
    text.forward(35 * scale)
    text.seth(270)
    text.forward(20 * scale)
    text.seth(200)
    text.forward(35 * scale)
    text.seth(270)
    text.forward(20 * scale)
    text.seth(20)
    text.forward(50 * scale)
    text.seth(270)
    text.forward(20 * scale)
    text.seth(200)
    text.forward(70 * scale)
    text.penup()

def a(x, y, scale, text):
    text.goto(x, y)
    text.seth(20)
    text.pendown()
    text.seth(90)
    text.forward(100 * scale)
    text.seth(20)
    text.forward(70 * scale)
    text.seth(270)
    text.forward(100 * scale)
    text.seth(200)
    text.forward(20 * scale)
    text.seth(90)
    text.forward(20 * scale)
    text.penup()
    text.forward(20 * scale)
    text.pendown()
    text.forward(40 * scale)
    text.seth(200)
    text.forward(30 * scale)
    text.seth(270)
    text.forward(40 * scale)
    text.seth(20)
    text.forward(30 * scale)
    text.seth(270)
    text.penup()
    text.forward(20 * scale)
    text.seth(200)
    text.pendown()
    text.forward(30 * scale)
    text.seth(270)
    text.forward(20 * scale)
    text.seth(200)
    text.forward(20 * scale)
    text.penup()

def M(text):
    text.goto(-137, -179)
    text.seth(20)
    text.forward(10)
    text.pendown()
    text.seth(90)
    text.forward(130)
    text.seth(-55)
    text.forward(80)
    text.seth(67.5)
    text.forward(103)
    text.seth(270)
    text.forward(130)
    text.seth(200)
    text.forward(20)
    text.seth(90)
    text.forward(45)
    text.seth(247.5)
    text.forward(44)
    text.seth(125)
    text.forward(55)
    text.seth(270)
    text.forward(67)
    text.seth(200)
    text.forward(20)
    text.penup()

def c(text):
    text.showturtle()
    text.penup()
    text.goto(15.02, -125.09)
    text.seth(20)
    text.forward(8)
    text.pendown()
    text.seth(90)
    text.forward(75)
    text.seth(20)
    text.forward(52.5)
    text.seth(270)
    text.forward(15)
    text.seth(200)
    text.forward(37.5)
    text.seth(270)
    text.forward(45)
    text.seth(20)
    text.forward(37.5)
    text.seth(270)
    text.forward(15)
    text.seth(200)
    text.forward(52.5)
    text.penup()

def h(text):
    text.seth(20)
    text.forward(61.5)
    text.pendown()
    text.seth(90)
    text.forward(75)
    text.seth(20)
    text.forward(15)
    text.seth(270)
    text.forward(30)
    text.seth(20)
    text.forward(22.5)
    text.seth(90)
    text.forward(30)
    text.seth(20)
    text.forward(15)
    text.seth(270)
    text.forward(75)
    text.seth(200)
    text.forward(15)
    text.seth(90)
    text.forward(30)
    text.seth(200)
    text.forward(22.5)
    text.seth(270)
    text.forward(30)
    text.seth(200)
    text.forward(15)
    text.penup()

def i(text):
    text.seth(20)
    text.forward(61.5)
    text.pendown()
    text.seth(90)
    text.forward(15)
    text.seth(20)
    text.forward(18.75)
    text.seth(90)
    text.forward(45)
    text.seth(200)
    text.forward(18.75)
    text.seth(90)
    text.forward(15)
    text.seth(20)
    text.forward(52.5)
    text.seth(270)
    text.forward(15)
    text.seth(200)
    text.forward(18.75)
    text.seth(270)
    text.forward(45)
    text.seth(20)
    text.forward(18.75)
    text.seth(270)
    text.forward(15)
    text.seth(200)
    text.forward(52.5)
    text.penup()

def n(text):
    text.seth(20)
    text.forward(61.5)
    text.pendown()
    text.seth(90)
    text.forward(75)
    text.seth(20)
    text.forward(20)
    text.seth(-67)
    text.forward(54.28)
    text.seth(90)
    text.forward(57)
    text.seth(20)
    text.forward(15)
    text.seth(200)
    text.hideturtle()
    text.seth(270)
    text.forward(75)
    text.seth(200)
    text.forward(20)
    text.seth(114)
    text.forward(54.28)
    text.seth(270)
    text.forward(57)
    text.seth(200)
    text.forward(15)
    text.penup()
    text.seth(20)
    text.forward(68.5)

def main():

    doodler =  MenuDoodle()
    screen = doodler.getScreen()

    logo(screen)

    text = turtle.RawTurtle(screen)
    text.hideturtle()
    screen.tracer(30)
    text.speed("fastest")

    time.sleep(0.1)
    screen.bgcolor("light gray")
    time.sleep(0.1)
    screen.bgcolor("gray")
    time.sleep(0.1)
  
     
    text.pensize(56) #50
    text.pencolor("lime")
    #Backbackground

    subprocess.run(["aplay", "./Woosh.wav", "--nonblock"], shell=False)

    T(text)
    e(-182.54, -57.25, 1, text)
    a(-107.36, -29.89, 1, text)

    M(text)
    a(-33.84,-142.87, 0.75, text)
    c(text)
    h(text)
    i(text)
    n(text)
    e(259.41,-36.20, 0.75, text)

    
    text.pensize(42) #36
    text.pencolor("black")
    #Background

    T(text)
    e(-182.54, -57.25, 1, text)
    a(-107.36, -29.89, 1, text)

    M(text)
    a(-33.84,-142.87, 0.75, text)
    c(text)
    h(text)
    i(text)
    n(text)
    e(259.41,-36.20, 0.75, text)


    text.pensize(4)
    text.pencolor("white")

    #Text

    T(text)
    e(-182.54, -57.25, 1, text)
    a(-107.36, -29.89, 1, text)

    M(text)
    a(-33.84,-142.87, 0.75, text)
    c(text)
    h(text)
    i(text)
    n(text)
    e(259.41,-36.20, 0.75, text)

    fillTurt = turtle.RawTurtle(screen)
    #Fill T
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 85, vertDist = 30, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -300, y = 130, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 30, vertDist = 230, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 85, vertDist = 30, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    #Fill E
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 20, vertDist = 100, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -182.54, y = 42.75, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 35, vertDist = 100, gap = 20, numGaps = 2, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 15, vertDist = 100, gap = 60, numGaps = 1, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    #Fill A
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 20, vertDist = 100, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -107.54, y = 70.11, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 30, vertDist = 100, gap = 'n/a', numGaps = 'n/a', gapList = [20, 40, 20, 20, 1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 20, vertDist = 100, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill M
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, screen, horizDist = 20, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [-55, 20], x = [-127.60, -127.60], y = [-45.58, -175.58], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, screen, horizDist = 55.7, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [-55.5, -54.5], x = [upperTurtX - 1, lowerTurtX - 1], y = [upperTurtY, lowerTurtY + 67], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, screen, horizDist = 44, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [67.5, 67.5], x = [upperTurtX + 5, lowerTurtX], y = [upperTurtY, lowerTurtY], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, screen, horizDist = 20, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [67.5, 20], x = [upperTurtX + 1, lowerTurtX], y = [upperTurtY + 1, lowerTurtY - 45], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, screen, horizDist = 20, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [67.5, 20], x = [upperTurtX + 1, -60.45], y = [upperTurtY, -151.68], color = "white", size = 4)

    #Fill A
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -33.84, y = -67.87, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 26, vertDist = 75, gap = 'n/a', numGaps = 'n/a', gapList = [15, 30, 15, 15, 1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill C
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 22.54, y = -47.35, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 39.5, vertDist = 75, gap = 45, numGaps = 1, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill H
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 80.33, y = -26.32, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 24.5, vertDist = 75, gap = "n/a", numGaps = "n/a", gapList = [30, 15, 30, -1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill I
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 20, vertDist = 75, gap = "n/a", numGaps = "n/a", gapList = [15, 45, 15, 1], slope = 20, x = 138.12, y = -5.29, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 15, vertDist = 75, gap = "n/a", numGaps = "n/a", gapList = [15, 45, 15, 1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill N
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 195.91, y = 15.75, color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, screen, horizDist = 50, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [-67, -67], x = [xPos + 3, xPos + 3], y = [19.75, 0.75], color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 235.91, y = 29.62, color = "white", size = 4)

    #Fill E
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 259.41, y = 38.8, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 26.25, vertDist = 75, gap = 15, numGaps = 2, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, screen, horizDist = 11.25, vertDist = 75, gap = 45, numGaps = 1, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)


    screen.update()

    time.sleep(3)
    screen.clear()
    screen.tracer(100)

    screen.bgcolor("light gray")

    #####################################################################################

    playsound("Sanson Labs Tea Machine Deep AI British Voice.wav", block=False)

    #Generate Menu Interface
    lineDoodler = turtle.RawTurtle(screen)
    lineDoodler.hideturtle()
    lineDoodler.pencolor("black")
    lineDoodler.pensize(4)

    #Generate Box
    menuFrame = doodler.Box(780, 456, -390, 228, fill=False, fillColor="black", outline=True, outlineColor="gray", outlineWeight=10)
    menuFrame.draw()
    imageFrame = doodler.Box(200, 250, -360, 200, fill=True, fillColor="white", outline=True, outlineColor="black", outlineWeight=4)
    imageFrame.draw()

    teaMugYShifter = 0

    #Generate Tea Mug
    cupBox = doodler.Box(60, 50, -290, 100 + teaMugYShifter, fill=True, fillColor="gray", outline=False, outlineColor="black", outlineWeight=4)
    cupBox.draw()
    mugBottomFill = doodler.Ellipse(-260, 50 + teaMugYShifter, 30, 10, fill=True, color="grey", outlineWeight=4)
    mugBottomFill.draw()
    mugOpening = doodler.Ellipse(-260, 100 + teaMugYShifter, 30, 10, outlineWeight=4)
    mugOpening.draw()
    tea = doodler.Ellipse(-260, 100 + teaMugYShifter, 26, 6, fill=True, color="brown", outlineWeight=4)
    tea.draw()
    lineDoodler.penup()
    lineDoodler.goto(-290, 100 + teaMugYShifter)
    lineDoodler.pendown()
    lineDoodler.seth(-90)
    lineDoodler.forward(50)
    mugBottom = doodler.Ellipse(-260, 50 + teaMugYShifter, 30, 10, fill=False, color="Black", half="bottom", outlineWeight=4)
    mugBottom.draw()
    lineDoodler.penup()
    lineDoodler.goto(-230, 50 + teaMugYShifter)
    lineDoodler.pendown()
    lineDoodler.seth(90)
    lineDoodler.forward(50)
    mugHandle = doodler.Ellipse(-230, 72 + teaMugYShifter, 16, 16, fill=False, color="Black", half="right", outlineWeight=6)
    mugHandle.draw()
    screen.update()
    
    #Define Tea Attributes
    global steepTime
    global numSugars
    global numCreams

    steepTime = 3 #Default steep time
    numSugars = 0 #Default number of sugars
    numCreams = 0 #Default number of creams

    #Define Button Functions
    def addSugar():
        global numSugars
        if numSugars < 10:
            numSugars += 1
            SugarDisplay.setText(numSugars)
            SugarDisplay.print()

    def removeSugar():
        global numSugars
        if numSugars > 0:
            numSugars -= 1
            SugarDisplay.setText(numSugars)
            SugarDisplay.print()

    def addCreams():
        global numCreams
        if numCreams < 10:
            numCreams += 1
            CreamDisplay.setText(numCreams)
            CreamDisplay.print()
        if numCreams == 1:
            tea = doodler.Ellipse(-260, 100 + teaMugYShifter, 26, 6, fill=True, color="tan", outlineWeight=4)
            screen.tracer(100)
            tea.draw()
            screen.tracer(1)
            screen.update()

    def removeCreams():
        global numCreams
        if numCreams > 0:
            numCreams -= 1
            CreamDisplay.setText(numCreams)
            CreamDisplay.print()
        if numCreams == 0:
            tea = doodler.Ellipse(-260, 100 + teaMugYShifter, 26, 6, fill=True, color="brown", outlineWeight=4)
            screen.tracer(100)
            tea.draw()
            screen.tracer(1)
            screen.update()

    def addTime():
        global steepTime
        if steepTime < 10:
            steepTime += 1
            steepTimeDisplay.setText(str(steepTime) + " min")
            steepTimeDisplay.print()

    def removeTime():
        global steepTime
        if steepTime > 1:
            steepTime -= 1
            steepTimeDisplay.setText(str(steepTime) + " min")
            steepTimeDisplay.print()
            
    #Button Shifters
    buttonYShifter = 60
    #Steep Time Button Shifter
    button1XShifter = -50
    #Sugar Button Shifter
    button2XShifter = 50
    #Cream Button Shifter
    button3XShifter = 150

    #Generate Buttons
    #Generate Steep time Button
    addSteepTimeButton = doodler.Button(-40 + button1XShifter, 10 + buttonYShifter, 3.5, 2.5, onClick=addTime, color="lime", pressedColor="green", shape="triangle", angle=90, outlineWeight=4)
    removeSteepTimeButton = doodler.Button(-40 + button1XShifter, -50 + buttonYShifter, 3.5, 2.5, onClick=removeTime, color="lime", pressedColor="green", shape="triangle", angle=-90, outlineWeight=4)
    steepTimeDisplay = doodler.Text(-40 + button1XShifter, -34 + buttonYShifter, str(steepTime) + " min" , fontColor="black", alignment="center", font="Arial", fontSize=18, fontType="bold")
    steepTimeDisplay.print()
    steepTimeMinutes = doodler.Text(-36 + button1XShifter, 50 + buttonYShifter, "Steep\nTime", fontColor="black", alignment="center", font="Arial", fontSize=20, fontType="bold")
    steepTimeMinutes.print()

    #Generate Sugar Button
    addSugarButton = doodler.Button(-40 + button2XShifter, 10 + buttonYShifter, 3.5, 2.5, onClick=addSugar, color="lime", pressedColor="green", shape="triangle", angle=90, outlineWeight=4)
    removeSugarButton = doodler.Button(-40 + button2XShifter, -50 + buttonYShifter, 3.5, 2.5, onClick=removeSugar, color="lime", pressedColor="green", shape="triangle", angle=-90, outlineWeight=4)
    SugarDisplay = doodler.Text(-40 + button2XShifter, -34 + buttonYShifter, numSugars, fontColor="black", alignment="center", font="Arial", fontSize=18, fontType="bold")
    SugarDisplay.print()
    NumberOfSugars = doodler.Text(-36 + button2XShifter, 50 + buttonYShifter, "Sugar", fontColor="black", alignment="center", font="Arial", fontSize=20, fontType="bold")
    NumberOfSugars.print()

    #Generate Cream Button
    addCreamButton = doodler.Button(-40 + button3XShifter, 10 + buttonYShifter, 3.5, 2.5, onClick=addCreams, color="lime", pressedColor="green", shape="triangle", angle=90, outlineWeight=4)
    removeCreamButton = doodler.Button(-40 + button3XShifter, -50 + buttonYShifter, 3.5, 2.5, onClick=removeCreams, color="lime", pressedColor="green", shape="triangle", angle=-90, outlineWeight=4)
    CreamDisplay = doodler.Text(-40 + button3XShifter, -34 + buttonYShifter, numCreams, fontColor="black", alignment="center", font="Arial", fontSize=18, fontType="bold")
    CreamDisplay.print()
    NumberOfCreams = doodler.Text(-36 + button3XShifter, 50 + buttonYShifter, "Cream", fontColor="black", alignment="center", font="Arial", fontSize=20, fontType="bold")
    NumberOfCreams.print()

    menuLoader = doodler.Loader(-260, -140, 40, loaderColor="black", eraserColor="light gray", outlineWeight=6)
    InstructionText = doodler.Text(80, -155, "Please Customize Your Tea", fontColor="black", alignment="center", font="Arial", fontSize=25, fontType="bold")
    InstructionText.print()

    exitButton = doodler.Button(340, 170, 2.5, 3.5, color = "red", pressedColor = "darkred", onClick = lambda: doodler.terminate())

    text1 = doodler.Text(340, 200, "Exit")
    text1.print()

    #Main Loop
    screen.tracer(1)

    doodler.getGUI().after(0, menuLoader.run)
    doodler.mainloop()
    
if __name__ == "__main__":
    main()
    
    












