'''Using Python to find the perfect divisors of a positive integer
March 5, 2015
Lab05, Exercise 1
Zach Wibbenmeyer (zdw3)'''

#Variable that counts the numbers of perfects found initialized to 0
perfect_found = 0

#For loop from 2 to 10000
for value in range(2,10000):
    #Initializes variable low to be 1
    low = 1
    #Initializes variable high to be equal to value
    high = value
    #Initializes variable divisors to be an empty list
    divisors = []
    #Initializes the variable perfect found to 0
    
    
    #while loop checking if low is less than high
    while low < high:
        #If statement checking if low is a divisor of value
        if (value % low) == 0:
            high = value // low
            divisors.append(low)
            #If statement checking if high is not equal to low
            if high != low:
                divisors.append(high)
        #Increments low by 1
        low += 1
    
        
    #Removes value from the list of divisors        
    divisors.remove(value) 
    
    #If statement checking to see if the sum adds up to the value entered
    if sum(divisors) == value:
        print(value , 'is a perfect number.\n')
        #Increments variable by 1
        perfect_found += 1
    
    #If statement checking to see if variable = 4. If it does, we break out of the code
    if perfect_found == 4:
            break
        
#Prints a final concluding statement        
print('These are all the perfect numbers less than 10000')