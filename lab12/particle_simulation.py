'''
GUI controller for a particle simulation
May 1, 2015
Lab 12
Zach Wibbenmeyer (zdw3)
'''

from tkinter import *
from random import randint
from particle import *
from helpers import *

#Create a class named ParticleSimulation
class ParticleSimulation:
    '''
    This class will simulate a particle
    '''
    #Create the instance variables
    def __init__(self):
        self.window = Tk()
        self.window.title("Particle Simulation")
        self.window.protocol('WM_DELETE_WINDOW', self.exitClean)
        self.width = 400
        self.canvas = Canvas(self.window, bg='black',
                        width = self.width, height = self.width)
        self.canvas.pack()
        
        #Create a default number of particle
        self.p_list = []
        self.terminate = False
        
        #Adds a button to add more particles
        self.add_button = Button(self.window, text = 'Add particle', command = self.addParticle)
        self.add_button.pack()
        
        self.canvas.bind('<Button-1>', self.checkRemoveParticle)
        
        #Animate the particle
        self.animate()
        self.window.mainloop()
    
    #Create a method and call it exitClean     
    def exitClean(self):
        self.terminate = True
        self.window.destroy()
        
    #Create a method and call it animate
    def animate(self):
        '''
        This method will animate the particles
        '''
        #While the program has not been terminated, move the particle
        while self.terminate == False:
            self.canvas.delete(ALL)
            for x in self.p_list:
                x.move(self.canvas)
                x.render(self.canvas)
            self.canvas.after(50)
            self.canvas.update()
            
    #Create an instance method and name it addParticle
    def addParticle(self):
        '''
        This method will create a random particle
        and append it to the particle list
        '''
        #Adds random sizes and positions of particles and appends it to the list
        add_particle = Particle(randint(0, self.width), randint(0, self.width),
                        randint(-25, 25), randint(-25, 25), randint(15, 25), getRandomColor())
        self.p_list.append(add_particle)
        
    #Create a method and call it checkRemoveParticle    
    def checkRemoveParticle(self, event):
        '''
        This method will allow the user to remove a particle
        with the click of the mouse
        '''
        #Makes a copy of the list
        copy = self.p_list[:]
        
        #For loop iterating through each particle in the copy of the list
        for particle1 in copy:
            #If dist is less than radius, then remove the particle from the original list
            if distance(event.x, event.y, particle1.get_x(), particle1.get_y()) < particle1.get_radius():
                self.p_list.remove(particle1)
        
#Call the class
ParticleSimulation()