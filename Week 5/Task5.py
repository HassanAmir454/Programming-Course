def Displaymenu() -> int:
    print("Options: ")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return int(input("Your choice: "))

    
    
def main():
    print("Program starting.")
    Word = ""
    choice = -1
    while choice != 0:
        choice = Displaymenu()
        if choice == 1:
            Word = str(input("Insert Word: "))
        elif choice == 2:
            print(f"Current Word - \"{Word}\"")
        elif choice == 3:
            print(f"Word Reversed - \"{Word[::-1]}\"")
        elif choice == 0:
            print("Exiting Program.")
        else:
            print("Unknown option! Try again.")
    print("Program ending.")
    return None
main()