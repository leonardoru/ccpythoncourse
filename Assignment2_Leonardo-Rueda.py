# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYT-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 2: Write a python program using turtle to draw following squares with initial side length for 120 ....
# Student: Leonardo Rueda

import turtle
import random

# Here are some initial variables, length and initial coordinates
length = 120
xPos = 5
yPos = 5

# Here we actually position the pen on the desired intial coordinates without drawing anything yet.
turtle.penup()
turtle.setx(xPos)
turtle.sety(yPos)
turtle.pendown()

# And now we loop based on te length variable
while length > 0:

    # Some turtle variables first
    turtle.speed('slow')
    turtle.pencolor('red')

    # Now lets draw the square
    turtle.forward(length)
    turtle.right(90)
    
    turtle.forward(length)
    turtle.right(90)
    
    turtle.forward(length)
    turtle.right(90)
    
    turtle.forward(length)
    turtle.right(90)

    # Finally set a new position without drawing
    turtle.penup()
    xPos = xPos + 8
    yPos = yPos - 8
    turtle.goto(xPos,yPos)
    turtle.pendown()

    # Decrease length in order to eventually break the loop 
    length -= 20

# By Leonardo Rueda



