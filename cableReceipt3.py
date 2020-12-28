#
# File: cableReceipt3.py
# Name: Christopher M. Anderson
# Date: 03/31/2019
# Course: DSC510 Intro to Programming
# Week: 3
# Assignment Number: 4.1
#
# Program Purpose: A program to calculate the total installation
#         costs of fiber optic cable and print a receipt after
#         gathering inputs.
#
#          cableReceipt3.py does the following things:
#
#          1) Provides a brief welcoming message
#          2) Gathers a couple of user inputs
#          3) A function to calculate the rate to charge based upon length of cable installed
#          4) Generates a total installation cost
#          5) Prints a nicely-formatted receipt
#


# ----------| WELCOME |----------

# Let's welcome the user with a brief introduction:

print("Welcome to the DSC510, Inc. Fiber Optic Cable Receipt Generator!")
print('\n')  # Start a new line (makes the program easier to follow along when there's 'breathing room'.
print("Please answer the following questions and we'll generate a receipt for you.")
print('\n')


# ----------| INPUTS |----------

# Now let's grab a few inputs from the user and assign them to variables:

companyName = input('1) What is the name of the company?: ')
cableLength = int(input('2) How many feet of fiber optic cable are to be installed?: '))


# ----------| PRICE CHART |----------

# We offer a discount based upon length of cable purchased:
#
# Price chart is from 03/24/19. Change as needed.
#
#   0 - 100: $.87 / foot
# 101 - 250: $.80 / foot
# 251 - 500: $.70 / foot
# 501+     : $.50 / foot

if cableLength <= 100:
    rate = 0.87
elif 101 <= cableLength <= 250:
    rate = 0.80
elif 251 <= cableLength <= 500:
    rate = 0.70
else:
    rate = 0.50


# ----------| CALCULATE TOTAL |----------

# Use a function to perform our calculation:

def calculate(feet, price):
    global total
    total = feet * price
    return total


calculate(cableLength, rate)


# ----------| RECEIPT |----------

# First we create a few variables that style the receipt output:

receiptLine = '*' * 50
headingTitle = 'DSC510, Inc. Fiber Optic Cable Receipt'
print('\n')

# Give a brief intro to the receipt:

print('Here is the receipt you have requested:\n')

# This is the start of the printed receipt:

# Print the receipt header:

print(receiptLine)
print('{:^50}'.format(headingTitle))
print(receiptLine)
print('\n')

# Print the user-inputted company name on the right following the label for it on the left:

print('{:<13}'.format('Company Name:'), '{:>36}'.format(companyName))
print('\n')

# Print the user-inputted cable length on the right following the label for it on the left:

print('{:<24}'.format('Cable requested (feet):'), '{:>25}'.format(cableLength))

# Print the price per foot of cable on the right following the label for it on the left:

print('{:<12}'.format('Cable price:'), '{:>24}'.format('x $'), '{:>12.2f}'.format(rate))

# Print an underline to help show we're calculating a total:

print('{:>50}'.format('----------'))

# Print the calculated price total on the right following the label for it on the left:

print('{:<6}'.format('Total:'), '{:>30}'.format('$'), '{:>12.2f}'.format(total))
print('\n')

# End the receipt showing a closing footer:

# Let the user know if they received a discount:

if rate < 0.87:
    print('{:<50}'.format('Buying in bulk earned you a discount today!\n'))
    print('{:<14}'.format('Total savings:'), '{:>22}'.format('$'), '{:>12.2f}\n'.format(cableLength * float(0.87) - (cableLength * rate)))
else:
    print('{:^50}'.format('Thank you for your business!\n'))

print(receiptLine)
