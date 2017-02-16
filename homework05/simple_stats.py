'''Using Python to compute simple stats
March 11, 2015
Homework 5
Zach Wibbenmeyer (zdw3)'''

#Creates an empty list
list = []
#Creates a variable named positive and initializes it to 0
positive = 0
#Creates a variable named negative and initializes it to 0
negative = 0
#Initializes a print statement
print("Enter as many int values as you'd like (the program exits if the input is 0): ")

#While statement for if everything is true
while True:

    #Prompts the user to enter int values
    values = int(input())
    #Exits the program if 0 is entered
    if values == 0:
        break
    #Appends values to the list if numbers greater than 0 are entered
    elif values > 0:
        list.append(values)
        #Increments the amount of positive numbers
        positive += 1
    #Appends values to the list if numbers less than 0 are entered
    elif values < 0:
        list.append(values)
        #Increments the amount of negative numbers
        negative += 1

#Computes the average of the list
average = (sum(list)) / (len(list))

#Prints the list
print(list)
#Prints the positive numbers of the list0        
print('The number of positives is' , positive)
#Prints the negative numbers of the list
print('The number of negatives is' , negative)
#Prints the total of the list
print('The total is' , sum(list))
#Prints the average of the list
print('The average is' , average)