# ----------------- QUSTION 1 -----------------
# Using a single print() statement, output a multiline ASCII art text banner of your name.
print(""" _     _                 
| |   (_) __ _ _ __ ___  
| |   | |/ _` | '_ ` _ \ 
| |___| | (_| | | | | | |
|_____|_|\__,_|_| |_| |_|""")


# ----------------- QUSTION 2 -----------------
# Write a program that asks the user to enter 3 sides lengths of a triangle and then displays the area of that triangle rounded to 2 decimal spots

import math   

# Ask user for side lengths

a = int(input("Please Input Length a of the triangle"))
b = int(input("Please Input Length b of the triangle"))
c = int(input("Please Input Length c of the triangle"))

#Calculates the values to get the area

s = (a + b + c) / 2
f = (s*(s-a)*(s-b)*(s-c))
radical = math.sqrt(f)
radical = round(radical, 2)

#prints the area

print("The Area of the triangle is", radical)


# ------------------ QUSTION 3 -----------------
#  Your program is going to display a persons budget for the month.  Generate realistic random values for the following budget items. 
import random
#Asks what the budget is

b = int(input("what is your budget"))

# Generates a random and realistic budget using percents

totper = 100
rent = random.randint(40,50)
clothing = random.randint(10,15)
food = random.randint(18,25)
entertainment = totper - rent - clothing - food

#Generates a dollar value for the percents

rent2 = round(rent/totper * b, 2)
clothing2 = round(clothing/totper * b, 2)
food2 = round(food/totper * b, 2)
entertainment2 = round(entertainment/totper * b, 2)

#Prints full breakdown of budget

print( "Rent:\t\t\t",rent2,"$",{rent},"%""\nClothing:\t\t\t",clothing2,"$",{clothing},"%""\nFood:\t\t\t",food2,"$",{food},"%""\nEntertainment:\t\t\t",entertainment2,"$",{entertainment},"%")
