'''Using Python to Deal with Various User Inputed Strings
March 26, 2015
Lab 7, Exercise 1
Zach Wibbenmeyer (zdw3)'''


'''Function Definitions'''

#Defining a function for the menu
def menu():
    #Prompts the user to select a choice
    print('Please select from the following list of options (type the appropriate character): ')
    #Choice A
    print('A. Print a nice message')
    #Choice B
    print('B. Check if your SSN is valid')
    #Choice C
    print('C. Check if your password is valid')
    #
    print('D. Check if your credit card is valid')
    #Choice D
    print('Q. Quit')
    
#Function for checking if a SSN is valid or not    
def isValidSSN(ssn):
    
    #Checks if the length is 11 characters
    if len(ssn) != 11:
        return False
    #Checks if there are hyphens in the given positions
    elif not ssn[3] == '-' and ssn[6] == '-':
        return False
    
    #Removes the hyphens from the SSN
    separated_ssn = ssn.split(sep = '-')

    #Checks if the first segment is 3 digits long    
    if not len(separated_ssn[0]) == 3:
        return False
    #Checks if the first segment is all digits
    elif not separated_ssn[0].isdigit():
        return False
    #Checks if the second segment is 2 digits long
    elif not len(separated_ssn[1]) == 2:
        return False
    #Checks if the second segment is all digits
    elif not separated_ssn[1].isdigit():
        return False
    #Checks if the third segment is 4 digits long
    elif not len(separated_ssn[2]) == 4:
        return False
    #Checks if the third segment is all digits
    elif not separated_ssn[2].isdigit():
        return False
    #Otherwise, return true
    else:
        return True
    
#Function for checking for a valid password
def isValidPassword(password):
    
    #Checking to see if the length is 8 characters or greater
    if not len(password) >= 8:
        return False
    #Checking if the password is alphanumeric
    if not password.isalnum():
        return False
    #Create a variable and initialize it to 0
    digits = 0
    #For loop iterating through each character in password
    for x in password:
        #Checks to see if x is a digit
        if x.isdigit() == True:
            #Increment digits by one
            digits += 1
    #Return False if digits is not greater or equal to 2
    if not digits >= 2:
        return False
    #Otherwise return True
    else:
        return True
    
    
def isValidPrefix(credit_card):
    
    #Create a variable for the first character
    digit1 = credit_card[0]
    #If the first character equals these numbers, return true
    if digit1 == '4' or digit1 == '5' or digit1 == '6':
        return True
    #If the first character equals a 3
    elif digit1 == '3':
        #Second variable for the second character
        digit2 = credit_card[1]
        #If second character equals 7, return True
        if digit2 == '7':
            return True
    #Otherwise return False
    return False

#Create a second function
def sum_of_odds(credit_card):
    
    #Create a variable that iterates through the list
    number = credit_card[-1::-2]
    #Create total and initialize it to 0
    total = 0
    #For every character in number, increment total and change x to an integer
    for x in number:
        total += int(x)
    return total

#Create a third function
def sum_of_double_evens(credit_card):
    
    #Create a variable that iterates through the list
    number = credit_card[-2::-2]
    #Create an empty list
    list = []
    #For loop for every character in number
    for x in number:
        #Create a variable that changes x to an integer and multiplies it by 2
        num1 = int(x)*2
        if num1 > 9:
            #Get the first number
            digit1 = num1//10
            #Get the second number
            digit2 = num1%10
            #Update num1 by adding the two digits together
            num1 = digit1 + digit2
        #Append num1 to the list
        list.append(num1)
    return sum(list)

#Create a third function
def isValidCC(credit_card):
    
    #Check first if they are all digits
    if credit_card.isdigit():
        if isValidPrefix(credit_card) and (13 <= len(credit_card) <= 16):
            #Create a variable for the odds
            odds = sum_of_odds(credit_card)
            #Create a variable for the evens
            evens = sum_of_double_evens(credit_card)
            #If odds +evens is divisible by 10, return True
            if ((odds + evens) % 10) == 0:
                return True
    #Otherwise, return False
    return False

'''Main Program Code'''
    
#Calls the menu function    
menu()
#Prompts the user to enter a choice
user_choice = str(input('Choice: '))

#Forever while loop
while True:
    #If user choice is A
    if user_choice.upper() == 'A':
        print('Have a great day!')
        menu()
        user_choice = str(input('Choice: '))
    #If user choice is Q
    elif user_choice.upper() == 'Q':
        print('Good-bye!')
        break
    #If user_choice is B
    elif user_choice.upper() == 'B':
        #Prompts the user to enter a SSN
        print("Let's Validate your Social Security Number")
        ssn = input('Please enter your SSN: ')
        #Assign the function to a variable
        valid = isValidSSN(ssn)
        #If variable is false, say this is not a valid SSN
        if valid == False:
            print('This is not a valid SSN')
            menu()
            user_choice = str(input('Choice: '))
        #Otherwise say this is a valid SSN
        else:
            print('This is a valid SSN')
            menu()
            user_choice = str(input('Choice: '))
    #If user_choice is C
    elif user_choice.upper() == 'C':
        #Prompts the user to enter a password
        print('Password Validation')
        password = input('Please enter a password: ')
        #Assign the function to a variable
        valid2 = isValidPassword(password)
        #If variable is false, say this is not a valid password
        if valid2 == False:
            print('This is not a valid password')
            menu()
            user_choice = str(input('Choice: '))
        #otherwise, say this is a valid password
        else:
            print('This is a valid password')
            menu()
            user_choice = str(input('Choice: '))
    #If user chooses D
    elif user_choice.upper() == 'D':
        #Prompts the user to enter a valid Prefix
        print('Credit Validation')
        credit_card = input('Please enter a credit card number: ')
        valid3 = isValidCC(credit_card)
        if valid3 == False:
            print('This is not a valid credit card')
            menu()
            user_choice = str(input('Choice: '))
        else:
            print('This is a valid credit card')
            menu()
            user_choice = str(input('Choice: '))
    #If user choice is anything else
    else:
        print("I'm sorry, that is not a valid option.")
        user_choice = str(input('Choice: '))