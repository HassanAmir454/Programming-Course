# Program starting.
# Options:
# 1 - Set pause duration
# 2 - Activate pause
# 0 - Exit
# Your choice: 1
# Insert pause duration (s): 0.1

# Options:
# 1 - Set pause duration
# 2 - Activate pause
# 0 - Exit
# Your choice: 2
# Pausing for 0.1 seconds.
# Unpaused.

# Options:
# 1 - Set pause duration
# 2 - Activate pause
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.
# import time
# duration = 1.0
print("Program starting.")
while True:
    print("\nOptions:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        duration = float(input("Insert pause duration (s): "))
    elif choice == 2:
        print(f"Pausing for {duration} seconds.")
        print("Unpaused.")
    elif choice == 0:
        print("Exiting program.")
        print("\nProgram ending.")
        break

