'''
Model a single particle
May 1, 2015
Lab 12
Zach Wibbenmeyer (zdw3)
'''

#Gain access to the tkinter module
#from tkinter import *

#Create a class named Particle
class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas
    '''
    #Initialize the functions
    def __init__(self, x = 50, y = 50, velX = 10, velY = 15, radius = 15, color = '#663977'):
        '''
        Constructor
        '''
        
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = color
        
    #Create an accessor called get_x  
    def get_x(self):
        '''accessor for the x-coordinate'''
        return self._x
    
    #Create an accessor called get_y
    def get_y(self):
        '''accessor for the y-coordinate'''
        return self._y
    
    #Create an accessor called get_radius
    def get_radius(self):
        '''accessor for the radius of the particle'''
        return self._radius
        
    #Create an instance method for receiving a canvas
    def render(self, canvas):
        '''
        Instance method that receives a canvas
        '''
        #Creates a canvas
        canvas.create_oval(self._x - self._radius,
                        self._y - self._radius,
                        self._x + self._radius,
                        self._y + self._radius,
                        fill = self._color)
        
    #Create an instance method and call it move   
    def move(self, canvas):
        '''
        This instance method will allow the particle to move on the canvas
        '''
        #Update the x and y coordinates
        self._x += self._velX
        self._y += self._velY
        
        #If statement that negates the x velocity if all this
        if ((self._x + self._radius) > (canvas.winfo_reqwidth())) or ((self._x - self._radius) < 0):
            self._velX = -self._velX
        if ((self._y + self._radius) > (canvas.winfo_reqwidth())) or ((self._y - self._radius) < 0):
            self._velY = -self._velY
        
    
        