##########################################
# Splash Text for Sanson Labs TeaMachine #
##########################################

import turtle
import time
from utils import playWavSound
from turtleLetterUtils import fillLetter
from letters import T, e, a, M, c, h, i, n
from menudoodle import MenuDoodle

def splashText(screen):
    # Initialize turtles
    text = turtle.RawTurtle(screen)
    text.hideturtle()

    fillTurt = turtle.RawTurtle(screen)
    fillTurt.penup()
    fillTurt.hideturtle()

    lowerTurt = turtle.RawTurtle(screen)
    lowerTurt.penup()
    lowerTurt.hideturtle()

    upperTurt = turtle.RawTurtle(screen)
    upperTurt.penup()
    upperTurt.hideturtle()

    # Draw splash text
    screen.tracer(30)
    text.speed("fastest")


    time.sleep(0.1)
    screen.bgcolor("light gray")
    time.sleep(0.1)
    screen.bgcolor("gray")
    time.sleep(0.1)
    
    text.pensize(56) #50
    text.pencolor("lime")

    playWavSound("./sounds/Woosh.wav", blocking=False)
    
    #Backbackground
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

    #Fill T
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 85, vertDist = 30, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -300, y = 130, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 30, vertDist = 230, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 85, vertDist = 30, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    #Fill E
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 20, vertDist = 100, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -182.54, y = 42.75, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 35, vertDist = 100, gap = 20, numGaps = 2, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 15, vertDist = 100, gap = 60, numGaps = 1, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    #Fill A
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 20, vertDist = 100, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -107.54, y = 70.11, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 30, vertDist = 100, gap = 'n/a', numGaps = 'n/a', gapList = [20, 40, 20, 20, 1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 20, vertDist = 100, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill M
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 20, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [-55, 20], x = [-127.60, -127.60], y = [-45.58, -175.58], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 55.7, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [-55.5, -54.5], x = [upperTurtX - 1, lowerTurtX - 1], y = [upperTurtY, lowerTurtY + 67], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 44, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [67.5, 67.5], x = [upperTurtX + 5, lowerTurtX], y = [upperTurtY, lowerTurtY], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 20, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [67.5, 20], x = [upperTurtX + 1, lowerTurtX], y = [upperTurtY + 1, lowerTurtY - 45], color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 20, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [67.5, 20], x = [upperTurtX + 1, -60.45], y = [upperTurtY, -151.68], color = "white", size = 4)

    #Fill A
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = -33.84, y = -67.87, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 26, vertDist = 75, gap = 'n/a', numGaps = 'n/a', gapList = [15, 30, 15, 15, 1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill C
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 22.54, y = -47.35, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 39.5, vertDist = 75, gap = 45, numGaps = 1, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill H
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 80.33, y = -26.32, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 24.5, vertDist = 75, gap = "n/a", numGaps = "n/a", gapList = [30, 15, 30, -1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 13, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill I
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 20, vertDist = 75, gap = "n/a", numGaps = "n/a", gapList = [15, 45, 15, 1], slope = 20, x = 138.12, y = -5.29, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 15, vertDist = 75, gap = "n/a", numGaps = "n/a", gapList = [15, 45, 15, 1], slope = 20, x = xPos, y = yPos, color = "white", size = 4)

    #Fill N
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 195.91, y = 15.75, color = "white", size = 4)
    (upperTurtX, upperTurtY, lowerTurtX, lowerTurtY) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 50, vertDist = 'n/a', gap = 'n/a', numGaps = 'n/a', gapList = [], slope = [-67, -67], x = [xPos + 3, xPos + 3], y = [19.75, 0.75], color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 235.91, y = 29.62, color = "white", size = 4)

    #Fill E
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 15, vertDist = 75, gap = 0, numGaps = 0, gapList = [], slope = 20, x = 259.41, y = 38.8, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 26.25, vertDist = 75, gap = 15, numGaps = 2, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)
    (xPos, yPos) = fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist = 11.25, vertDist = 75, gap = 45, numGaps = 1, gapList = [], slope = 20, x = xPos, y = yPos, color = "white", size = 4)


    screen.update()

    time.sleep(3)
    screen.clear()
    screen.tracer(100)

    screen.bgcolor("light gray")

if __name__ == "__main__":
    doodler =  MenuDoodle()
    screen = doodler.getScreen()

    splashText(screen)