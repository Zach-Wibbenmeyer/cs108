'''Using Python to Calculate Loans
April 29, 2015
Homework 11
Zach Wibbenmeyer (zdw3)'''

#Gain access to the necessary modules
from tkinter import *
from loan import *
import sys

#Create a class
class Driver:
    '''
    This class will create the GUI
    '''
    
    #Create an instance method
    def __init__(self):
        '''
        This method will initialize all of the buttons on the GUI
        '''
        #Create an instance of the Loan Calculator
        self.calc = Loan_Calculator()
        
        #Create the window
        window = Tk()
        window.title('Loan Calculator')
        
        #Create instances of StringVar()
        self.operand1 = StringVar()
        self.operand2 = StringVar()
        self.operand3 = StringVar()
        
        #Create an entry for the length
        Label(window, text = 'Length (years):').grid(row = 1, sticky = E)
        operand1Entry = Entry(window, textvariable = self.operand1, width = 15)
        operand1Entry.grid(row = 1, column = 1, sticky = W)
        #Create an entry for the initial loan amount
        Label(window, text = 'Initial Loan:').grid(row = 2, sticky = E)
        operand2Entry = Entry(window, textvariable = self.operand2, width = 15)
        operand2Entry.grid(row = 2, column = 1, sticky = W)
        #Create an entry for the annual interest
        Label(window, text = 'Annual Interest:').grid(row = 3, sticky = E)
        operand3Entry = Entry(window, textvariable = self.operand3, width = 15)
        operand3Entry.grid(row = 3, column = 1, sticky = W)
        
        #Create a button for the result
        Button(window, text = 'Calculate', command = self.doCalculation).grid(row = 4, column = 1)
        Label(window, text = 'Result').grid(row = 4, column = 2)
        self.result_text = StringVar()
        Label(window, textvariable = self.result_text).grid(row = 4, column = 3)
        
        #Event loop for the window
        window.mainloop()
        
    #Create a method for the calculation    
    def doCalculation(self):
        '''
        This method will complete the calculation
        '''
        try:    
            result = self.calc.calculation(float(self.operand1.get()), float(self.operand2.get()), float(self.operand3.get()))
        except ValueError as e:
            print(e, file = sys.stderr)
            
        self.result_text.set(result)
        
#Create an instance of the driver        
Driver()
