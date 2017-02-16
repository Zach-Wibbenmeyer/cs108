'''Using Python to Find the Genes in a Genome
April 1, 2015
Homework 7
Zach Wibbenmeyer (zdw3)'''

#Promps the user to enter a genome string
genome = str(input('Enter a genome string: '))
#Converts the string to all capital letters
genome = genome.upper()

#Genome starts after this string
start_string = 'ATG'
#Genome ends before these string
end_string = ['TAG' , 'TAA' , 'TGA' , 'ATG']


#Finds the index where 'ATG' starts and adds 3 to it
start = genome.find(start_string) + 3


#Create a variable and initialize it to 1
x = 1
#First forever while loop
while True:
    if start - 3 == -1:
        print('No gene is found')
        break
    #Create an empty string
    string = ''
    #Create a count and initialize it to 0
    count = 0
    #Second forever while loop
    while True:
        #Create a variable and assign it to finding the genome
        code = genome[(start + count):(start + count + 3)]
        if code not in end_string:
            #Increment count by 3
            count += 3
            #Add code to string
            string = string + code
            #Check if the count is greater than the length of the string
            if count > len(string):
                print('No genes were found')
                break
        #If start returns a negative 1, then break
        elif start - 3 == -1:
            print('No genes were found')
            break
        #Otherwise, print the gene
        else:
            print('Gene' , x, ':' , string)
            x += 1
            break
    #Create a variable and assign it to the updated genome finder
    new = genome.find(start_string , (start + 1) , -1) + 3
    start = new
    #If new returns a negative 1, then break
    if new - 3 == -1:
        break