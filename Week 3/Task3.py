print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")

print("Options:")
print("1 - Print welcome message")
print("0 - Exit")
choice = int(input("Your choice:"))
if choice ==1:
    print(f"Welcome {name}!\n")
elif choice == 0:
    print("Exiting...\n")
else:
    print("Unknown option.\n")
print("Program ending.")
