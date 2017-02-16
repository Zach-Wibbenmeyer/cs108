'''Using Python to Simulate the Game War
April 15, 2015
Homework 8
Zach Wibbenmeyer (zdw3)'''

#Gains access to the random module
import random
#Gains access to the system module
import sys
#Create a list of the suits of the cards
suits_of_cards = ['S', 'H', 'C', 'D']

#Create the class for the war game
class PlayingCards:
    
    '''
    Constructor
    Models the card game War
    Each card will have a number between 2 and 14
    Each card will have one of four suites
    '''
    
    #Initalize all the parameters
    def __init__(self, number = 14, suit = 'S'):
    
        '''Instance variables for different kinds of cards'''
        
        #If statement constraining the number on the cards
        if 2 <= number <= 14:
            self._number = number
        #Otherwise print an error and exit the system
        else:
            print('Please enter a valid number for the cards', file = sys.stderr)
            sys.exit(-1)
        #If statement that constrains the suit on the cards    
        if suit in suits_of_cards:
            self._suit = suit
        #Otherwise print an error and exit the system
        else:
            print('Please enter a valid suit', file = sys.stderr)
            sys.exit(-1)
        
    #Create a function to access the number    
    def get_number(self):
        '''Accessor for the number on the cards'''
        return self._number
    
    #Create a function to access the suit
    def get_suit(self):
        '''Accessor for the suit on the cards'''
        return self._suit
    
    #Create a function that prints out the cards in a string 
    def __str__(self):
        '''Allows the cards to print nicely'''
        
        #If statements that assign values to each numbered card
        if self._number == 11:
            return 'J' + self._suit
        elif self._number == 12:
            return 'Q' + self._suit
        elif self._number == 13:
            return 'K' + self._suit
        elif self._number == 14:
            return 'A' + self._suit
        else:
            return str(self._number) + self._suit
        
    #Create a function for greater than
    def __gt__(self, other):
        '''Overload the operator for greater than'''
        
        #If statement to compare self being greater than other
        if self._number > other.get_number():
            return True
        else:
            return False
        
    #Create a function for less than    
    def __lt__(self, other):
        '''Overload the operator for less than'''
        
        #If statement to compare self being less than other
        if self._number < other.get_number():
            return True
        else:
            return False
        
    #Create a function for equal to   
    def __eq__(self, other):
        '''Overload the operator for equal'''
        
        #If statement to compare self being equal to other
        if self._number == other.get_number():
            return True
        else:
            return False
        
#This function will generate a random card    
def RandomHand(count = 1):
    '''Generates a random hand for a player'''

    #Establish an empty list
    list = []
    #For loop that iterates through count   
    for x in range(count):
        #Create a variable that randomizes the number and the suit on the cards
        playing_hand = PlayingCards(random.randint(2, 14), random.choice(suits_of_cards))
        #Append the hand to the empty list and turn it into a string
        list.append(playing_hand)
    return list
        
        
'''--------------------------------Main Code------------------------------------------------'''
'''
The initial tests were commented out in order to only show the war game
'''
#Tests for the base parameters        
#hand1 = PlayingCards()
#print(hand1)

#Test for Jack and different suit
#hand2 = PlayingCards(11, 'C')
#print(hand2)

#Test for numbers below 11 and a different suit
#hand3 = PlayingCards(7, 'D')
#print(hand3)

#Tests the accessors
#print('hand3 number: ', hand3.get_number())
#print('hand3 suit: ', hand3.get_suit())

#Initialize a variable to 5
SIZE_OF_HAND = 5
#Generates two random hands
player_one_hand = RandomHand(SIZE_OF_HAND)
player_two_hand = RandomHand(SIZE_OF_HAND)
#First for loop that prints player one's random hand
print('Player one plays: ', end = ' ')
for x in player_one_hand:
    print(x, end = ' ')
#Second for loop that prints player two's random hand
print('\nPlayer two plays: ', end = ' ')
for x in player_two_hand:
    print(x, end = ' ')
#print("Player one's hand: ", player_one_hand)
#print("Player two's hand: ", player_two_hand)

#Create two variables and initialize them to 0
player_one_points = 0
player_two_points = 0
#For loop that iterates through the length of the first playing hand
for i in range(len(player_one_hand)):
    #If statement that adds to player one score if player one hand is greater
   
    if player_one_hand[i] > player_two_hand[i]:
        print('\nPlayer 1 gets a point!')
        player_one_points += 1
    #Else if statement that adds to the player two score if player one hand is less
    elif player_one_hand[i] < player_two_hand[i]:
        print('\nPlayer 2 gets a point')
        player_two_points += 1
    #Otherwise it is a tie if the cards have the same number
    elif player_one_hand[i] == player_two_hand[i]:
        print('\nNo points for either players')
        
#Print the final score of the game        
print('\nFinal Score')
print('\nPlayer 1: ', player_one_points)
print('Player 2: ', player_two_points)

#If statement that says player one wins if player one points are greater
if player_one_points > player_two_points:
    print('\nPlayer 1 wins!')
#Says player two wins if player one points are less
elif player_one_points < player_two_points:
    print('\nPlayer 2 wins!')
#Otherwise it is a tie if the points are equal to each other
else:
    print('\nIt is a draw!')