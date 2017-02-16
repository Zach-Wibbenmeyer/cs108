'''
Model a sun
Created Fall 2014

@author: zdw3
'''

#Gain access to the turtle module
import turtle

#Create a class named Sun
class Sun:
    '''
    This class will model the sun
    '''
    #Initialize the instance variables
    def __init__(self, name, rad, m, temp):
        self._name = name
        if (rad >= 0) and (m >= 0) and (temp > -273.15):
            self._radius = rad
            self._mass = m
            self._temp = temp
        else:
            raise ValueError('radius and mass should be positive values, and temp should be above -273.15')
        #Initialize the x and y coordinates
        self._x = 0
        self._y = 0
        #Create a turtle as an instance variable
        self._turtle = turtle.Turtle()
        self._turtle.shape('circle')
        self._turtle.color('yellow')
        self._turtle.goto(self._x, self._y)
        
        
    def get_mass(self):
        return self._mass
    
    def __str__(self):
        return self._name


'------------------------------------Main Code-------------------------------------------------'
#Tests for creating a legitimate sun
p1 = Sun('HTML Rulez d00d', 15, 15.5, 23.2)
print(p1)

p2 = Sun('Nickels is Money Too', 12.2, 888, -255)
print(p2)

#Test for not maintaining one of the invariants
#p3 = Sun('blah', -1, 156, -89)
#print(p3)

#p4 = Sun('Woah', 23, -5, 654654)
#print(p4)

#p5 = Sun('Poop', 23, 22.0000000000000000000008, -273.15)
#print(p5)