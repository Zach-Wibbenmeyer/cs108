'''Using Python to Import the Employee Class
April 17, 2015
Lab 09, Exercise 2
Zach Wibbenmeyer (zdw3)'''

#Gain access to the class Employee from the employee file
from employee import Employee

#Create an empty list
employees = []
#For loop that iterates through each line in the Salary text file
with open('Salary.txt') as file:
    for line in file:
        #Appends an employee to the list of employees
        employees.append(Employee(line))
    #Prints the length of the list employees
    print('The number of employees is', len(employees), 'employees' + '\n')
    
#If statement that checks if the list of employees is empty
if len(employees) < 1:
    print('There are no employees in the list')
#Otherwise do all of the next steps
else:
    #Create two empty dictionaries
    totals = {}
    counts = {}
    #Create two variables and set them equal to the first employee in list of employees
    max_employee = employees[0]
    min_employee = employees[0]
    #For loop that iterates through each element in employees
    for x in employees:
        #If rank is in totals
        if (x.get_rank() in totals):
            #Increment the value for that rank by the current employee salary in the totals dictionary
            totals[x.get_rank()] += x.get_salary()
            #Increment the count for that rank by 1 in the counts dictionary
            counts[x.get_rank()] += 1
        else:
            #Add a key value pair in the rank for the current employee salary in the totals dictionary
            totals[x.get_rank()] = x.get_salary()
            #Add a key value pair for the rank and set the counts dictionary equal to 1
            counts[x.get_rank()] = 1
        #If the current salary is greater than the variable max_employee
        if x.get_salary() > max_employee.get_salary():
            #Update max_employee
            max_employee = x
        #If the current salary is less than the variable min_employee
        if x.get_salary() < min_employee.get_salary():
            #Update min_employee
            min_employee = x
            
#Create a function that computes the average salary by rank
def print_averages(totals, counts, outFile):
    '''
    Function is used to compute the average salary of all the employees
    '''
    #Write the file heading
    outFile.write('Rank\tAverage Salary\n')
    #For loop iterating through totals
    print('The average salaries are: ' + '\n')
    for rank in totals:
        #Compute the average salary
        average_salary = totals[rank]/counts[rank]
        #Write the average salaries in a readable format
        outFile.write(rank + '\t' + str(average_salary) + '\n')
        print(rank + ': \t' + '$' + str(average_salary) + '\n')
    
'-------------------------------------------Main Code--------------------------------------------------'
#Opens up a txt file
with open('employee_stats.txt', 'w') as file:
    #Writes the employee with the highest salary on the txt file
    file.write('The employee with the highest salary is ' + str(max_employee) + '\n')
    #Writes the employee with the smallest salary on the txt file
    file.write('The employee with the smallest salary is ' + str(min_employee) + '\n')
    #Prints the information to the txt file
    print_averages(totals, counts, file) 