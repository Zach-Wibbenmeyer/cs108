'''Python: Mutating a DNA Sequence
February 25, 2015
Homework 3
Zach Wibbenmeyer (zdw3)'''

#Prompts the user to enter a sequence of characters
sequence = input("Enter a sequence of characters: ")
#Prompts the user to enter a pattern in the sequence
pattern = input("Enter the pattern: ")

#Reverses the pattern
reverse = pattern[::-1]

#Uses the find function to find the pattern entered by the user
beginning = sequence.find(pattern)
#Uses the find function find the reverse in the pattern
ending = sequence.find(reverse)
#Finds the length of the reverse variable
length = len(reverse)

#Takes the sequence and goes through the beginning and ending variables and adds the pattern variable
inside = sequence[beginning:ending] + reverse

#Takes the reverse of the sequence and assigns it to the variable 'reverse_inside'
reverse_inside = inside[::-1]

#Calculates the mutated sequence
mutated_sequence = sequence[:beginning] + reverse_inside + sequence[(ending + length):]

#Prints the mutated sequence
print('Mutated Sequence: ' , mutated_sequence)