'''
Test for the Yahtzee Project
May 19, 2015
Zach Wibbenmeyer (zdw3)
'''

#Create a function for the scoring tactics in the list box
def score_dice(self, user_choice):
    '''This function will model the different scoring tactics in the game'''
    global roll_number, selection
    global final_scores, list_scores
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
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
    #If you are able to collect
    if collect:
        #Add the score to the final score
        return result

#Create a function for the scoring tactics 3 and 4 of a kind and full house
def how_many(self, rolls):
    '''This function will allow the scores 3 and 4 of a kind work'''
    #Set all the die to 0
    ones = twos = threes = fours = fives = sixes = 0
    #For  loop iterating through the die
    #rolls = [1,1,1,3,2]
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
    return result

#Create a function for small straight
def small_straight(self, rolls):
    '''This function will allow the score small straight to work'''
    if set([1, 2, 3, 4]).issubset(rolls):
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
    if set([1, 2, 3, 4, 5]).issubset(rolls):
        return True
    elif set([2, 3, 4, 5, 6]).issubset(rolls):
        return True
    else:
        return False
    
    
'''---------------------------------------------------Main Code------------------------------------------------'''
rolls1 = [2,2,3,1,4]

rolls2 = [6,4,4,4,3]

rolls3 = [1, 2, 3, 4, 5]

rolls4 = [2, 3, 4, 5, 1] 

rolls5 = [1, 2, 3, 4, 5]  
   
f1 = how_many(rolls1, rolls1)
print(f1)

f2 = how_many(rolls2, rolls2)
print(f2)

f10 = how_many(rolls5, rolls5)
print(f10)

f3 = small_straight(rolls3, rolls3)
print(f3)

f4 = small_straight(rolls4, rolls4)
print(f4)

f5 = large_straight(rolls3, rolls3)
print(f5)

f6 = small_straight(rolls2, rolls2)
print(f6)

f7 = large_straight(rolls2, rolls2)
print(f7)

f8 = large_straight(rolls5, rolls5)
print(f8)