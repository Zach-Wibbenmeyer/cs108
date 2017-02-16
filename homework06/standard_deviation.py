'''Using Python to compute the standard deviation
March 25, 2015
Homework 6
Zach Wibbenmeyer (zdw3)'''


#Create a function values with one parameter
def standard_deviation(values):
    
    #Create a variable that calculates the mean of the function
    mean = (sum(values))/(len(values))
    
    #Create a variable and initalize it to zero
    discriminant = 0
    #For loop iterating for each thing in value
    for x in values:
        discriminant = discriminant + (x - mean)**2
    discriminant = discriminant / (len(values))
    
    #Returns the square root of the discriminant
    return (discriminant)**.5

    #Prints the discriminant
    print(discriminant)

#Create an empty list
list = []

print('Enter a list of numbers. Enter 0 to stop: ')
#Forever while loop
while True:
    #Prompt the user to enter a list of numbers
    x = float(input())
    #Prompts the user to enter more numbers if they enter 0 first
    if x == 0 and list == []:
        print('Please enter at least one value: ')
    #If 0 is entered, then break
    elif x == 0:
        break
    #Appends x to the list
    else:
        list.append(x)

#Prints the list
print('The list you entered is' , list)
#Prints the standard deviation
print('The standard deviation of the list is' , standard_deviation(list))