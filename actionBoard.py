### Action Drawing Board Created

import turtle as tur #turtle imported and its names tur

blackBoard = tur.Screen() #blackBoard Screen created
blackBoard.bgcolor("black") #set bg color
blackBoard.title("Action Black Board") #set board title

blackIns = tur.Turtle() # blackIns Turtle object has created
blackIns.color("white") # arrow and line color sets

def drawing(): #a function defined
    blackIns.forward(150) #forward XXX px action

blackBoard.listen() #keyboard listen has started
blackBoard.onkey(fun=drawing,key="space") # press to space button on keyboard

tur.mainloop() #loop func.
