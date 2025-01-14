### SQUARE in SQUARE Drawing ###
import turtle as tur #shortname is tur

shape = tur.Screen()
shape.bgcolor("light blue") #background color
shape.title("Black Board - Square in Square") #titled

shape = tur.Turtle() #new objective defined
shape.color("yellow") #arrow color set
tur.speed(0) #animation speed value

def square(dim,angle): #define drawing method
    for i in range(4):
        tur.forward(dim)
        tur.left(angle)
        dim-=1
        angle+=1

for i in range(60):
    square(120,90)


tur.done()