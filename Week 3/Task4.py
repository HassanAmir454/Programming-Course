print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")

print("Options:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the frist character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
choice = int(input("Your choice:"))
if choice ==1:
    print(f"Welcome {name}!\n")
elif choice == 2:
    print(f"Your name backwards is {name[::-1]}\n")
elif choice == 3:
    print(f"The first character in name {name} is '{name[0]}'\n")
elif choice == 4:
    print(f"There are {len(name)} characters in the name \"{name}\" \n")
elif choice == 0:
    print("Exiting...\n")
else:
    print("Unknown option.\n")
print("Program ending.")
