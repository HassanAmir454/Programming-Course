print("Hello")
# it is an example of function

def greet(name):
    return f"Hello, {name}"

message = greet("Mira")
print(message)

message = greet("Hassan")
print(message)
 
def greeting():
    print("How do you do?")

greeting()#call the function
greeting()

def greeting_airport(person, age):
    # print(f"Person: {person}, Age: {age}")
    print(f"How do you do {person}!")
    if age>=18:
        print("Welcome to flight")
    else:
        print(f"You have to wait for {18-age} years to filght on your own")

greeting_airport("Mira", 10)

# Create a program which asks the user for a number then check with a function if the number is a prime
# Also ask the user if they want to test another number as many times as they want 
#Tips: use function conditions and loop....

# integer = int(input("Enter number to check is it prime:"))

# def prime(integer):
#     if integer <= 1:
#         print("Enter number is not prime")
#         return
#     for i in range(2, integer):
#         if integer%i == 0:
#             print("Enter number is not prime")
#             return
#         print("Entered number is prime")
# prime(integer)
            
def prime(integer):
    if integer <= 1:
        print("Entered number is not prime")
        return
    for i in range(2, integer):
        if integer % i == 0:
            print("Entered number is not prime")
            return
    print("Entered number is prime")

# main program loop
while True:
    integer = int(input("Enter number to check if it is prime: "))
    prime(integer)
    
    choice = input("Do you want to test another number? (yes/no): ")
    if choice != "yes":
        print("Goodbye!")
        break




