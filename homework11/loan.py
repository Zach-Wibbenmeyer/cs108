'''Using Python to Calculate Loans
April 29, 2015
Homework 11
Zach Wibbenmeyer (zdw3)'''

#Gain access to the system module
import sys

#Create a new class
class Loan_Calculator:
    '''
    This class will perform the basic loan calculations
    '''
    
    #Define the instance variables
    def __init__(self, length = 1, initial_loan = 1, annual_interest = 1):
        '''
        This method will constrain the instance variables
        '''
        self._length = length
        self._intial_loan = initial_loan
        self._annual_interest = annual_interest

    #Create a mutator for the length
    def set_length(self, other):
        '''This mutator allows the length to change'''
        self._length = other
        
    #Create a mutator for the initial loan
    def set_initial_loan(self, other):
        '''This mutator allows the initial loan amount to change'''
        self._initial_loan = other
        
    #Create a mutator for the annual interest    
    def set_annual_interest(self, other):
        '''This mutator allows the annual interest ammount to change'''
        self._annual_interest = other
        
    #Create a method for the calculation    
    def calculation(self, length, initial_loan, annual_interest):
        '''
        This method will do the calculation
        ''' 
        #Raise exceptions if the values are less than 1       
        if length < 1:
            raise ValueError('Length must be positive: {}'.format(length))
        elif initial_loan < 1:
            raise ValueError('Initial Loan must be positive: {}'.format(initial_loan))
        elif annual_interest < 1:
            raise ValueError('Annual Interest must be positive: {}'.format(annual_interest))
        
        #Perform the calculation
        n = length * 12
        i = annual_interest / 100 / 12
        D = (((1 + i)**n)- 1) / (i * (1 + i)**n)
        monthlyPayment = initial_loan / D
        return float(monthlyPayment)