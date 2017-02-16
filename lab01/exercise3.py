''' A first turtle graphics program
Created Fall 2014
Lab 01
@author: Serita Nelesen (smn4)
'''

#Gain access to the turtle module
import turtle

#Give the name "window" to the screen where the turle will appear
window = turtle.Screen()

#Create a turle named zach
zach = turtle.Turtle()

#Tell zach to move backwards 50 pixels
zach.backward(50)

#Tell zach to turn right 90 degrees
zach.right(90)

#Tell zach to move forward 150 pixels
zach.forward(150)

#Tell zach to turn left 90 degrees
zach.left(90)

#Tell zach to move forward 50 pixels
zach.forward(50)

#Tell zach to pick up the pen cursor
zach.penup()

#Tell zach to move forwards 70 pixels
zach.forward(70)

#Tell zach to turn left 90 degrees
zach.left(90)

#Tell zach to move forward 150 pixels
zach.forward(150)

#Tell zach to turn left 90 degrees
zach.left(90)

#Tell zach to put the pen cursor down
zach.pendown()

#Tell zach to move forwards 50 pixels
zach.forward(50)

#Tell zach to turn left 90 degrees
zach.left(90)

#Tell zach to move forwards 75 pixels
zach.forward(75)

#Tell zach to turn left 90 degrees
zach.left(90)

#Tell zach to move forwards 50 pixels
zach.forward(50)

#Tell zach to turn right 90 degrees
zach.right(90)

#Tell zach to move forwards 75 pixels
zach.forward(75)

#Tell zach to turn right 90 degrees
zach.right(90)

#Tell zach to move forwards 50 pixels
zach.forward(50)

#Keep the window open until it is clicked
window.exitonclick()