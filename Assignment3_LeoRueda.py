
# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYT-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 3: Write a Python program using turtle to draw polygons
# Student: Leonardo Rueda

import turtle
import random

# Here are some initial variables, length and initial coordinates
length = 80
xPos = 5
yPos = 5

# Main Methods
# First get the agle, divide 360 by sides
def angle(sides):
    angleDegress = 360 / sides
    return angleDegress

def drawShape(Turtle,sides,length):
    currentAngle = angle(sides)    
    i = 1 
    while i <= sides:
        turtle.forward(length)    
        turtle.right(currentAngle)
        sides = sides - 1

def SpinPolygon(Turtle, sides, angle, length, repeat):
    #  Re-set turtle
    turtle.reset()

    #  Set repetition number start
    repeatTurn = 1
    while repeatTurn <= repeat:
        turtle.left( angle + angle)
        drawShape(0,sides,length)
        repeatTurn = repeatTurn + 1


def ScalePolygon(Turtle, sides, length, sfactor, number):

    #  Re-set turtle
    turtle.reset()

    # Draw Initial polygon without variations.
    drawShape(0,sides,length)

    #  Set repetition number start
    repeatTurn = 2

    # Loop and grow
    while repeatTurn <= number:
        length = length * sfactor
        drawShape(0,sides,length)
        repeatTurn = repeatTurn + 1

# Examples
SpinPolygon(0,6, 13, 55, 40)

# By Leonardo Rueda
