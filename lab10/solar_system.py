'''
Model of a solar system
Created Fall 2014

@author: zdw3
'''

from sun import *
from planet import *

class Solar_System:
    '''
    This class will model the solar system
    '''
    #Initialize the instance variables
    def __init__(self):
        self._sun = None
        self._planets = []
        
    #Create a method for adding the sun  
    def add_sun(self, a_sun):
        #If statement that checks the type of the sun
        if isinstance(a_sun, Sun):
            self._sun = a_sun
        else:
            raise TypeError('add_sun(): cannot add ' + str(type(a_sun)) + ' to solar system')   
    
    #Create a method for adding a planet         
    def add_planet(self, a_planet):
        #If statement that checks the type of the planet
        if isinstance(a_planet, Planet):
            self._planets.append(a_planet)
        else:
            raise TypeError('add_planet(): cannot add ' + str(type(a_planet)) + ' to solar system')
    
    #Create a method for showing the planets
    def show_planets(self):
        for a_planet in self._planets:
            print(a_planet)
        
        
'------------------------------------Main Code-----------------------------------------------------'