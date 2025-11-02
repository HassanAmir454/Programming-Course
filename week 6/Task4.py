# Program starting.
# This program analyses a list of names from a file.
# Insert filename to read: A6_T4_D1.txt
# Reading names from "A6_T4_D1.txt".
# Analysing names...
# Analysis complete!
# #### REPORT BEGIN ####
# Name count - 2
# Shortest name - 3 chars
# Longest name - 4 chars
# Average name - 3.50 chars
# #### REPORT END ####
# Program ending.

print("Program starting.")
print("This program analyses a list of names from a file.")
file_name = input("Insert filename to read:")
print(f"Reading names from \"{file_name}\".")
print("Analysing names...")
print("Analysis complete!")
print("#### REPORT BEGIN ####")
with open(f"{file_name}", "r") as file:
    names = file.readlines()

name_count = 0
name_character = 0
shortest = float("inf")
longest = 0

for name in names:
    name = name.strip()
    if name:
        length = len(name)
        name_count += 1
        name_character += length
        if length < shortest:
            shortest = length
        if longest < length:
            longest = length

if name_count > 0:
    average = name_character/ name_count
else:
    average = 0

print(f"Name count - {name_count}")
print(f"Shortest name - {shortest} chars")
print(f"Longest name - {longest} chars")
print(f"Average name - {average:.2f} chars")


print("#### REPORT END ####")
print("Program ending.")
