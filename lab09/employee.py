'''Using Python to Process Employee Salary Data
April 17, 2015
Lab 09, Exercise 1
Zach Wibbenmeyer (zdw3)'''

#Gain access to the system module
import sys

#Create a class named employee
class Employee:
    '''
    This class takes information from an employee title and organizes
    it into a nice, readable format
    '''
    
    #Initialize the line paramater
    def __init__(self, line = ''):
        '''
        This is initializing the employee titles below
        '''
        #If statement that checks if the line is an empty string and gives the variables default names
        if line == '':
            #Initialize the instance variables
            self._first = 'Tim'
            self._last = 'Sandt'
            self._rank = 'associate'
            self._salary = 20001
        #Otherwise initialize the instance variables
        else:
            strings = line.split()
            self._first = strings[0]
            self._last = strings[1]
            self._rank = strings[2]
            if float(strings[3]) > 20000:
                self._salary = float(strings[3])
            else:
                print('Please enter a salary greater than $20000', file = sys.stderr)
                sys.exit(-1)
        
    #Create the string method
    def __str__(self):
        '''
        Allows the employee title to print nicely
        '''
        #Concatenates the employee title into a readable string
        return (self._last + ', ' + self._first[0] + '.: ' + self._rank + ' ($' + str(self._salary) + ')')
    
    #Create an accessor for the rank
    def get_rank(self):
        '''Accessor for the rank'''
        return self._rank
    
    #Create an accessor for the salary
    def get_salary(self):
        '''Accessor for the salary'''
        return self._salary

'''-----------------------------------------Main Code--------------------------------------------------'''
#Initializes the tests
if __name__ == '__main__':
    
    #Tests the default parameters
    f1 = Employee()
    print(f1)
    
    #Test the accessors
    print('Employee rank: ', f1.get_rank())
    print('Employee salary: ', f1.get_salary())
    
    #Test for the updated init variables
    f2 = Employee('Mike Sandt associate 20001')
    print(f2)
    
    f3 = Employee ('Caleb Postma full 30000')
    print(f3)
    
    #Tests salary below $20000
    #f4 = Employee('Caleb Postma manager 19000')
    #print(f4)