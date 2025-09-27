print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print("\nLength options:")
    print("1 - Meters to Kilometers")
    print("2 - Kilometers to Meters")
    print("0 - Exit")
    subchoice = int(input("Your choice: "))
    if subchoice == 1:
        meters = float(input("Insert meters: "))
        Kilometers = meters/1000
        print(f"{round(meters,1)} m is {round(Kilometers,1)} km\n")
    elif subchoice == 2:
        Kilometers = float(input("Insert kilometers: "))
        meters = Kilometers*1000
        print(f"{round(Kilometers,1)} km is {round(meters,1)} m \n")
    elif subchoice == 0:
        print("Exiting...\n")
    else:
        print("Unknown option.\n")
elif choice == 2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    subchoice = int(input("Your choice: "))
    if subchoice == 1:
        Grams = float(input("Insert grams: "))
        Pounds = Grams*0.00220462
        print(f"{round(Grams,1)} g is {round(Pounds,1)} lb \n")
    elif subchoice == 2:
        Pounds = float(input("Insert pounds: "))
        Grams = Pounds*453.592
        print(f"{round(Pounds,1)} lb is {round(Grams,1)} g \n")
    elif subchoice == 0:
        print("Exiting... \n")
    else:
        print("Unknown option. \n")
elif choice == 0:
    print("\nExiting... \n")
else:
    print("\nUnknown option \n")

print("Program ending.")
