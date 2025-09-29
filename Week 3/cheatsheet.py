temp = int(input("whats the temperature of your computer:"))

if temp > 80 :
    print("Warning! The temperature is too high")
else :
    print ("Every things cool ! keep going")

# > greater 
# < less 
# => greater or equal 
# =< less or equal 
# == euqal 
# != not equal 

# MAKE A PROGRAM , WHICH TEST IF THE USER INPUT IS ODD OR EVEN. HINT : %

num = int(input("Enter a number:"))
if num % 2 == 0:
    print (f"{num} is even")
else :
    print(f"{num} is odd.")

# NOW IF ELSE NESTED CONCEPT 
# MAKE A PROGRAM WHICH ASKS YOUSER FOR THE TWO NAMES . THEN TEST IF THE LENGHT OF THE FIRST 
#LONGER , SHORTER OR EQUALS TO THE SECOND NAME. HINT len().

name1 = input("What is the frist name:")
name2 = input("What is the second name:")

len1 = len(name1)
len2 = len(name2)

if len1 > len2 :
    print(f" the first name {name1} is longer then the second name {name2}.")
elif len1 < len2 :
    print(f"The first name {name1} is equals to the second name{name2} ")
else : 
    print(f" The first name {name1} is lesser than the name {name2}")


# NOW MAKE A PROGRAM THAT TELLS ABOUT THE ADDRESS 
town = "lahti"
street = "mukkulankatu"
building = 20

if (town == "lahti" and street == "mukkulankatu" and building == 19):
    print("You are at lab")
elif(town == "lahti" and street != "mukkulankatu" or building != 19):
    print ("you are in the correct town cheak the street")
elif not(town == "lahti" and street == "mukkulankatu" and building == 19):
    print("you are completely lost")

import random

number = random.randint(1, 10)
print(number)