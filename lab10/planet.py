'''
Model a planet
Created Fall 2014

@author: zdw3
'''

#Gain access to the turtle module
import turtle

#Create a class named Planet
class Planet:
    '''
    This class will model a planet
    '''
    #Initialize the instance variables
    def __init__(self, name, rad, m, dist, color):
        self._name = name
        self._color = color
        #If statement checking for positive values
        if (rad >= 0) and (m >= 0) and (dist >= 0):
            self._radius = rad
            self._mass = m
            self._distance = dist
        else:
            #Raise an exception
            raise ValueError('radius, mass, and distance must be positive values')
        #Initialize the x and y coordinates
        self._x = self._distance
        self._y = 0
        #Create a turtle as an instance variable
        self._turtle = turtle.Turtle()
        self._turtle.penup()
        self._turtle.color(self._color)
        self._turtle.shape('circle')
        self._turtle.shapesize(self._radius, self._radius)
        self._turtle.goto(self._x, self._y)
        
    def get_name(self):
        return self._name
    
    def get_radius(self):
        return self._radius
    
    def get_mass(self):
        return self._mass
    
    def get_distance(self):
        return self._distance
    
    def set_name(self, newname):
        self._name = newname
    
    def __str__(self):
        return self._name
    
'-------------------------------#Main Code------------------------------------------------------'
#Tests for creating a legitimate planet
p1 = Planet("Hey John, What's Your Name Again?", 11, 12, 15, 'red')
print(p1)

p2 = Planet('Reptar, King of the Ozone', 11.5, 16, 2, 'blue')
print(p2)

#Tests for not maintaining one of the invariants
#p3 = Planet('Monkey', -1, 16, 5)
#print(p3)

#p4 = Planet('Goats on a Boat', 5, -2, 5)
#print(p4)

#p5 = Planet('I Hate Buffering', 5, 6, -3)
#print(p5)