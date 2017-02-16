'''Using Python to Calculate the Day of the Week
February 26, 2015
Lab 4, Project 2
Zach Wibbenmeyer (zdw3)'''

#Prompts the user to enter the year
year = int(input('Please enter the year in numerical format: '))
#Prompts the user to enter the month
month = int(input('Please enter the month of the year in numerical format: '))
#Prompts the user to enter the day
day = int(input('Please enter the day of the month in numerical format: '))

#Sets restrictions for the month
if (month == 1) or (month == 2):
    month = month + 12
    year = year - 1

#Creates a variable named century
century = year//100
#Creates a variable named year_of_century
year_of_century = year % 100
    
#Calculates the day of the week
day_of_week = (day + (((month + 1) * 26)//10) + year_of_century + ((year_of_century)//4) + (century//4) + (5 * century)) % 7

#Creates a list full of the days of the week
list = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

#Prints the day of the week
print('The day of the week is' , list[int(day_of_week)])