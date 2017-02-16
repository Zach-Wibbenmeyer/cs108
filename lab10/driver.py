'''
Created on May 7, 2015

@author: zdw3
'''

#Import the necessary modules
import turtle
from solar_system import *

#Assign a turtle to the window
window = turtle.Screen()
#Set the coordinates of the window
window.setworldcoordinates(-1, -1, 1, 1)

#Create the solar system
ss = Solar_System() 
ss.add_sun(Sun("SUN", 19.5, 1000, 5800))
ss.add_planet(Planet("EARTH", .475, 5000, 0.3, 'blue'))

#Exception for a user prompted planet
try:
    #Prompt the user for a planet
    name = input('Please enter a name for the planet: ')
    radius = float(input('Please enter a radius: '))
    mass = float(input('Please enter a mass: '))
    distance = float(input('Please enter a distance from the sun: '))
    color = input('Please enter a color: ')
    ss.add_planet(Planet(name, radius, mass, distance, color))
except TypeError as what:
    print('Please enter strings for the given values: ', what)
except ValueError as what:
    print('Please enter positive numbers', what)
except turtle.TurtleGraphicsError as what:
    print('Please enter a legitimate color: ', what)

#Keep the window open until it is clicked
window.exitonclick()
