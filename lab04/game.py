'''Using Python to Play Rock Paper Scissors
February 26, 2015
Lab 4, Project 3
Zach Wibbenmeyer (zdw3)'''

#Gains access to the random module
import random

#Prompts the user to play either rock, paper, or scissors
user_choice = int(input('Enter 0 for rock, 1 for paper, or 2 for scissors: '))

#Creates a variable that calculates the computer's choice
computer_choice = random.randint(0,2)

#User chooses rock
if user_choice == 0:
    #If computer chooses paper, the computer wins
    if computer_choice == 1:
        print('The computer chooses paper!')
        print('Computer wins!')
    #If computer chooses scissors, the user wins
    elif computer_choice == 2:
        print('The computer chooses scissors!')
        print('You win!')
    #If computer chooses rock, it is a draw
    else:
        print('The computer chooses rock!')
        print('It is a draw!')
#If the user chooses paper
elif user_choice == 1:
    #If the computer chooses 2, computer wins
    if computer_choice == 2:
        print('The computer chooses scissors!')
        print('Computer wins!')
    #If computer chooses rock, user wins
    elif computer_choice == 0:
        print('The computer chooses rock!')
        print('You win!')
    #If computer chooses paper, it is a draw
    else:
        print('The computer chooses paper!')
        print('It is a draw!')
#If user chooses scissors
elif user_choice == 2:
    #If computer chooses rock, computer wins
    if computer_choice == 0:
        print('The computer chooses rock!')
        print('Computer wins!')
    #If computer chooses paper, user wins
    elif computer_choice == 1:
        print('The computer chooses paper!')
        print('You win!')
    #If computer chooses scissors, it is a draw
    else:
        print('The computer chooses scissors!')
        print('It is a draw!')