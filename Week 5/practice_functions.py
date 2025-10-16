# Greeting Function – Write a function greet_user(name) that prints “Hello, [name]!”

# Square a Number – Write square(num) that returns the square of the given number.

# Sum of Two Numbers – Write add_numbers(a, b) that returns the sum.

# Even or Odd – Write a function is_even(num) that returns True if the number is even, else False.

# Maximum of Three Numbers – Write max_of_three(a, b, c) that returns the largest number.

#Number 1

def greeting(Name):
    print(f"Hello {Name}!")

greeting("Hassan")

#Number 2

#1 way of withing code of function
def square(num):
    return num**2

print(square(44))

#2 way
def square(num):
    print(num**2)

square(44)

#3 way
def square(num):
    return num**2

result = square(44)
print(result)

#Number 3

def sum(a=15, b=30):
    return a + b

result = (sum(4, 8))
print(result) #12

def sum(a, b):
    return a + b

result = (sum(4, 8))
print(result)  #12

def sum(a=15, b=30):
    return a + b

result = (sum())
print(result)#45

def evenorodd(number):
    if number/2 == 0:
        return True
    else:
        return False
    
result = evenorodd(9)
print(result)

#Number5
def largernum(a, b, c):
    if b<a>c:
        return a
    elif a<b>c:
        return b
    elif a<c>b:
        return c
    else:
        print("Numbers are equal")
result = largernum(23, 76, 71)
print(result)

# Factorial Calculator – Write factorial(n) using a loop.

# Count Vowels – Write count_vowels(text) that returns the number of vowels in a string.

# Palindrome Checker – Write is_palindrome(word) that returns True if the word reads the same backward.

# Prime Number Check – Write is_prime(n) that returns True if n is a prime number.

# List Sum – Write sum_list(numbers) that returns the sum of all numbers in a list.

def factorial(n):
    fact = 1
    for i in range(1, n+1):
       fact *= i
    return fact


result = factorial(5)
print(result)

#7
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for i in text.lower():
        if i in vowels:
            count += 1
    return count
print(count_vowels("Elephant"))

def is_palindrome(word):
    if word[::] == word[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("civic"))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if  n%i == 0:
            return False
        
    return True
print(is_prime(7))

list = [2, 4, 6, 44, 87, 22, 1]
def sum_list(list):
    total = 0
    for num in list:
        total += num
    return total
print(sum_list(list))

list = [2, 4, 6, 44, 87, 22, 1]
def sum_list(list):
    total = 0
    for num in list:
        total += num
    return total
print(sum_list(list))
    