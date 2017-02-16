'''Python: Using a turtle module to create a line specified by the user
February 19, 2015
Lab 3 Exercise 4
Zach Wibbenmeyer (zdw3)'''

#Gains access to the turtle module
import turtle

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()
#Create a turtle and name it zach
zach = turtle.Turtle()
#Tells the turtle to hide the arrow on the screen
zach.hideturtle()


x = int(input("Please enter an X coordinate: ")) #Prompts the user to enter the first x coordinate
y = int(input("Please enter a Y coordinate: ")) #Prompts the user to enter the first y coordinate
x1 = int(input("Please enter a second X coordinate: ")) #Prompts the user to enter a second x coordinate
y1 = int(input("Please enter a second Y coordinate: ")) #Prompts the user to enter a second y coordinate

#Creates two tuples that specifies the coordinates
point1 = (x,y)
point2 = (x1,y1)

#Changes the pensize to be 3
zach.pensize(3)
#Picks the pen up
zach.penup()
#Goes to point 1
zach.goto(point1)
#Puts the pen down
zach.pendown()
#Draws a line to point 2
zach.goto(point2)
#Picks the pen up
zach.penup()

#Create a variable to concatenate 'p2' and point 2 together
string1 = ('p2 ' + str(point2))
#Tells the turtle to write the second point
zach.write(string1 , font = ('Arial' , 20 , 'italic'))

#Tells the turtle to go to point 1
zach.penup()
zach.goto(point1)

#Create another variable that concatenates 'p2' and the second point together
string2 = ('p1 ' + str(point1))
#Tells the turtle to write the first point
zach.write(string2, font = ('Arial',20, 'italic'))

#Creates two tuples that contain together the x and y values
point3 = (y,y1)
point4 = (x,x1)
#Creates variables that find the minimum of the x and y values
lowest_number_x = min(point4)
lowest_number_y = min(point3) - 100
#Tells the turtle to go to the lowest x and y values
zach.goto(lowest_number_x,lowest_number_y)

#Creates a variable named distance that calculates the distance between the two points
distance = ((x1 - x)**2 + (y1 - y)**2)**.5

#Create another variable that concatenates a sentence and the length together
string3 = ('This is the line you described! \n Its length is ' + str(distance))
#Tells the turtle to write 
zach.write(string3 , font = ('Arial' , 20 , 'italic'))

#Keep the window screen open until it is clicked on
window.exitonclick()