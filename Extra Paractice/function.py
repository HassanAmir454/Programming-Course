# Write a function hello() that prints "Hello, world!".
def hello():
    print("Hello World!")
hello()
# Write a function print_name(name) that prints your name.
def print_name(name):
    print("your name is :", name)
print_name("Hassan")
# Write a function add(a, b) that returns their sum.
def sum(a, b):
    return a + b
result = sum(7, 8)
print(result)

# Write a function subtract(a, b) that returns their difference.
def difference(a, b):
    return a - b
result = difference(7, 8)
print(result)

# Write a function multiply(a, b) that returns their product.
def product(a, b):
    return a * b
result = product(7, 8)
print(result)

# Write a function divide(a, b) that safely divides (and avoids division by zero).
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."
result = division(7, 3)
print(result)

# Write a function square(n) that returns the square of a number.
def square(n):
    return n**2
result = square(11)
print(result)

# Write a function cube(n) that returns the cube of a number.
def cube(n):
    return n**3
result = cube(11)
print(result)


# Write a function max_of_two(a, b) that prints which number is greater.
def max_of_two(a, b):
    if a > b:
        return f"a = {a} is greater than b"
    elif b > a:
        return f"b = {b} is greater than a"
    else:
        return "both are same"
result = max_of_two(6, 7)
print(result)

# Write a function greet_person(name, age) that prints a message like “Hello Ali, you are 20 years old.”
def greet_person(name, age):
    return f"Hello {name}, you are {age} years old."
result = greet_person("Hassan", 20)
print(result)



# Write a function is_even(n) that returns True if even, else False.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(9))

# Write a function sum_of_n(n) that returns the sum of numbers 1–n.
def sum_of_n(n):
    sum = 0
    while n > 0:
        sum += n    
        n -= 1
    return sum
    
print(sum_of_n(15))

# Write a function factorial(n) that returns n factorial using a while loop.
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact
print(factorial(5))

# Write a function count_digits(n) that counts digits in a number.
def count_digits(n):
    return len(str(n))
print(count_digits(98765))

# Write a function sum_of_digits(n) that adds all digits in a number.
def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum
print(sum_of_digits(12345))


# Write a function reverse_number(n) that returns the reverse of a number (no string conversion).
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
print(reverse_number(1234))

# Write a function is_palindrome_num(n) that checks if a number is palindrome.
def is_palindrome(n):
    orignal = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if rev == orignal:
        return "yes, the number is palndrome"
    else:
        return "No, the numbe is not palindrome"
print(is_palindrome(454))
    

# Write a function is_prime(n) that checks if a number is prime
def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return "False, the number is not a prime"
        i += 1
    return "True, the number is prime"
print(is_prime(2))



# Write a function print_primes(limit) that prints all primes up to limit.
def print_primes(limit):
    num = 2
    while num <= limit:
        i = 2
        is_prime = True
        while i <num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        
        if is_prime:
            print(num)
        num += 1
print_primes(100)


# Write a function fibonacci(n) that prints first n Fibonacci numbers.
def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num
        count += 1
    return count
print(fibonacci(10))


# Write a function even_sum_odd_product(n) that adds even digits and multiplies odd digits.
def even_sum_odd_product(n):
    even_sum = 0
    odd_product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit
        elif digit % 2 != 0:
            odd_product *= digit
        n = n // 10
    return f"sum of evens is {even_sum} & product of odds is {odd_product}"
print(even_sum_odd_product(123456))

# Write a function table(n) that prints multiplication table of n (1–10).
def table(n):
    for tab in range(1, n+1):
        for i in range(1, 11):
            print(f"{tab} X {i} =", tab*i)
table(10)


# Write a function perfect_numbers(limit) that prints all perfect numbers up to limit.
def perfect_num(n):
   
    num = 2
    while num <= n:
        sum = 0
        i = 1
        while i < num:
            if num % i == 0:
                sum += i
            i += 1
        if sum == num:
            print(num)
        num += 1
perfect_num(1000)




# def perfect_numbers(limit):
#     num = 2
#     while num <= limit:
#         sum_div = 0
#         i = 1
#         while i < num:
#             if num % i == 0:
#                 sum_div += i
#             i += 1
#         if sum_div == num:
#             print(num)
#         num += 1

# perfect_numbers(1000)
# Write a function armstrong_numbers(limit) that prints all Armstrong numbers up to limit.
def armstrong_numbers(limit):
    num = 1
    
    while num <= limit:
        orignal = num
        temp = num
        sum = 0
        power = len(str(num))
        while temp > 0:
            digit = temp % 10
            sum += digit**power
            temp = temp // 10
        if sum == orignal:
            print(orignal)
        num += 1
armstrong_numbers(1000)



# Write a function find_max(lst) that finds the largest number in a list (without max()).
lst = [2, 44, 67, 35, 23, 67, 99, 982, 456, 352, 468, 820, 763]
def find_max(lst):
    maximum = lst[0]
    for i in lst:
        if maximum < i:
            maximum = i
    return maximum
print(find_max(lst))
