'''Using Python to Analyze Text
March 12, 2015
lab06, Exercise 1
Zach Wibbenmeyer (zdw3)'''

#Exercise 6.2
empty_list = []
#Exercise 6.2
list1 = ['bleh']
#Exercise 6.2
list2 = ['what' , 'are' , 'you' , 'doing']


#Code that I copied from the lab
green_eggs_and_ham = [ "i", "am", "sam", "sam", "i", "am", "that",
            "sam-i-am", "that", "sam-i-am", "i", "do", "not", "like", "that", "sam-i-am", "do",
            "you", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them",
            "sam-i-am", "i", "do", "not", "like", "green", "eggs", "and", "ham", "would", "you",
            "like", "them", "here", "or", "there", "i", "would", "not", "like", "them", "here",
            "or", "there", "i", "would", "not", "like", "them", "anywhere", "i", "do", "not",
            "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am",
            "would", "you", "like", "them", "in", "a", "house", "would", "you", "like", "them",
            "with", "a", "mouse", "i", "do", "not", "like", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would",
            "you", "eat", "them", "in", "a", "box", "would", "you", "eat", "them", "with", "a",
            "fox", "not", "in", "a", "box", "not", "with", "a", "fox", "not", "in", "a", "house",
            "not", "with", "a", "mouse", "i", "would", "not", "eat", "them", "here", "or", "there",
            "i", "would", "not", "eat", "them", "anywhere", "i", "would", "not", "eat", "green",
            "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would", "you",
            "could", "you", "in", "a", "car", "eat", "them", "eat", "them", "here", "they", "are",
            "i", "would", "not", "could", "not", "in", "a", "car", "you", "may", "like", "them",
            "you", "will", "see", "you", "may", "like", "them", "in", "a", "tree", "not", "in",
            "a", "tree", "i", "would", "not", "could", "not", "in", "a", "tree", "not", "in", "a",
            "car", "you", "let", "me", "be", "i", "do", "not", "like", "them", "in", "a", "box",
            "i", "do", "not", "like", "them", "with", "a", "fox", "i", "do", "not", "like", "them",
            "in", "a", "house", "i", "do", "not", "like", "them", "with", "a", "mouse", "i", "do",
            "not", "like", "them", "here", "or", "there", "i", "do", "not", "like", "them",
            "anywhere", "i", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not",
            "like", "them", "sam-i-am", "a", "train", "a", "train", "a", "train", "a", "train",
            "could", "you", "would", "you", "on", "a", "train", "not", "on", "a", "train", "not",
            "in", "a", "tree", "not", "in", "a", "car", "sam", "let", "me", "be", "i", "would",
            "not", "could", "not", "in", "a", "box", "i", "could", "not", "would", "not", "with",
            "a", "fox", "i", "will", "not", "eat", "them", "with", "a", "mouse", "i", "will",
            "not", "eat", "them", "in", "a", "house", "i", "will", "not", "eat", "them", "here",
            "or", "there", "i", "will", "not", "eat", "them", "anywhere", "i", "do", "not", "like",
            "them", "sam-i-am", "say", "in", "the", "dark", "here", "in", "the", "dark", "would",
            "you", "could", "you", "in", "the", "dark", "i", "would", "not", "could", "not", "in",
            "the", "dark", "would", "you", "could", "you", "in", "the", "rain", "i", "would",
            "not", "could", "not", "in", "the", "rain", "not", "in", "the", "dark", "not", "on",
            "a", "train", "not", "in", "a", "car", "not", "in", "a", "tree", "i", "do", "not",
            "like", "them", "sam", "you", "see", "not", "in", "a", "house", "not", "in", "a",
            "box", "not", "with", "a", "mouse", "not", "with", "a", "fox", "i", "will", "not",
            "eat", "them", "here", "or", "there", "i", "do", "not", "like", "them", "anywhere",
            "you", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like",
            "them", "sam-i-am", "could", "you", "would", "you", "with", "a", "goat", "i", "would",
            "not", "could", "not", "with", "a", "goat", "would", "you", "could", "you", "on", "a",
            "boat", "i", "could", "not", "would", "not", "on", "a", "boat", "i", "will", "not",
            "will", "not", "with", "a", "goat", "i", "will", "not", "eat", "them", "in", "the",
            "rain", "i", "will", "not", "eat", "them", "on", "a", "train", "not", "in", "the",
            "dark", "not", "in", "a", "tree", "not", "in", "a", "car", "you", "let", "me", "be",
            "i", "do", "not", "like", "them", "in", "a", "box", "i", "do", "not", "like", "them",
            "with", "a", "fox", "i", "will", "not", "eat", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "you",
            "do", "not", "like", "them", "so", "you", "say", "try", "them", "try", "them", "and",
            "you", "may", "try", "them", "and", "you", "may", "i", "say", "sam", "if", "you",
            "will", "let", "me", "be", "i", "will", "try", "them", "you", "will", "see", "say",
            "i", "like", "green", "eggs", "and", "ham", "i", "do", "i", "like", "them", "sam-i-am",
            "and", "i", "would", "eat", "them", "in", "a", "boat", "and", "i", "would", "eat",
            "them", "with", "a", "goat", "and", "i", "will", "eat", "them", "in", "the", "rain",
            "and", "in", "the", "dark", "and", "on", "a", "train", "and", "in", "a", "car", "and",
            "in", "a", "tree", "they", "are", "so", "good", "so", "good", "you", "see", "so", "i",
            "will", "eat", "them", "in", "a", "box", "and", "i", "will", "eat", "them", "with",
            "a", "fox", "and", "i", "will", "eat", "them", "in", "a", "house", "and", "i", "will",
            "eat", "them", "with", "a", "mouse", "and", "i", "will", "eat", "them", "here", "and",
            "there", "say", "i", "will", "eat", "them", "anywhere", "i", "do", "so", "like",
            "green", "eggs", "and", "ham", "thank", "you", "thank", "you", "sam-i-am"]

