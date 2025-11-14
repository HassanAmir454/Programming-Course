
# Program starting.
# Insert filename: A8_T4_D1.txt
# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 1
# Insert year: 2000
# Amount of timestamps during year '2000' is 3

# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 2
# Insert month: April
# Amount of timestamps during month 'April' is 2

# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 3
# Insert weekday: Monday
# Amount of timestamps during weekday 'Monday' is 3

# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.
import task4librarayfile as lib

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    timestamps = []
    filename = input("Insert filename: ")
    lib.readTimestamps(filename, timestamps)

    while True:
        showOptions()
        
        choice = int(input("Your choice: "))
        
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            year = int(input("Insert year: "))
            amount = lib.calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}")
        elif choice == 2:
            month = input("Insert month: ")
            amount = lib.calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}")
        elif choice == 3:
            weekday = input("Insert weekday: ")
            amount = lib.calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()


#A8_T4_D2.txt