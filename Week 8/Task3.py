# Program starting.
# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 1
# Insert filename: A8_T3_D1.txt

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 2
# Amount of values 5

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 3
# Sum of values -115.5

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 4
# Average of values -23.1

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

print("Program starting.")
count = 0
nums = []
while True:
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    if choice == 0:
        print("Exiting program.")
        break
    elif choice == 1:
        filename = input("Insert filename: ")
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            count += 1
            nums.append(float(line))
    elif choice == 2:
        print(f"Amount of values {count}")
    elif choice == 3:
        result = sum(nums)
        print(f"Sum of values {result}")
    elif choice == 4:
        average = sum(nums)/count
        print(f"Average of values {average:.2f}")
print("\nProgram ending.")


#A8_T3_D2.txt  
