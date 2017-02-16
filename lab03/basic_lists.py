''' Python: Returning lists in order
February 19, 2015
Lab 3, Exercise 2
Zach Wibbenmeyer (zdw3)'''

#Prompts the user to enter a first number
number1 = int(input("Please enter number 1: "))

#Prompts the user to enter a second number
number2 = int(input("Please enter number 2: "))

#Prompts the user to enter a third number
number3 = int(input("Please enter number 3: "))

#Prompts the user to enter a fourth number
number4 = int(input("Please enter number 4: "))

'''Algorithm:  This program will begin by asking the user for four different numbers.  The program will
then take the four numbers and compile them into a list.  Next, the program will read through the list
and pull the minimum number from the list and put it into a new list.  The number will be appended to the 
end of the list.  The lowest number that was pulled from the list will be deleted.  The program will 
continue to do this until the list that was first created is completely empty, and the new list contains 
all of the numbers in order from lowest to highest.'''


list = [number1,number2,number3,number4] #Creates a list
final_list = [] #Creates a final list that is empty

#Finds the minimum number in the list, removes it, and appends it to the new list
final_number1 = min(list)
final_list.append(final_number1)
list.remove(final_number1)

#Finds the second lowest number in the list, removes it, and appends it to the new list
final_number2 = min(list)
final_list.append(final_number2)
list.remove(final_number2)

#Finds the next lowest number in the list, removes it, and appends it to the new list
final_number3 = min(list)
final_list.append(final_number3)
list.remove(final_number3)

#Finds the final lowest number in the list, removes it, and appends it to the new list
final_number4 = min(list)
final_list.append(final_number4)
list.remove(final_number4)

#Prints the final list
print(final_list)