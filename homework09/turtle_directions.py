'''
Using Python to Prompt the User For Turtle Directions
April 22, 2015
Homework 09
Zach Wibbenmeyer (zdw3)
'''

#Gains access to the turtle module
import turtle
#Gains access to the system module
import sys

#Create a turtle named zach
zach = turtle.Turtle()

#Prompts the user to enter various directions for the Turtle
file_name = str(input('Please enter a file name: '))

color_name = ['green', 'red', 'pink', 'purple', 'black', 'blue']

#Opens a text file that the user has entered
with open(file_name) as file:
    
    #Reads through each line
    words = file.readlines()
    #Create a variable that counts the length of the text
    count = len(words)
    
    #If statement that checks if there are any commands in the text
    if count > 0:
        #For loop iterating through each item in words
        for lines in words:
            #Checks to see if there is whitespace between the lines
            if lines != '\n':
                #Split up the lines
                lines = lines.split()
                #For the command 'penup'
                if lines[0] == 'penup':
                    zach.penup()
                #For the command 'pendown'
                elif lines[0] == 'pendown':
                    zach.pendown()
                #For the 'pencolor' command
                elif lines[0] == 'color':
                    #Checks if the second index is in the list of colors
                    if lines[1] in color_name:
                        zach.pencolor(lines[1])
                    else:
                        #Otherwise print an error and exit the program
                        print('Please enter a valid color', file = sys.stderr)
                        sys.exit(-1)
                #For the command 'goto'
                elif lines[0] == 'goto':
                    #Checks if the x and y coordinates are integers
                    if (float(lines[1]) % 1 == 0) and (float(lines[2]) % 1 == 0):
                        zach.penup()
                        zach.goto(int(lines[1]), int(lines[2]))
                        zach.pendown()
                    else:
                        #Otherwise print an error message and close the program
                        print('Please enter only coordinates that are integers', file = sys.stderr)
                        sys.exit(-1)
                #For the command 'point size'
                elif lines[0] == 'point':
                    #Checks if x and y are integers and if 'size' is an integer between 5 and 20 inclusive
                    if (float(lines[2]) % 1 == 0) and (float(lines[3]) % 1 == 0) and ((float(lines[1]) % 1 == 0) and (5 <= float(lines[1]) <= 20)): 
                        zach.penup()
                        zach.goto(int(lines[2]), int(lines[3]))
                        zach.pendown()
                        zach.dot(int(lines[1]))
                    else:
                        #Otherwise print an error message and close the program
                        print('Please enter only coordinates that are integers', file = sys.stderr)
                        sys.exit(-1)
                #For the command 'forward'
                elif lines[0] == 'forward':
                    #Checks if the coordinate is an integer
                    if float(lines[1]) % 1 == 0:
                        zach.forward(int(lines[1]))
                    else:
                        #Otherwise print an error message and close the program
                        print('Please enter only integers as coordinates', file = sys.stderr)
                        sys.exit(-1)
                #For the command 'right'
                elif lines[0] == 'right':
                    #Checks to see if the angle is an integer
                    if float(lines[1]) % 1 == 0:
                        zach.right(int(lines[1]))
                    else:
                        #Otherwise prints an error message and closes the program
                        print('Please enter only integers as coordinates', file = sys.stderr)
                        sys.exit(-1)
                #For the command 'left'
                elif lines[0] == 'left':
                    #Checks to see if the angle entered is an integer
                    if float(lines[1]) % 1 == 0:
                        zach.left(int(lines[1]))
                    else:
                        #Otherwise prints an error message and closes the program
                        print('Please enter only integers as coordinates', file = sys.stderr)
                        sys.exit(-1)
            #Otherwise prints an error message and closes the program
            else:
                print('Please make sure there is no whitespace between the lines', file = sys.stderr)
                sys.exit(-1)
    #Otherwise prints an error message and closes the program
    else:
        print('Please enter some commands', file = sys.stderr)
        sys.exit(-1)

#Make the window the screen where the turtle will appear
window = turtle.Screen()

#Keep the window open until it is clicked
window.exitonclick()