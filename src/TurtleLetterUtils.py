import turtle
import math

def fillLetter(fillTurt, lowerTurt, upperTurt, screen, horizDist, vertDist, gap, numGaps, gapList, slope, x, y, color, size):
    fillTurt.penup()
    
    fillTurt.pencolor(color)
    fillTurt.pensize(size)
    fillTurt.seth(270)
    distance = 0
    
    if gap == 0 and str(type(slope)):
        fillTurt.goto(x, y)
        fillTurt.pendown()
        while distance < horizDist:
            fillTurt.forward(vertDist)
            fillTurt.penup()
            fillTurt.seth(slope)
            fillTurt.forward(1)
            fillTurt.seth(90)
            fillTurt.forward(vertDist)
            fillTurt.seth(270)
            fillTurt.pendown()
            distance += 1
        return(fillTurt.xcor(), fillTurt.ycor())
    
    elif len(gapList) != 0:
        fillTurt.goto(x, y)
        fillTurt.pendown()
        alternatorNum = gapList[-1]
        gapList.pop(len(gapList) - 1)
        while distance < horizDist:
            fillTurt.seth(270)
            alternator = alternatorNum
            for length in gapList:
                fillTurt.pendown()
                if alternator == -1:
                    fillTurt.penup()
                fillTurt.forward(length)
                alternator *= -1
            fillTurt.seth(slope)
            fillTurt.forward(1)
            fillTurt.penup()
            fillTurt.seth(90)
            fillTurt.forward(vertDist)
            distance += 1
        return(fillTurt.xcor(), fillTurt.ycor())
    
    elif str(type(slope)) == "<class 'list'>":
        upperX = x[0]
        lowerX = x[1]
        upperY = y[0]
        lowerY = y[1]
        
        
        lowerTurt.goto(lowerX, lowerY)
        upperTurt.goto(upperX, upperY)
        
        upperSlope = slope[0]
        lowerSlope = slope[1]

        upperTurt.seth(upperSlope)
        lowerTurt.seth(lowerSlope)
        
        calculatedVerticalDistance = 0
        while distance < horizDist:
            upperTurt.forward(1)
            lowerTurt.forward(1)
            fillTurt.goto(upperTurt.pos())
            fillTurt.pendown()
            fillTurt.goto(lowerTurt.pos())
            fillTurt.penup()
            
            distance += 1
        return(upperTurt.xcor(), upperTurt.ycor(), lowerTurt.xcor(), lowerTurt.ycor())        
            

    else:
        fillTurt.goto(x, y)
        fillTurt.pendown()
        fillAmt = (vertDist - (gap * numGaps)) / (numGaps + 1)
        while distance < horizDist:
            number = 0
            
            while number < numGaps + 1:
                fillTurt.pendown()
                fillTurt.forward(fillAmt)
                fillTurt.penup()
                fillTurt.forward(gap)
                number += 1
               
            fillTurt.penup()
            fillTurt.seth(slope)
            fillTurt.forward(1)
            fillTurt.seth(90)
            fillTurt.forward(vertDist + gap)
            fillTurt.seth(270)
            fillTurt.pendown()
            
            distance += 1
        return(fillTurt.xcor(), fillTurt.ycor())
