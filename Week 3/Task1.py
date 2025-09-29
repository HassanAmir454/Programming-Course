print("Program starting.")
print("Insert two integers: ")
first_integer = int(input("Insert the first integers: "))
second_integer = int(input("Insert the second integers: "))
print("Comparing inserted integers.")
if first_integer > second_integer:
    print("The first integer is greater.")
elif first_integer < second_integer:
    print("The second integer is greater.")
else:
    print("Both integers are the same")
print("Adding integers together.")
sum = first_integer + second_integer
print(f"{first_integer} + {second_integer} = {sum}")
print("Cheaking the parity of sum...")
if sum % 2 == 0:
    print("The sum is even")
else:
    print("The sum is odd")
print("Program ended.")