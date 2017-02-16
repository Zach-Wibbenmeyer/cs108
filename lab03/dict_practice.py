'''Python: Practicing with Dictionaries
February 19, 2015
Lab 3, Exercise 3
Zach Wibbenmeyer (zdw3)'''

#Creates a dictionary titled "scoreDict"
scoreDict = {'Joe':10,'Tom':23,'Barb':13,'Sue':19,'Sally':12}

#Prints Barb's score
print(scoreDict['Barb'])

#Edits Sally's score to now be 13 in the dictionary
scoreDict['Sally'] = 13

#Deletes Tom from the dictionary
del scoreDict['Tom']

#Prints the final result of the dictionary
print(scoreDict)