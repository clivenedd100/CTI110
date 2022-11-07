#CTI-110
#P4LAB1A - Shapes
#Winth Clive
#11/07/2022

import turtle   
import random
wn = turtle.Screen()
wn.bgcolor("black")
turtle.shape("turtle")
no_square=int(input("Enter no. of square"))


angle=360/no_square

#Turtle definition
square=turtle.Turtle()

#looping
for i in range(no_square):
    #creating random colors
    r=random.random()
    g=random.random()
    b=random.random()
    #setting color
    square.fillcolor(r,g,b)
    square.pencolor(r,g,b)
    #beginning filling
    square.begin_fill()

    #drawing square
    square.forward(75)
    square.left(90)
    square.forward(75)
    square.left(90)
    square.forward(75)
    square.left(90)
    square.forward(75)
    square.left(90)

    #slanting by angle' degree for square
    square.left(angle)

    #end placing
    square.end_fill()

import turtle
import random

no_circle=int(input("Enter no. of circles"))
radius=int(input("Enter radius"))


distance=radius/no_circle

#Turtle definition
circles=turtle.Turtle()

#hiding turtle from screen
circles.hideturtle()


#position of turtle
x=radius

#largest  circle
circles.goto(0,-x)


for i in range(no_circle):
               r=random.random()
               g=random.random()
               b=random.random()

            #color setting
               circles.fillcolor(r,g,b)
               circles.pencolor(r,g,b)

               circles.begin_fill()
               #circle radius of x
               circles.circle(x)
               circles.end_fill()

               #making radius smaller for next circle
               x=x-distance

               #next color for turtle
               circles.goto(0,-x)
