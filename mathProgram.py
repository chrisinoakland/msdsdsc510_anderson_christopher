#
# File: week5.py
# Name: Christopher M. Anderson
# Date: 04/11/2019
# Course: DSC510 Intro to Programming
# Week: 5
# Assignment Number: 5.1

# Instructions:

# This program will have a main section which contains a while loop. The while loop will
# be used to allow the user to run the program until they enter a value which ends the loop.

# Requirements:

# 1. The main program should prompt the user for the operation they wish to perform.
# 2. The main program should evaluate the entered data using if statements.
# 3. The main program should call the necessary function to perform the calculation.


# Program Purpose:

# This program perform various math calculations: (multiplication, division, addition,
# subtraction, and average) based upon a user telling the program which operation to
# perform, and then taking values inputted from the user.

# week5.py does the following things:

# 1) Provides a brief welcoming message.
# 2) Asks the user which math operation they would like to perform.
# 3) If the math operation is addition, subtraction, multiplication, or division, then
#    prompt the user for two inputted numbers and print the calculated value.
# 4) If the math operation is to provide an average, first ask the user how many numbers they want to
#    use in their calculation, then get the inputs and print the calculated average.
# 5) Asks the user if they would like to perform another calculation and re-run if so
#    and exit the program if not.


# ----------| FUNCTION: PERFORM CALCULATION |----------

# The parameter will be the math operation being performed (+, -, *, /).

# This function will perform the following:

# 1) Prompt the user for two numbers then perform the
#    expected operation depending on the parameter that's passed into the function.
# 2) Print the inputted values and also the calculated value for the end user.


def performCalculation(operation):

    num1 = int(input('    Please enter the first number: '))
    num2 = int(input('    Please enter the second number: '))

    if operation == '+':
        print('''
    {} + {} ='''.format(num1, num2), (num1 + num2))

    elif operation == '-':
        print('''
    {} - {} ='''.format(num1, num2), (num1 - num2))

    elif operation == '*':
        print('''
    {} * {} ='''.format(num1, num2), (num1 * num2))

    elif operation == '/':
        print('''
    {} / {} ='''.format(num1, num2), (num1 / num2))

    else:
        print('    You have not typed a valid math operation, please try again.')


# ----------| FUNCTION: CALCULATE AVERAGE |----------

# This function will perform the following:

# 1) Ask for the amount of numbers to find the average for.
# 2) Use a loop to get input values until it has enough to reach that number.
# 3) Print the inputted vales, the total, and the calculated average.


def calculateAverage():
    avgNumber = int(input('    Please type in how many numbers you want to find the average for: '))
    avgTotal = 0
    numbers = 0
    for n in range(avgNumber):
        numbers = float(input('    Enter number: '))
        avgTotal += numbers
    average = avgTotal / avgNumber
    print('\n    The total of the numbers you entered is:', avgTotal, 'and the average is:', average)


# ----------| WELCOME AND HEADER |----------

# Let's welcome the user with a brief introduction

# First we create a few variables that style the heading output:

headingLine = '*' * 50
headingTitle = 'Welcome to the DSC510 Math Program!'

# Print the program header:

print(headingLine)
print('{:^50}'.format(headingTitle))
print(headingLine)


# ----------| MAIN |----------

# Ask the user what they want to do and provide
# a brief menu to help them make a selection:

menuPrompt = 'y'
while menuPrompt == 'y':
    menuList = ['+', '-', '*', '/', 'a']
    selection = input('''
    What type of math would you like to do?

    + for addition
    - for subtraction
    * for multiplication
    / for division
    a for average
    ''')

# Loop the program based upon the user's selection(s):

    if selection == '+':
        performCalculation(selection)
    elif selection == '-':
        performCalculation(selection)
    elif selection == '*':
        performCalculation(selection)
    elif selection == '/':
        performCalculation(selection)
    elif selection == 'a':
        calculateAverage()
    else:
        print('    That was not a valid selection. Please try again.')
        continue

# Ask the user if they are done and honor their request:

    menuPrompt = input('''
    Would you like to perform another calculation? Please type y for yes or n for no.
    ''')
    if menuPrompt == 'y':
        continue
    elif menuPrompt == 'n':
        print('''
    Thanks for using the DSC510 Math Program, see you next time!''')
