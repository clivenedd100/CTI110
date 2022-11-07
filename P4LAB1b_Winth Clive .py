#CTI-110
#P4LAB1B - Initials
#Winth Clive
#11/07/2022

import turtle
t = turtle.Turtle()
t.speed(5)
t.getscreen() .bgcolor('black')
t.shape('turtle')
t.color('yellow')
t.pencolor('blue')
t.pensize(10)

# C shape

t.penup()
t.goto(-30, 50)
t.pendown()
t.right(180)
t.circle(50,180)
t.penup()
t.forward(100)


#W shape
t.penup()
t.pendown()
t.pensize(10)
t.right(80)
t.forward(100)
t.left(160)
t.forward(100)
t.right(160)
t.forward(100)
t.left(160)
t.forward(100)

turtle.done()
        

 
