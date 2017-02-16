''' A Turtle Graphics program that draws the Olympics Symbol
Created Spring 2015
Homework 01
@Author: Zach Wibbenmeyer (zdw3)'''

#Gain access to the turtle module
import turtle

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

#Create a turtle and name it zach
zach = turtle.Turtle()

#Draws a blue circle with a radius of 50 and a pen size of 5
zach.pencolor("Blue")
zach.pensize(5)
zach.circle(50)
zach.penup()

#Draws a yellow circle with a radius of 50 and a pen size of 5
zach.forward(55)
zach.right(90)
zach.forward(55)
zach.left(90)
zach.pendown()
zach.pencolor("Yellow")
zach.circle(50)
zach.penup()

#Draws a black circle with a radius of 50 and a pen size of 5
zach.forward(55)
zach.left(90)
zach.forward(55)
zach.right(90)
zach.pendown()
zach.pencolor("Black")
zach.circle(50)
zach.penup()

#Draws a green circle with a radius of 50 and a pen size of 5
zach.forward(55)
zach.right(90)
zach.forward(55)
zach.left(90)
zach.pendown()
zach.pencolor("Green")
zach.circle(50)
zach.penup()

#Draws a red circle with a radius of 50 and a pen size of 5
zach.forward(55)
zach.left(90)
zach.forward(55)
zach.right(90)
zach.pendown()
zach.pencolor("Red")
zach.circle(50)
zach.penup()

#Keep the window open until it is clicked
window.exitonclick()

