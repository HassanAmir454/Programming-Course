# # Take marks of 5 subjects and calculate:

# # total

# # percentage

# # grade using conditions

# i = 1 
# total = 0

# while i < 6:
#     marks = int(input("Enter your marks: "))
#     total += marks
#     i += 1
# percentage = total/500 * 100
# if percentage > 90:
#     grade = "A"
# elif 80 < percentage > 90:
#     grade = "B"
# elif 70 < percentage> 80:
#     grade ="C"
# else:
#     grade = "F"

# print(f" {total}, {percentage}, {grade}")


# # Print all prime numbers between 1 and 100.
# for num in range(2, 101):
#     is_prime = True
#     for i in range(1, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

    

# # Write a program to reverse a number using a loop.
# number = int(input("Enter number to get reverse: "))
# rev = 0
# while number > 0:
#     digit = number % 10
#     rev = rev * 10 + digit
#     number //= 10
# print(rev)

# # Generate the first n Fibonacci numbers.

# n = int(input("Enter number to get facbonaci: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     a = b
#     b = a + b
# print()

# # Take a string and:

# # count vowels

# # count consonants

# string = input("Enter word to count vowel and consonents:")
# vowels = ["a", "e", "i", "o", "u"]
# vowel = 0
# consonent = 0
# for i in string:
#     if i in vowels:
#         vowel += 1
#     else:
#         consonent += 1
# print(f"No of vowels is {vowel}")
# print(f"No of consonent is {consonent}")

# # Check whether a string is a palindrome (ignore case).
# string2 = input("Enter string to find palindrome: ")
# rev = string2[::-1]
# if string2 == rev:
#     print("Entered word is palindrome")
# else:
#     print("Entered word is palindrome")

# Find the most frequent character in a string.
string3 = input("enter string to find most frequent character: ")
counts = []

for i in range(0, len(string3)):
    word = string3[i]
    count = 0
    for j in string3:
        if word == j:
            count += 1
    counts.append(count)
max_count = max(counts)
index_max = counts.index(max_count)
freq_ch = string3[index_max]
print(f"Most frequent character is: {freq_ch}")

# Remove duplicates from a list without using set.
list1 = [2, 4, 6, 8, 9, 2, 5, 2]
unique = []

for j in list1:
    if j not in unique:
        unique.append(j)
print(unique)

# Sort a list without using sort().
list = [8, 9, 6, 10, 4, 3, 2, 11]
sorted = []
while list:
    min_num = list[0]
    for i in list:
        if i < min_num:
            min_num = i
    sorted.append(min_num)
    list.remove(min_num)
print(sorted)

#or another way
list2 = [81, 91, 16, 10, 41, 13, 21, 11]
for i in range(len(list2)):
    for j in range(i+1, len(list2)):
        if list2[j] < list2[i]:
            list2[i], list2[j] = list2[j], list2[i]
print(list2)


# Convert a list into a tuple and print it.
tuple = tuple(list2)
print(tuple)

# Find common elements between two lists using sets.
list1 = [2, 4, 6, 8, 9, 2, 5, 2]
list = [8, 9, 6, 10, 4, 3, 2, 11]
set1 = set(list1)
set2 = set(list)
common = set1.intersection(set2)
print(common)

# 🔹 7. Dictionary

# Create a dictionary to store student name & marks.
Student = {
    "name" : "Hassan",
    "marks" : 99
}
Student["Grade"] = "A"
print(Student)
print(Student["marks"])
# Find student with highest marks
students = {
    "Hassan": 99,
    "Ali": 85,
    "Sara": 92
}

top_student = max(students, key=students.get)
print("Top student:", top_student)

# Count frequency of each word in a sentence using dictionary.

# 🔹 8. Functions

# Write a function that checks whether a number is prime.
def check_prime(numberr):
    if numberr <= 1:
        print(f"Number {numberr} is not prime")
        return

    for i in range(2, numberr):  
        if numberr % i == 0:
            print(f"Number {numberr} is not prime")
            return
    print(f"Yes {numberr} is prime")
numberr = int(input("Enter number to find either it is prime or not: "))
check_prime(numberr)



# Write a function that returns factorial of a number.
def fact(numm):
    factorial = 1
    while numm> 0:
        factorial *= numm
        numm -= 1
    return factorial
numm = int(input("Enter num to get factorial: "))
print(fact(numm))



# Create a function-based calculator.

# 🔹 9. Exception Handling

# Write a program that:

# takes two numbers

# handles invalid input and division by zero

# 🔹 10. File Handling

# Write a program to:

# create a file

# write user input into it

# read and display file content

# Count number of lines, words, and characters in a file.

# 🔹 11. Modules

# Generate a random password of length 8 using random and string modules.

# Use math module to:

# find square root

# power

# factorial
 



