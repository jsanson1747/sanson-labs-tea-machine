import turtle, time


turt2 = turtle.Turtle()
turt = turtle.Turtle()


turt.shape("square")
turt2.shape("square")

turt.color("white")
turt2.color("black")

turt2.turtlesize(3)
turt.turtlesize(2.5)

turt2.goto(-200, 200)
turt.goto(-200, 200)

turt2.write("Hello", True, "center", ("Arial", "8", "normal"))

turt2.goto(0, 0)
turt.goto(0, 0)

def FW(x, y):
    turt.forward(1)

def BW(x, y):
    turt.back(1)
    
while True:
    turt.onclick(FW, 1)
    turt.onclick(BW, 3)

'''
def parseTimeData():
    timeData = time.asctime().split(" ") #Split the time data into individual list items
    day = timeData[0] #Current Day
    month = timeData[1] #Current Month(The three letter abbreviation)
    date = timeData[2] #The current date(the number)
    
    milTime = timeData[3].split(":") #Split the time into hour, min, and sec
    hour = milTime[0]   #Current hour in military time
    minute = milTime[1] #Current minute in military time
    second = milTime[2] #Current second in military time
    
    year = timeData[4] #Current year
    print(year)
parseTimeData()
'''



'''

testText = "print('hello')"

exec(testText)

'''
