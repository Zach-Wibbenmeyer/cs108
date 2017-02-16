'''Using Turtle Graphics to Draw a Stick Figure
February 12, 2015
Zach Wibbenmeyer (zdw3)'''

#Gain access to the turtle module
import turtle

#Gain access to everything math related
import math

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

#Create a turtle named zach
zach = turtle.Turtle()

#Establishes a unit that can be changed
UNIT = 25

#Change the pensize to 3
zach.pensize(3)

#Draws the head
zach.circle(UNIT)

#Draws the neck
zach.right(90)
zach.forward(UNIT)

#Draws the arms
zach.left(90)
zach.forward(UNIT)
zach.left(180)
zach.forward(2 * UNIT)

#Draws the body
zach.right(180)
zach.forward(UNIT)
zach.right(90)
zach.forward(UNIT)

#Draws the left leg
zach.right(45)
zach.forward((2**.5) * UNIT)
zach.right(180)
zach.forward((2**.5) * UNIT)

#Draws the right leg
zach.right(90)
zach.forward((2**.5) * UNIT)

#Tell the window to stay open until it is clicked on
window.exitonclick()