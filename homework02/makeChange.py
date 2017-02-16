'''Using Python to compute the amount of change given in a transaction
February 16, 2015
Homework # 2
Zach Wibbenmeyer (zdw3)'''

#Prompts the user to enter a cost that is not greater than $100
charge = int(input("Please enter the amount charged for the transaction that is not greater than $100: "))

#Prompts the user to enter the amound paid for the transaction
amount_paid = int(input("Please enter the amount paid (Must be a whole number, and not greater than $100): "))

#Calculates the difference between the amound paid and the transaction
diff = amount_paid - charge
print("Change is $",diff, end = ": ")


diff_20 = int(diff // 20) #Calculates the number of $20 to give back in change
diff = diff - (diff_20*20) #Subracts the number of $20 from the difference and creates a new difference

diff_10 = int(diff // 10) #Calculates the number of $10 to give back in change
diff = diff - (diff_10*10) #Subtracts the number of $10 from the difference and updates the difference


diff_5 = int(diff // 5) #Calculates the number of $5 to give back in change
diff = diff - (diff_5*5) #Subtracts the number of $5 from the difference and updates the difference


diff_1 = int(diff // 1) #Calculates the number of $1 to give back in change
diff = diff - (diff_1) #Subtracts the number of $1 from the difference and updates the difference


#Prints the amount of change that is given back
print(diff_20,"20(s),",diff_10,"10(s),",diff_5,"5(s),","and", diff_1,"1(s),")


