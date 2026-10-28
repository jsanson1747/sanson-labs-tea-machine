##################################
# GUI for Sanson Labs TeaMachine #
##################################

#Import Dependencies
import turtle
from menudoodle import MenuDoodle
from utils import playWavSound
from logo import logo
from splashText import splashText
from teaSettings import TeaSettings

def intro(screen):
    logo(screen)
    splashText(screen)
    
def main():

    # Initialize MenuDoodle and Screen
    doodler =  MenuDoodle()
    screen = doodler.getScreen()

    # Play the intro sounds and display splash text
    intro(screen)

    # Start main interface
    playWavSound("src\sounds\T.A.L.O.S-2026-10-21-00-31-Welcome-to-the-Sanson-Labs-Tea-Machine.-Please-c.wav", blocking=False)

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
    tea = TeaSettings()

    #Define Button Functions
    def drawTea(color):
        liquid = doodler.Ellipse(-260, 100 + teaMugYShifter, 26, 6, fill=True, color=color, outlineWeight=4)
        screen.tracer(100)
        liquid.draw()
        screen.tracer(1)
        screen.update()

    def creamChanged(n):
        if n <2 and n > 0:
            drawTea("tan")
        elif n == 0:
            drawTea("brown")

    def bindDisplay(attr, display, fmt=str):
        def refresh(value):
            display.setText(fmt(value))
            display.print()
        tea.subscribe(attr, refresh)

    def adjuster(attr, delta):
        sound = "./sounds/HighBonk.wav" if delta > 0 else "./sounds/LowBonk.wav"
        def onPress():
            playWavSound(sound, blocking=False)
            tea.adjust(attr, delta)
        return onPress
            
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
    addSteepTimeButton = doodler.Button(-40 + button1XShifter, 10 + buttonYShifter, 3.5, 2.5, onClick=adjuster("steepTime", 1), color="lime", pressedColor="green", shape="triangle", angle=90, outlineWeight=4)
    removeSteepTimeButton = doodler.Button(-40 + button1XShifter, -50 + buttonYShifter, 3.5, 2.5, onClick=adjuster("steepTime", -1), color="lime", pressedColor="green", shape="triangle", angle=-90, outlineWeight=4)
    steepTimeDisplay = doodler.Text(-40 + button1XShifter, -34 + buttonYShifter, str(tea.steepTime) + " min" , fontColor="black", alignment="center", font="Arial", fontSize=18, fontType="bold")
    steepTimeDisplay.print()
    bindDisplay("steepTime", steepTimeDisplay, lambda v: f"{v} min")
    steepTimeMinutes = doodler.Text(-36 + button1XShifter, 50 + buttonYShifter, "Steep\nTime", fontColor="black", alignment="center", font="Arial", fontSize=20, fontType="bold")
    steepTimeMinutes.print()

    #Generate Sugar Button
    addSugarButton = doodler.Button(-40 + button2XShifter, 10 + buttonYShifter, 3.5, 2.5, onClick=adjuster("numSugars", 1), color="lime", pressedColor="green", shape="triangle", angle=90, outlineWeight=4)
    removeSugarButton = doodler.Button(-40 + button2XShifter, -50 + buttonYShifter, 3.5, 2.5, onClick=adjuster("numSugars", -1), color="lime", pressedColor="green", shape="triangle", angle=-90, outlineWeight=4)
    sugarDisplay = doodler.Text(-40 + button2XShifter, -34 + buttonYShifter, tea.numSugars, fontColor="black", alignment="center", font="Arial", fontSize=18, fontType="bold")
    sugarDisplay.print()
    bindDisplay("numSugars", sugarDisplay)
    NumberOfSugars = doodler.Text(-36 + button2XShifter, 50 + buttonYShifter, "Sugar", fontColor="black", alignment="center", font="Arial", fontSize=20, fontType="bold")
    NumberOfSugars.print()

    #Generate Cream Button
    addCreamButton = doodler.Button(-40 + button3XShifter, 10 + buttonYShifter, 3.5, 2.5, onClick=adjuster("numCreams", 1), color="lime", pressedColor="green", shape="triangle", angle=90, outlineWeight=4)
    removeCreamButton = doodler.Button(-40 + button3XShifter, -50 + buttonYShifter, 3.5, 2.5, onClick=adjuster("numCreams", -1), color="lime", pressedColor="green", shape="triangle", angle=-90, outlineWeight=4)
    creamDisplay = doodler.Text(-40 + button3XShifter, -34 + buttonYShifter, tea.numCreams, fontColor="black", alignment="center", font="Arial", fontSize=18, fontType="bold")
    creamDisplay.print()
    bindDisplay("numCreams", creamDisplay)
    tea.subscribe("numCreams", creamChanged)
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
    
    












