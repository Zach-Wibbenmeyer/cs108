'''Using Python to draw a spirograph
March 5, 2015
Lab05 Exercise 2
Zach Wibbenmeyer (zdw3)'''

#Gains access to the turtle module
import turtle

#Gains access to the math module
import math

#Prompts the user to enter a choice if they would like to draw or not
choice = str(input('Would you like to draw a spirograph? (Y/n): '))

#Forever while loop
while True:
    #If statement checking if choice is no
    if choice == 'n' or choice == 'N':
        print('Okay! Maybe some other time')
        break
    #Else if statement checking if choice is yes
    elif choice == 'Y' or choice == 'y':

        #Create a variable named window and make it the turtle screen
        window = turtle.Screen()
        #Create a turtle and name it zach
        zach = turtle.Turtle()
        
        #Prompts the user to enter the moving radius
        mov_rad = float(input('Please enter a moving radius: '))
        #Prompts the user to enter the fixed radius
        fix_rad = float(input('Please enter a fixed radius: '))
        #Prompts the user to enter the pen offset
        pen_offset = float(input('Please enter the pen offset: '))
        #Prompts the user to enter the color
        color = str(input('Please enter the color: '))
        
        #Creates a variable of the current time and initializes it to 0
        current_time = 0.0
        
        #Finds the x value
        x = (fix_rad * mov_rad) * math.cos(current_time) + pen_offset * math.cos((((fix_rad + mov_rad) * current_time))/mov_rad)
        
        #Finds the y value
        y = (fix_rad * mov_rad) * math.sin(current_time) + pen_offset * math.sin((((fix_rad + mov_rad) * current_time))/mov_rad)
        #Tells zach to change the speed to 10
        zach.speed(10)
        #Tells zach to pick the pen up
        zach.penup()
        #Tells zach to go to the x and y points
        zach.goto(x,y)
        #Tells zach to put the pen down
        zach.pendown()
        #Tells zach to change the pen color to what the user enters
        zach.pencolor(color)
        
        #While loop checking if current_time is less than 100
        while current_time < 100:
            #Redefines the x variable
            x = (fix_rad * mov_rad) * math.cos(current_time) + pen_offset * math.cos((((fix_rad + mov_rad) * current_time))/mov_rad)
            #Redefines the y variable
            y = (fix_rad * mov_rad) * math.sin(current_time) + pen_offset * math.sin((((fix_rad + mov_rad) * current_time))/mov_rad)
            #Tells zach to go to the new x and y points
            zach.goto(x,y)
            #Increments the current time
            current_time += .1
        
        #Tell the turtle window to remain open until clicked on
        window.exitonclick()
    #Else if statement checking if choice is something other than yes
    elif choice != 'y' or choice != 'Y':
        choice = str(input('Would you like to draw a spirograph? (Y/n): '))