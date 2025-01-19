import turtle as tur

### GLOBAL VARIABLES ####################
table_size = 12 #table size set         #
score=0 # scoreboard reset              #
xVals = [30,20,10,0,-10,-20]            #
yVals = [-30,-20,-10,0,10,20]           #
turtleList =[]                          #
#########################################

gameBoard = tur.Screen()
gameBoard.bgcolor("light yellow") #screen backcolor set
gameBoard.title("Escape the Turtle") #screenboard title set

countIns = tur.Turtle() #count of click turtle

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

    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("red")

    t.goto(x * table_size, y * table_size) #distance turtles calculate


def show_turtles():

    for yy in yVals:
        for xx in xVals:
            create_turtle(xx,yy)

    countIns.clear()
    countIns.write(arg=("Count:"+str(score)), move=False, align="center",
                       font=("Verdana", 25, "bold"))  # Write on the Turtle screen object

tur.tracer(0) #turtle shaping is now start (NO ANIMATION)
count_turtle() #write count value on top of the screen
show_turtles()
tur.tracer(1) #turtle shaping is now finish

tur.mainloop()