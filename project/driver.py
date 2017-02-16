'''
Using Python to Module the Game Yahtzee
May 19, 2015
Zach Wibbenmeyer (zdw3)
'''

#Gain access to the necessary modules
from tkinter import *
from random import *

#Create a global variable for the number of rolls and used_scores
roll_number = 0
used_scores = []

#Create a class and call it Yahtzee
class Yahtzee:
    '''
    This class will create a GUI that
    will model the game Yahtzee
    '''
    
    #Start to create the GUI
    def __init__(self):
        '''
        This will create the basic GUI
        '''
         #Create the window and title it Yahtzee!
        window = Tk()
        window.title('Yahtzee!')
        #Create a frame
        frame = Frame(window, width = 500, height = 500 )
        frame.pack()
        
        #Create the roll button       
        self._roll = Button(frame, command = self.roll_die, text = 'Roll', width = 5).grid(row = 1, column = 8)
        self._stop = False
        
        #Create the label for the first die
        die1_label = Label(frame, text = 'Die 1').grid(row = 1, column = 1)
        #Create an updated label for the first die
        #Credit goes to Joel Stehouwer for the Intvar()
        self._roll1 = IntVar()
        die1 = Label(frame, textvariable = self._roll1).grid(row = 2, column = 1)

        #Create a keep button for the first die
        self._die1_keep = Button(frame, command = self.keep_die1, text = 'Keep', width = 5)
        self._die1_keep.grid(row = 3, column = 1)
        self._keep1 = False
        
        #Create the label for the second die
        die2_label = Label(frame, text = 'Die 2').grid(row = 1, column = 2)
        #Create an updated label for the second die
        self._roll2 = IntVar()
        die2 = Label(frame, textvariable = self._roll2).grid(row = 2, column = 2)
        
        #Create a keep button for the second die
        self._die2_keep = Button(frame, command = self.keep_die2, text = 'Keep', width = 5)
        self._die2_keep.grid(row = 3, column = 2)
        self._keep2 = False
        
        #Create the label for the third die
        die3_label = Label(frame, text = 'Die 3').grid(row = 1, column = 3)
        #Create an updated label for the third die
        self._roll3 = IntVar()
        die3 = Label(frame, textvariable = self._roll3).grid(row = 2, column = 3)
        
        #Create a keep button for the third die
        self._die3_keep = Button(frame, command = self.keep_die3, text = 'Keep', width = 5)
        self._die3_keep.grid(row = 3, column = 3)
        self._keep3 = False
        #Create the label for the fourth die
        die4 = Label(frame, text = 'Die 4').grid(row = 1, column = 4)
        #Create an updated label for the third die
        self._roll4 = IntVar()
        die4 = Label(frame, textvariable = self._roll4).grid(row = 2, column = 4)
        
        #Create a keep button for the fourth die
        self._die4_keep = Button(frame, command = self.keep_die4, text = 'Keep', width = 5)
        self._die4_keep.grid(row = 3, column = 4)
        self._keep4 = False
        
        #Create the label for the fifth die
        die5_label = Label(frame, text = 'Die 5').grid(row = 1, column = 5)
        #Create an updated label for the fifth die
        self._roll5 = IntVar()
        die5 = Label(frame, textvariable = self._roll5).grid(row = 2, column = 5)
        
        #Create a keep button for the fifth die
        self._die5_keep = Button(frame, command = self.keep_die5, text = 'Keep', width = 5)
        self._die5_keep.grid(row = 3, column = 5)
        self._keep5 = False
        
        #Create a label for the listbox
        list_label = Label(frame, text = 'Score as: ').grid(row = 4, column = 1)
        
        #Create a list of the different scoring tactics
        #The credit for the term global is attributed to Joel Stehouwer
        global list_scores
        list_scores = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a kind', '4 of a kind', 
                       'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance']
        
        #Create the list box and append all the scoring tactics
        #Joel Stehouwer helped me create the listbox and everything that goes with it (including selection.curselection()[0]
        #The website I used for the listbox is http://www.tutorialspoint.com/python/tk_listbox.htm
        #And the website http://effbot.org/tkinterbook/widget.htm
        global selection
        #Creates the listbox
        selection = Listbox(frame, selectmode = 'single', exportselection = False)
        #Appends the choices to the listbox
        for x in range(0, len(list_scores)):
            selection.insert(x, list_scores[x])
        selection.grid(row = 5, column = 1)
        selection.activate(0)
                
        #Scrollbar credit comes from the website http://effbot.org/tkinterbook/listbox.htm
        scrollbar = Scrollbar(frame, orient = VERTICAL)
        scrollbar.config(command = selection.yview)
        scrollbar.grid(row = 5, column = 2)
        
        
        #Create a score button
        #Credit for the definition term lambda is attributed to Joel Stehouwer
        score_button = Button(frame, command = lambda: self.score_dice(selection.curselection()[0], True), text = 'Score:', width = 5)
        score_button.grid(row = 5, column = 3)
        
        #Create a button for testing the score
        score_test = Button(frame, command = lambda: self.score_dice(selection.curselection()[0], False), text = 'Score Test', width = 8)
        score_test.grid(row = 6, column = 3)
        
        #Create a label for the test score
        #Credit for IntVar() is attributed to Joel Stehouwer
        self._score_test = IntVar()
        test = Label(frame, textvariable = self._score_test).grid(row = 6, column = 4)
        
        #Create a label for the final score
        self._score = IntVar()
        final_score = Label(frame, textvariable = self._score).grid(row = 5, column = 4)
        
        #Create a label for printing a message
        self._print = StringVar()
        message = Label(frame, textvariable = self._print).grid(row = 5, column = 5)
        
        #Event loop the window
        window.mainloop()
        
    #Create a function that will model the die  
    def roll_die(self):
        '''This method will produce random rolls for the five die'''
        global roll_number
        if 0 <= roll_number < 3:
            if self._keep1 == False:
                self._roll1.set(randint(1,6))
            if self._keep2 == False:
                self._roll2.set(randint(1,6))
            if self._keep3 == False:
                self._roll3.set(randint(1,6))
            if self._keep4 == False:
                self._roll4.set(randint(1,6))
            if self._keep5 == False:
                self._roll5.set(randint(1,6))
            roll_number += 1
        
    #Create a function for keeping the first die
    def keep_die1(self):
        '''This method will allow the user to keep the first die'''
        self._keep1 = not self._keep1
        
    #Create a function for keeping the second die
    def keep_die2(self):
        '''This method will allow the user to keep the second die'''
        self._keep2 = not self._keep2 
        
    #Create a function for keeping the third die
    def keep_die3(self):
        '''This method will allow the user to keep the third die'''
        self._keep3 = not self._keep3
        
    #Create a function for keeping the fourth die
    def keep_die4(self):
        '''This method will allow the user to keep the fourth die'''
        self._keep4 = not self._keep4
        
    #Create a function for keeping the fifth die
    def keep_die5(self):
        '''This method will allow the user to keep the fifth die'''
        self._keep5 = not self._keep5
    
    #Create a function for the scoring tactics in the list box
    def score_dice(self, user_choice, refresh):
        '''This function will model the different scoring tactics in the game'''
        #Globalize variables
        global roll_number, selection
        global final_scores, list_scores
        #Checking if the user has already selected a choice
        if self.check(user_choice):
            self._print.set('You have already selected this item!')
            collect = False
            refresh = False
            return
    
        choice = selection.curselection()[0] #Credit goes to Joel and the website http://www.tutorialspoint.com/python/tk_listbox.htm
        #Create a variable result and set it to 0
        result = 0
        #Create a list that contains the die rolls
        die_rolls = [self._roll1.get(), self._roll2.get(), self._roll3.get(), self._roll4.get(), self._roll5.get()]
        #Set collect to false
        collect = False
        #If statement for the scores aces through sixes
        if 0 <= choice <= 5:
            collect = True
            #For loop that iterates through the list
            for i in die_rolls:
                if i-1 == choice:
                    #Increment the result by the die you roll
                    result += i
        #If the choice in the listbox is 3 of a kind
        elif choice == 6:
            rolls = self.how_many(die_rolls)
            for x in rolls:
                if x >= 3:
                    collect = True
            if collect == True:
                for x in die_rolls:
                    result += x
        #If the choice is 4 of a kind
        elif choice == 7:
            rolls = self.how_many(die_rolls)
            for x in rolls:
                if x >= 4:
                    collect = True
            if collect == True:
                for x in die_rolls:
                    result += x
        #If the choice is full house
        elif choice == 8:
            rolls = self.how_many(die_rolls)
            for x in rolls:
                for y in rolls:
                    if (x == 2 and y == 3) or (x == 3 and y == 2):
                        collect = True
            if collect == True:
                result += 25
        #If the choice is small straight
        elif choice == 9:
            rolls = self.small_straight(die_rolls)
            if rolls == True:
                collect = True
            if collect == True:
                result += 30
        #If the choice is large straight
        elif choice == 10:
            rolls = self.large_straight(die_rolls)
            if rolls == True:
                collect = True
            if collect == True:
                result += 40
        #If choice is Yahtzee
        elif choice == 11:
            rolls = self.how_many(die_rolls)
            for x in rolls:
                if x == 5:
                    collect = True
            if collect == True:
                result += 50
        #If the choice is chance
        elif choice == 12:
            collect = True
            for x in die_rolls:
                result += x
        #If refresh is true
        if refresh:
            #If you are able to collect
            if collect:
                #Add the score to the final score
                self._score.set(self._score.get() + result)
            #Set the die back to 0
            self._roll1.set(0)
            self._roll2.set(0)
            self._roll3.set(0)
            self._roll4.set(0)
            self._roll5.set(0)
            #Set the keep buttons back to 0
            self._keep1 = False
            self._keep2 = False
            self._keep3 = False
            self._keep4 = False
            self._keep5 = False
            #Set the rolls back to 0
            roll_number = 0
            #Set the score test back to 0
            self._score_test.set(0)
            
            #Globalize used_scores
            global used_scores
            used_scores.append(list_scores[choice])
            used_scores.append(choice)
            self._print.set('')
        else:
            if collect:
                #Adds up the score
                self._score_test.set(self._score.get() + result)
        #Checks to see if the game has ended
        if len(used_scores) == 26:
            self._print.set('The Game Has Ended!')
    
    #Create a function for the scoring tactics 3 and 4 of a kind and full house
    def how_many(self, rolls):
        '''This function will allow the scores 3 and 4 of a kind work'''
        #Set all the die to 0
        ones = twos = threes = fours = fives = sixes = 0
        #For  loop iterating through the die
        for x in rolls:
            if x == 1:
                ones += 1
            elif x == 2:
                twos += 1
            elif x == 3:
                threes += 1
            elif x == 4:
                fours += 1
            elif x == 5:
                fives += 1
            elif x == 6:
                sixes += 1
        #Create a list with the die in it
        result = [ones, twos, threes, fours, fives, sixes]
        #Return the list
        return result
    
    #Create a function for small straight
    def small_straight(self, rolls):
        '''This function will allow the score small straight to work'''
        #Checks for different subsets
        if set([1, 2, 3, 4]).issubset(rolls): #Credit for issubset goes to Joel
            return True
        elif set([2, 3, 4, 5]).issubset(rolls):
            return True
        elif set([3, 4, 5, 6]).issubset(rolls):
            return True
        else:
            return False
    
    #Create a function for the large straight
    def large_straight(self, rolls):
        '''This function will allow the score small straight to work'''
        #Checks for different subsets
        if set([1, 2, 3, 4, 5]).issubset(rolls):
            return True
        elif set([2, 3, 4, 5, 6]).issubset(rolls):
            return True
        else:
            return False
        
    #Create a function that checks if items have already been selected
    def check(self, user_choice):
        '''This function will check to see if the user has already selected an item'''
        #Globalizes used_scores
        global used_scores
        #Checks to see if the choice is in used_scores
        if user_choice in used_scores:
            return True     #score has been used
        return False

#Call the program
Yahtzee()