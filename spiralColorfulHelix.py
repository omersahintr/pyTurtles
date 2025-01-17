### COLORFUL HELIX SPIRAL SHAPE DRAWING ###

import turtle as tur
import secrets as sec
from math import pi


helix = tur.Screen() #define screen
helix.title("Helix Spinner") #title name
helix.bgcolor("black") #background color set

spinner = tur.Turtle() #new turtle object created
spinner.speed(0.22) #object animation speed has changed
spinner.color("red") #default line color set

for i in range(150): #150 times for loop
    spinner.circle(pi * i) #pi=3.14 calculate
    spinner.circle(-pi * i) #-pi=-3.14
    spinner.circle(20 * (i / 100), 10 * (i / 100), (1)) #circle animation formula

    scolor = ""
    x = 0

    while x<6: #this loop generate to color hexcode
        scolor += sec.choice("0123456789ABCDEF") #secret code generated for base hexcode
        x += 1
    spinner.color("#"+scolor)


#tur.done() #turtle has closed
tur.mainloop() #always running with mainloop non-stop
###dev2 added
