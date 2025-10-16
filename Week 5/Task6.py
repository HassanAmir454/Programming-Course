def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    choice = input("Your choice: ")
    if not choice.isnumeric():
        print("Unknown option!")
        return -1
    return int(choice)

def main():
    print("Program starting.")
    num = 0
    choice = -1
    while choice != 0:
        choice = showOptions()
        if choice == 1:
            print(f"Current count - {num}")
        elif choice == 2:
            print("Count increased!")
            num += 1
        elif choice == 3:
            print("Cleared count!")
            num = 0
        elif choice == 0:
            print("Exiting program.")
        elif choice != -1:
            print("Unknown option!")
    print("Program ending.")

main()

# def Displaymenu() -> int:
#     print("Options: ")
#     print("1 - Show count")
#     print("2 - Increase count")
#     print("3 - Clear count")
#     print("0 - Exit")
#     choice = input("Your choice: ")
#     if not choice.isnumeric():
#         print("Unknown option!")
#         return -1
#     return int(choice)


# def main():
#     print("Program starting.")
#     count = 0
#     choice = -1
#     while choice != 0:
#         choice = Displaymenu()
#         if choice == 1:
#             print(f"Current count - {count}")
#         elif choice == 2:
#             count += 1
#             print("Count increased!")
#         elif choice == 3:
#             count = 0
#             print("Cleared count!")
#         elif choice == 0:
#             print("Exiting program.")
#         elif choice != -1:
#             print("Unknown option!")
#     print("Program ending.")
#     return None
# main()