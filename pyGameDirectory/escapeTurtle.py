import turtle as tur
import random



### GLOBAL VARIABLES ####################
table_size = 12 #table size set         #
score=0 # scoreboard reset              #
xVals = [30,20,10,0,-10,-20]            #
yVals = [-30,-20,-10,0,10,20]           #
turtleList =[]                          #
timerVal=600                           #
countDown=15                            #
gameOver = False                        #
#########################################

gameBoard = tur.Screen()
gameBoard.bgcolor("light yellow") #screen backcolor set
gameBoard.title("Escape the Turtle") #screenboard title set

countIns = tur.Turtle() #count of click turtle
count_down = tur.Turtle()

def count_turtle():

    countIns.color("dark green")
    countIns.penup() #pen up on the board
    countIns.hideturtle() #turtle arrow is hide

    top = gameBoard.window_height()/2 #top on the gameBoard Screen
    yAxis = top*0.9 #y-axis value
    countIns.setpos(0,yAxis) #set position on the screen
    countIns.write(arg="Count:0", move=False, align="center",
                   font=("Verdana", 25, "bold"))  # Write on the Turtle screen object


def create_turtle(x,y): #Turtle show position on screen function
    t = tur.Turtle()
    def detect_click(x,y):
        global score
        global gameOver
        score+=1
        if not gameOver:
            countIns.clear()
            countIns.write(arg=f"Count:{score}", move=False, align="center",
                            font=("Verdana", 25, "bold"))  # Write on the Turtle screen object
            #print(x,y)
    t.onclick(detect_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("red")

    t.goto(x * table_size, y * table_size) #distance turtles calculate
    turtleList.append(t) #List array has added

def show_turtles(): #all turtle show func.

    for yy in yVals:
        for xx in xVals:
            create_turtle(xx,yy)

def hide_turtles(): #all turtles hide func.
    for t in turtleList:
        t.hideturtle()

def random_show_turtle(): # random choice turtle function
    if not gameOver:
        hide_turtles()
        random.choice(turtleList).showturtle()
        gameBoard.ontimer(random_show_turtle,timerVal) #recursive function: running function in self

def count_down_func(countDown):
    global gameOver
    count_down.color("dark green")
    count_down.penup()  # pen up on the board
    count_down.hideturtle()  # turtle arrow is hide

    top = gameBoard.window_height() / 2  # top on the gameBoard Screen
    yAxis = top * 0.9  # y-axis value
    count_down.setpos(0, yAxis-30)  # set position on the screen

    if countDown>0:
        count_down.clear()
        count_down.write(arg=f"Timer:{countDown}", move=False, align="center",
                   font=("Verdana", 25, "bold"))  # Write on the Turtle screen object
        gameBoard.ontimer(lambda: count_down_func(countDown-1),1000)

    else:
        gameOver=True
        count_down.clear()
        hide_turtles()
        count_down.write(arg="Game Over", move=False, align="center",
                         font=("Verdana", 25, "bold"))  # Write on the Turtle screen object

def start_the_game():
    tur.tracer(0) #turtle shaping is now start (NO ANIMATION)
    count_turtle() #write count value on top of the screen
    show_turtles() #all turtles show
    hide_turtles() #all turtles hide
    random_show_turtle() #random a turtle show
    count_down_func(countDown)
    tur.tracer(1) #turtle shaping is now finish

start_the_game()
tur.mainloop()