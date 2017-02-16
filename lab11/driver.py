'''Using Python to Build a Calculator
April 24, 2015
Lab 11
Zach Wibbenmeyer (zdw3)'''

#Imports the necessary modules
from tkinter import *
from calculator import *

#Create a class named Driver
class Driver:
    
    '''
    Class that creates the calculator
    '''
    
    #Create an instance method
    def __init__(self):
        '''
        Instance method that initializes all the 
        buttons on the calculator
        '''
        #Create an instance of the Calculator
        self.calc = Calculator()
        
        #Initialize the window
        window = Tk()
        window.title('Calculator')
        #Creates a frame and attaches it to the window
        frame = Frame(window)
        frame.grid(row = 3, columnspan = 2)
        #Creates a StringVar instance variable and gives it a value of '+'
        self.operation = StringVar()
        self.operation.set('+')
        
        #Create instances of StringVar()
        self.operand1 = StringVar()
        self.operand2 = StringVar()
        
        #Adds the addition button to the left side
        add_rb = Radiobutton(frame, text="+", variable = self.operation, value = '+')
        add_rb.pack(side = LEFT)
        #Adds the subtraction button to the left side
        add_rb2 = Radiobutton(frame, text="-", variable = self.operation, value = '-')
        add_rb2.pack(side = LEFT)
        #Adds the division button to the left side
        add_rb3 = Radiobutton(frame, text="/", variable = self.operation, value = '/')
        add_rb3.pack(side = LEFT)
        #Adds the multiplication button to the left side
        add_rb4 = Radiobutton(frame, text="*", variable = self.operation, value = '*')
        add_rb4.pack(side = LEFT)
        #Create a label and entry for the first number entered
        Label(window, text = "Input 1:").grid(row = 1, sticky = E)
        operand1Entry = Entry(window, textvariable = self.operand1, width = 6)
        operand1Entry.grid(row = 1, column = 1, sticky = W)
        #Create a label and entry for the second number entered
        Label(window, text = "Input 2:").grid(row = 2, sticky = E)
        operand2Entry = Entry(window, textvariable = self.operand2, width = 6)
        operand2Entry.grid(row = 2, column = 1, sticky = W)
        #Makes sure to change the operator sign
        Label(window, text = 'Operator: ').grid(row = 3, column = 2)
        opLabel = Label(window, textvariable = self.operation, width = 3)
        opLabel.grid(row = 3, column = 3)
        
        #Create a button that performs the calculation
        Button(window, text = 'Calculation', command = self.doCalculation).grid(row = 4, column = 1)
        Label(window, text = 'Result').grid(row = 4, column = 2)
        self.result_text = StringVar()
        Label(window, textvariable = self.result_text).grid(row = 4, column = 3)
        
        #Event loop for the window
        window.mainloop()
    
    #Method that does the calculation    
    def doCalculation(self):
        '''
        This method completes the calculation
        ''' 
        result = self.calc.calculate(self.operand1.get(), self.operation.get(), self.operand2.get())
        self.result_text.set(result)

#Create an instance of Driver
Driver()