# Program starting.
# Insert first name: Guido
# Insert last name: Rossum
# Insert filename: A6_T2_F1.txt
# Program ending.
print("Program starting.")
frist_name = input("Insert first name:")
last_name = input("Insert last name:")
file_name = input("Insert filename:")
with open(f"{file_name}", "w") as file:
    file.write(frist_name + "\n")
    file.write(last_name)

print("Program ending.")