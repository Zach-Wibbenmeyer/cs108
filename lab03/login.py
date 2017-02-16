'''Python: Using Strings to generate a login ID
February 19, 2015
Lab 3, Exercise 1
Zach Wibbenmeyer (zdw3)'''


#Prompts the user to enter their first name
first_name = input("Please enter your first name: ")

#Prompts the user to enter their last name
last_name = input("Please enter your last name: ")

#Prompts the student to enter their id number
student_id = str(input("Please enter your student id number: "))

#Concatenates the strings together to form a login id
login = (first_name[0] + last_name[0:5] + student_id[-2:])

#Makes the login id all lowercase
login = login.lower()

#Prints the login id
print("Your login ID is:" , login)