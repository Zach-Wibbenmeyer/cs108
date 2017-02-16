'''Using Python to Compute the Wind Chill
February 26, 2015
Lab 4, Project 1
Zach Wibbenmeyer (zdw3)'''

#Prompts the user to enter a number for the temperature
temperature = float(input('Please enter a number for the temperature in Fahrenheit: '))

#Prompts the user to enter a number for the wind speed
wind_speed = float(input('Please enter a number for the wind speed: '))

#Calculates the wind chill temperature
wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed)**.16) + (0.4275 * temperature * (wind_speed)**.16)

#If/else statement saying the program will not work by the given specifications
if (wind_speed < 2) or (temperature < -58) or (temperature > 41):
    print('The program will not work')
else:
    #Prints out the result of the wind chill temperature
    print('The wind chill temperature is' , wind_chill , 'degrees Fahrenheit')
    #Telling the user how many layers to wear based on the wind chill    
    if wind_chill < -40:
        print('Wear 5 layers outside today')
    elif -40 <= wind_chill < -10:
        print('Wear 4 layers outside today')
    elif -10 <= wind_chill < 20:
        print('Wear 3 layers outside today')
    elif 20 <= wind_chill < 40:
        print('Wear 2 layers outside today')
    elif wind_chill >= 40:
        print('Wear 1 layer outside today')