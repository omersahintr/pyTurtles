### Action Drawing Board Created

import turtle as tur #turtle imported and its names tur

blackBoard = tur.Screen() #blackBoard Screen created
blackBoard.bgcolor("black") #set bg color
blackBoard.title("Action Black Board") #set board title

blackIns = tur.Turtle() # blackIns Turtle object has created
blackIns.color("white") # arrow and line color sets

def drawing(): #a function defined
    blackIns.forward(150) #forward XXX px action

def chanegAngleRight(): #rotate right angle
    blackIns.right(30)

def changeAngleLeft(): #Rotate left angle
    blackIns.left(30)

def cleanBoard(): #clear black board funvtion
    blackIns.clear()


def returnLastPoint(): #REturn home or last point
    blackIns.penup()  #pen up from board
    blackIns.home()  #jump to home point
    blackIns.pendown()  #pen down to board

def noPen(): #pen up function
    blackIns.penup()

def onPen(): #pen down function
    blackIns.pendown()


blackBoard.listen() #keyboard listening has started
blackBoard.onkey(fun=drawing,key="space") # press to space button on keyboard
blackBoard.onkey(fun=chanegAngleRight,key="Right") # press to Right button on keyboard
blackBoard.onkey(fun=changeAngleLeft,key="Left") # press to Left button on keyboard
blackBoard.onkey(fun=cleanBoard,key="c") # press to C button on keyboard
blackBoard.onkey(fun=returnLastPoint,key="h") # press to H button on keyboard
blackBoard.onkey(fun=noPen,key="n") # press to N button on keyboard
blackBoard.onkey(fun=onPen,key="o") # press to O button on keyboard

tur.mainloop() #loop func.
