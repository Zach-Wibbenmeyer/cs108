''' A math problem using Python
February 12, 2015
Zach Wibbenmeyer (zdw3)'''

#Prompts the user to enter a 3 digit number, with the last two digits differing by at least 2
number = int(input("Enter a 3 digit number where the last 2 digits differ by at least 2: "))

#Isolates each digit of the number the user entered
rev_number1 = number % 10
rev_number2 = (number//10)%10
rev_number3 = (number//100)%10

#Takes the isolated numbers and concatenates them into an integer that is the reverse of the number
rev_number = int(str(rev_number1) + str(rev_number2) + str(rev_number3))

#Takes the difference of the number and the reverse of the number
difference = abs(number - rev_number)

#Isolates each number of the difference
difference1 = difference % 10
difference2 = (difference//10) % 10
difference3 = (difference//100) % 10

#Takes the isolated numbers of the difference and concatenates them into the reverse
rev_diff = int(str(difference1) + str(difference2) + str(difference3))

#Prints the sum of the difference and the reverse of the difference
print(difference + rev_diff)