#Another code copied from lab
stop_words = [ "a", "able", "about", "across", "after", "all",
            "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be",
            "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does",
            "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have",
            "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is",
            "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most",
            "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or",
            "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so",
            "some", "than", "that", "the", "their", "them", "then", "there", "these", "they",
            "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when",
            "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you",
            "your" ]

#Exercise 6.1
print(len(green_eggs_and_ham))

#Creates a function and gives it parameters
def search(str_list , target):
    #If the list is an empty list return -1
    if str_list == []:
        return -1
    #Create a variable and set it equal to 0
    position_indicator = 0
    #For loop for each element in the list
    for x in str_list:
        #If parameter equals element in the list, return position indicator
        if target == x:
            return position_indicator
        #Increment position indicator by 1
        position_indicator += 1
    return -1
        
#Defining a function to search in the lists created above        
def test_search():
    print(search(empty_list , 0))
    print(search(list1 , 'bleh'))
    print(search(list2 , 'what'))
    print(search(list2 , 'are'))
    print(search(list2 , 'you'))
    print(search(list2 , 'doing'))
    print(search(list2 , 'hey'))
  
#Calling the test_search function    
test_search()

'''Algorithm'''
#Create a function called longest_and_shortest with one parameter long_list
    #Create an empty list
    #Print an error message if parameter is an empty list
    #Otherwise, loop for each element in the parameter
        #Create a variable that calculates the length of each element
        #Append length to the empty list
    #Print minimum of the list and the maximum of the list

#Create a function for finding the longest and shortest words in a list
def longest_and_shortest(long_list):
    #Create a list and initialize it to an empty list
    word_length = []
    #If statement for if the list is an empty list
    if long_list == []:
        print('The given list was empty')
    else:
        #If list is not empty, execute this for loop
        for x in long_list:
            length = len(x)
            word_length.append(length)
        #Prints the length of the minimum and maximum words
        print(min(word_length) , max(word_length))
        
'''Algorithm 2'''
#Create a function called count_words_not_present and give it two parameters
    #Create a variable missing_words and initialize it to 0
    #Loop for each parameter in the first list
        #Assign a new variable to the element
        #Create a variable value and use the search function to search the second parameter and new variable
        #If value returns a -1
            #Increment missing_words
    #Print missing_words
        
#Create a function that counts the words not present between two lists        
def count_words_not_present(first_list , second_list):
    #Initialize a variable to 0
    missing_words = 0
    #For loop comparing each word in the first_list to the second_list
    for x in first_list:
        word = x
        value = search(second_list , word)
        #If a word was not found, increment missing_words
        if value == -1:
            missing_words += 1
    #Print the total of missing words
    print(missing_words)

'''Extra Credit'''
#Create a function that ocunts the unique words in two lists    
def count_unique_words(str_list , uniqueWords):
    count = 0
    unique_words = []
    #Search each element in str_list
    for x in str_list:
        word1 = x
        value = search(uniqueWords , word1)
        #If a word was not found, append to unique_words and increment count
        if value not in uniqueWords:
            unique_words.append(word1)
            count += 1
    #Return count
    return count
    #Print unique_words list and count
    print(unique_words , count)
    
#Defining a function to search in the green eggs and ham list
def green_eggs_and_ham_analysis():
    print(search(green_eggs_and_ham , 'i'))
    print(search(green_eggs_and_ham , 'boat'))
    print(search(green_eggs_and_ham , 'fox'))
    print(search(green_eggs_and_ham , 'thank'))
    print(search(green_eggs_and_ham , 'book'))
    longest_and_shortest(green_eggs_and_ham)
    count_words_not_present(green_eggs_and_ham , stop_words) 
    count_unique_words(green_eggs_and_ham , stop_words)
    
#Calling the green_eggs_and_ham_analysis function
green_eggs_and_ham_analysis()