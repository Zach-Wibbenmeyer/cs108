'''Using Python to Draw Two Circles
March 2, 2015
Homework 4
Zach Wibbenmeyer (zdw3)'''

#Gain access to the turtle module
import turtle

#Prompts the user to enter a first x-coordinate
x = int(input('Enter a first x-coordinate: '))
#Prompts the user to enter a first y-coordinate
y = int(input('Enter a first y coordinate: '))
#Prompts the user to enter a first radius
radius1 = int(input('Enter the first radius: '))
#Prompts the user to enter a second x-coordinate
x2 = int(input('Enter the second x-coordinate: '))
#Prompts the user to enter a second y-coordinate
y2 = int(input('Enter the second y-coordinate: '))
#Prompts the user to enter a second radius
radius2 = int(input('Enter the second radius: '))

#Creates a tuple of the first x and y coordinates
point1 = (x,y)
#Creates a tuple of the second x and y coordinates
point2 = (x2,y2)

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

#Create a turtle and name it zach
zach = turtle.Turtle()

#Tells zach to pick the pen up
zach.penup()
#Tells zach to go to point 1
zach.goto(point1)
#Tells zach to put the pen down
zach.pendown()
#Tells zach to draw a circle of radius 1
zach.circle(radius1)
#Tells zach to pick the pen up
zach.penup()
#Tells zach to go to point 2
zach.goto(point2)
#Tells zach to put the pen down
zach.pendown()
#Tells zach to draw a circle of radius 2
zach.circle(radius2)

#Calculates the distance between points
distance = ((x2 - x)**2 + (y2 - y)**2)**.5

#Tests if the circles are disjoint
if distance > (radius1 + radius2):
    zach.write('Circles are disjoint' , font = ('Arial' , 20 , 'italic'))
#Tests if circle 1 contains circle 2
elif (distance + radius2) < radius1:
    zach.write('Circle 1 contains circle 2' , font = ('Arial' , 20 , 'italic'))
#Tests if circle 2 contains circle 1
elif (distance + radius1) < radius2:
    zach.write('Circle 2 contains circle 1' , font = ('Arial' , 20 , 'italic'))
#If none of the above works, then the circles overlap
else:
    zach.write('Circle 1 and circle 2 overlap' , font = ('Arial' , 20 , 'italic'))


#Keep the window open until it is clicked on
window.exitonclick()