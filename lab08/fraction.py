'''Using Python to Model Fractions
April 9, 2015
Lab 8
Zach Wibbenmeyer (zdw3)'''

#Gains access to the system module
import sys

#Compute the Greatest Common Divisor
def computeGCD(alpha, beta):
    '''
    (int, int) -> int
    This function finds the greatest common divisor of two integers, using
    Euclid’s algorithm
    '''
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while (remainder != 0):
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta

#Create an empty class 'Fraction'
class Fraction:
    
    '''Models fractions
        Invariants:
            Numerator is all real numbers
            Denominator is all real numbers except 0
            If one of the details in the invariants is false, then
            an error message is printed and the program ends '''
    
    #Create the instance variables
    def __init__(self , numerator = 0 , denominator = 1):
        
        '''This is initalizing a fraction with a numerator of 0
            and a denominator of 1'''
        
        #Checks to see if the numerator is an integer
        if (numerator % 1) == 0:
            self._numerator = numerator
        #Checks to see if the numerator is an integer
        elif (numerator % 1) != 0:
            print('Please enter integers only' , file = sys.stderr)
            sys.exit(-1) 
        else:
            #Otherwise say fraction is invalid and exit the program
            print('Unable to create invalid fraction' , file = sys.stderr)
            sys.exit(-1)
            
        #Checks to see if the denominator is an integer and it is not equal to zero
        if (denominator != 0) and ((denominator % 1) == 0):
            self._denominator = denominator
        #Checks to see if the denominator is an integer
        elif (denominator % 1) != 0:
            print('Please enter integers only' , file = sys.stderr)
            sys.exit(-1)
        #Otherwise say fraction is invalid and exit program
        else:
            print('Unable to create invalid fraction' , file = sys.stderr)
            sys.exit(-1)
        
        #This simplifies the values provided by the calling program
        self.simplify()

    #Create the string method
    def __str__(self):
        '''Allow fractions to print nicely'''
        #Concatenates the fraction together
        return ('Your fraction is' + ' ' + str(self._numerator) + '/' + str(self._denominator))
    
    #Create an accessor for the numerator
    def get_numerator(self):
        '''accessor for numerator'''
        return self._numerator
    
    #Create an accessor for the denominator
    def get_denominator(self):
        '''accessor for the denominator'''
        return self._denominator
    
    
    #Simplify the fraction
    def simplify(self):
        '''This function simplifies the fraction by creating the lowest common form of the
        fraction, and puts the negative sign (if present) on the numerator'''
        
        #Set GCD equal to the greatest common divisor of the numerator and divisor
        gcd = computeGCD(self._numerator , self._denominator)
        
        #If gcd does not equal 0
        if gcd != 0:
            #Set the numerator and denominator to be divided by gcd
            self._numerator = self._numerator//gcd
            self._denominator = self._denominator//gcd
        #If the denominator is less than 0
        elif self._denominator < 0:
            self._numerator = self._numerator * -1
            self._denominator = self._denominator * -1
            
    #Create a function for multiplying fractions together    
    def __mul__(self , other):
        '''This function takes two fractions, multiplies them together, and simplifies them'''
        
        #Create a variable for the multiplied numerator
        new_numerator = self._numerator * other.get_numerator()
        #Create a variable for the multiplied denominator
        new_denominator = self._denominator * other.get_denominator()
        #Return the new multiplied fraction
        return (Fraction(new_numerator , new_denominator)) 
        


'''-----------------------------------------Main Code--------------------------------------------'''
    
#Construct the initial fraction
f1 = Fraction()
print(f1)

#Construct a fraction for one half
f2 = Fraction(1 , 2)
print(f2)

#Construct a fraction for two thirds
f3 = Fraction(2 , 3)
print(f3)

#Test if the error message is working
#f4 = Fraction(2 , 0)
#print(f4)

#Construct a fraction for negative one third
f5 = Fraction(-1 , 3)
print(f5)


#Test the accessors
print('f1 Numerator: ' , f1.get_numerator())
print('f1 Denominator: ' , f1.get_denominator())
#f3 accessors
print('f3 Numerator: ' , f3.get_numerator())
print('f3 Denominator: ' , f3.get_denominator())

#Testing the simplify function
f6 = Fraction(2 ,4)
print(f6)

f7 = Fraction(-3 , 9)
print(f7)

#Tests the mul function
f7 = Fraction(2 , 3) * Fraction(1 , 2)
print(f7)

f8 = Fraction(-3 , 4) * Fraction(5 , 4)
print(f8)

#Tests for fractions that are not integers
#f9 = Fraction(3.5 , 4)
#print(f9)

#f10 = Fraction(3 , 4.5)
#print(f10)

#f11 = Fraction(3.5 , 4.5)
#print(f11)