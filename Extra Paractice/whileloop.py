# Print numbers 1 to 50 using a for loop.
i = 1
while i < 51:
    print(i)
    i += 1

# Print all even numbers between 1–100 using a for loop.
i = 1
while i < 100:
    if i % 2 == 0:
        print(i)
    i += 1


# Print all odd numbers between 1–100 using a while loop.
i = 2
while i < 100:
    if i % 2 != 0:
        print(i)
    i += 1
    

# Print numbers 10 to 1 in descending order.
i = 10
while i != 0:
    print(i)
    i -= 1
# Print the sum of numbers 1–100 using both for and while loops.
i = 1
sum = 0
while i < 101:
    sum += i
    i += 1
print(sum)


sum2 = 0
for i in range(1, 101):
    sum2 += i
print(sum2)


# Print factorial of a number entered by the user (use for loop first, then while).
n = int(input("Enter num for fact:"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# Take a number as input and print the sum of its digits (no string conversion).
n = int(input("Enter num for sum of digit:"))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
print(sum)

# product
n = int(input("Enter num for product of digits:"))
product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n = n // 10
print(product)

# Take a number n and print the factorial of n using a while loop.
n = int(input("Enter num for fact:"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# Print the cumulative sum of numbers 1–20.
i = 1
sum = 0
while i < 21:
    sum += i
    print(sum)
    i += 1




# Print the cumulative product of numbers 1–10.
i = 1
product = 1
while i < 11:
    product *= i
    print(product)
    i += 1

#     Print all numbers 1–100 divisible by 3.
i = 1
while i <= 100:
    if i % 3 == 0:
        print(i)
    i += 1



# Print all numbers 1–100 divisible by 5 or 7.
i = 1
while i <= 100:
    if i % 5 == 0 or i % 7 == 0:
        print(i)
    i += 1

# Take a number and check if it is prime using a while loop.
n = int(input("Enter number to check prime: "))
i = 2
while i < n:
    if n % i == 0:
        print("Number is not prime")
        break
    else:
        print("Number is prime")
        break
        
i += 1



# Print all prime numbers between 1–50 using a while loop.




n = 2  # start from 2
while n <= 50:
    is_prime = True
    i = 2
    while i < n:   # check divisibility from 2 to n-1
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(n)
    n += 1


# Take a number and check if it is an Armstrong number.
n = int(input("Enter number for armstrong:"))
orignal = n 
power = len(str(n))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit**power
    n = n // 10

if sum == orignal:
    print("Number is prime")


# Print a pattern of stars:

# *
# **
# ***
# ****
# *****

i = 1
while i < 6:
    print("*"*i)
    i += 1

print()
# Print a reverse triangle pattern:

# *****
# ****
# ***
# **
# *
i = 5
while i != 0:
    print("*"*i)
    i -= 1

# Print numbers 1–n in a cumulative sum fashion (running total).
n = int(input("Enter number"))
i = 1
sum = 0
while i <= n:
    sum += i
    print(sum)
    i += 1

# Take a number n and print the first n Fibonacci numbers using while loop.
n = int(input("enter num for fibonachi: "))
a = 0
b = 1
count = 0
while count< n:
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num
    count += 1

print()


# Take a number and reverse it without converting to string.
n = int(input("enter num for reverse: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)
#     Step	n	digit = n % 10	rev before	rev * 10 + digit	n after (n // 10)
# 1	1234	4	0	0×10 + 4 = 4	123
# 2	123	3	4	4×10 + 3 = 43	12
# 3	12	2	43	43×10 + 2 = 432	1
# 4	1	1	432	432×10 + 1 = 4321	0

n = 10
while True:
    userinput = int(input("Guess number to won: "))
    if n == userinput:
        print("congrats, you win")
        break
    else:
        print("Try again")

# Take a number n and print its binary equivalent using a while loop.
n = int(input("enter num to get binary: "))
quo = n
binary = " "
while quo> 0:
    remainder = quo % 2
    binary = str(remainder) + binary
    quo = quo // 2
print("Binary =", binary)

# Take a number n and print its octal equivalent using a while loop.
n = int(input("enter num to get octal: "))
quo = n
octal = ""
while quo > 0:
    remainder = quo % 8
    octal = str(remainder) + octal
    quo = quo // 8
print("Octal=",octal)

n = 1 
while n < 1000:
    i = 1
    sum_of_divisor = 0
    while i < n:
        if n % i == 0:
            sum_of_divisor += i
        i += 1
    if sum_of_divisor == n:
        print(n)
    n += 1

# Print all Armstrong numbers between 1–1000.
n = 1
while n < 1000:
    temp = n
    sum = 0
    power = len(str(n))
    while temp > 0:
        digit = temp % 10
        armstrong = digit**power
        temp = temp // 10
        sum += armstrong
    if sum == n:
        print(n)
    n += 1

# Take a number n and print a diamond/star pattern of height n.
n = 1
while n < 6:
    print("*" * n)
    n += 1

# Write a program that adds even digits and multiplies odd digits of a number.

