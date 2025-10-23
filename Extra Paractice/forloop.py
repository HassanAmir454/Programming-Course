# Print numbers 1 to 10

# Print numbers 10 to 1 (reverse)

# Print only even numbers between 1–50

# Print the squares of numbers from 1–10

# Print each character of your name on a new line

# Print the sum of numbers from 1–100

# Print the factorial of 5
fact = 1
n = 5
for i in range(1, n+1):
    fact *= n
print(fact)

# Print “Hello” five times using a for loop

# Loop through the string "PYTHON" and print letters with their index (use enumerate)

# Loop through a list of fruits and print each in uppercase

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(1, 50):
    if i%2 == 0:
        print(i)
    else:
        continue

for i in range(1, 11):
    print(i**2)

name = "hassan"
for i in name:
    print(i)

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

fact = 1
n = 5
for i in range(1, n+1):
    fact *= i
print(fact)

facto = 1
n = 6
for i in range(1, n+1):
    facto = facto * i
print(facto)

greet = "Hello world!"
for i in range(1, 6):
    print(greet)

# Loop through the string "PYTHON" and print letters with their index (use enumerate)
lang = "PYTHON" 
for i in range(0, 6):
    print(f"{i} -",lang[i])

# Loop through a list of fruits and print each in uppercase
fruits = ["banana", "apple", "grapes", "orange", "strawberry"]
for i in fruits:
    print(i.upper())



#     Goal: Use loops for pattern creation, accumulation, and conditional logic.
# 🔹 Pattern Printing (Classic Exercises)

# Print a 5×5 square of *

# *****
# *****
# *****
# *****
# *****
n = 5
for i in range(n):
    print("*"*n)

# Print a right triangle

# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*"*i)

# Print a reversed triangle

# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    print("*"*i)

# Print a number triangle

# 1
# 12
# 123
# 1234

rows = 4
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
    
# Print multiplication table of 7
n = 7
for i in range(1, 11):
    print(f"{n} X {i} =", n*i)

# Print all tables from 1–10 using nested loops

for n in range(1, 11):
    for i in range(1, 11):
        print(f"{n} X {i} =", n*i)


# Given this list:

# nums = [5, 10, 15, 20, 25, 30]


# Do the following:

# Print each element
nums = [5, 10, 15, 20, 25, 30]
for i in nums:
    print(i)

# Print double of each element
nums = [5, 10, 15, 20, 25, 30]
for i in nums:
    print(i*2)

# Print the sum of all elements (using loop, not sum())
nums = [5, 10, 15, 20, 25, 30]
sum = 0
for i in nums:
    sum += i
print(sum)

# Print only elements greater than 15
nums = [5, 10, 15, 20, 25, 30]
# for i in range(3, 6):
#     print(nums[i])
for i in nums:
    if i > 15:
        print(i)
    else:
        continue

# Create a new list with squares of all numbers (using loop)
nums = [5, 10, 15, 20, 25, 30]
new_list = []
for i in nums:
    a = i**2
    new_list.append(a)
print(new_list)
    

# Count how many elements are multiples of 5
nums = [5, 10, 15, 20, 25, 30]
count = 0
for i in nums:
    if i%5 == 0:
        count += 1
print(count)

# Create a list [2, 4, 6, 8, 10, 12, 14, 16] and print:

# The total sum

# The average

# The maximum and minimum (without using built-ins)

list = [2, 4, 6, 8, 10, 12, 14, 16]
sum = 0
for i in list:
    sum += i
print(sum)

list = [2, 4, 6, 8, 10, 12, 14, 16]
sum = 0
for i in list:
    sum += i
avg = sum/len(list)
print(avg)

list = [2, 4, 6, 8, 10, 12, 14, 16, 1]

minimum = list[0]
maximum = list[0]

for i in list:
    if minimum > i:
        minimum = i
    if maximum < i:
        maximum = i
print(minimum)
print(maximum)


# 🔹 Part 1: Numeric Patterns & Logic Loops

# Print all numbers between 1–100 that are divisible by 7 but not by 5.
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
        
    

# Print the sum of all even numbers from 1–50.
sum = 0
for i in range(1, 51):
    
    if i % 2 == 0:
        sum += i
print("The sum of  all even numbers from 1-50 =", sum)
    

# Print all prime numbers between 1–50.
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)


# Print the product of all odd numbers between 1–15.
product = 1
for i in range(1, 16):
    if i % 2 != 0:
        
        product *= i
print(product)

# Print the multiplication table for numbers from 1 to 5, each separated by a blank line.
for n in range(1, 6):
    print()
    for i in range(1, 11):
        print(f"{n} X {i} =", n*i)
        

# Print the sum of digits of a number entered by the user (no string conversion allowed).
num = int(input("Enter num for sum:"))

sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print(sum)

# Print numbers between 1–20 with these rules:

# “Fizz” if divisible by 3

# “Buzz” if divisible by 5

# “FizzBuzz” if divisible by both

for i in range(1, 21):
    print(i)
    if i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue

# Print the cumulative sum of numbers 1–10 like this:

# 1
# 3
# 6
# 10
# 15
# ...
sum = 0
for i in range(1, 11):
    sum += i
    print(sum)

# total = 0   # start with zero

# for i in range(1, 11):
#     total += i         # add current number to total
#     print(total) 


# Print the factorial of a number entered by the user (without using math library).
n = int(input("Enter num for fact:"))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

























# Goal: Combine loops, conditionals, and collections to solve problems like a pro.
# 🔸 Nested Loops

# Print coordinate pairs (x, y) where x in [1,3] and y in [1,3]

# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)


# Print multiplication table (1–5 × 1–5)

# Print a hollow square:

# *****
# *   *
# *   *
# *****


# Print a pyramid pattern (hint: spaces + stars)

#     *
#    ***
#   *****
#  *******

# 🔸 Looping with Strings & Conditions

# Count vowels in a word

# Print only consonants from "Programming"

# Given "hello world", print each word reversed ("olleh dlrow")

# Count how many letters, digits, and special characters are in "Hello123!"

# 🔸 Realistic Challenges

# Sum of digits – input a number, sum its digits using a loop

# Prime check – input a number, check if it’s prime using a loop

# Fibonacci sequence – print first 10 Fibonacci numbers

# Find max manually – given a list, find the largest number using a loop

# Reverse a list manually – no slicing or built-in reverse

# 💥 Mini Projects (choose 2)

# Student Grades

# Input 5 student scores

# Calculate average, max, min, and how many passed (score ≥ 50)

# Password Strength Checker

# Input a password

# Count uppercase, lowercase, digits, symbols

# Print total and give strength level

# Pattern Art Generator

# Input a number n

# Print pyramid, diamond, and hollow square patterns dynamically

# 🧠 Bonus: Stretch Goals (if you still have energy)

# Nested List Iteration

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# Print all elements in row-column format.

# For Loop + Dictionary

# fruits = {"apple": 100, "banana": 50, "mango": 80}


# Print fruit names and prices

# Increase all prices by 10%

# Find which fruit is most expensive
