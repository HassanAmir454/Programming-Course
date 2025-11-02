print("Program starting.")
print("This program can read a file.")

file_name = input("Insert filename:")
print(f"#### START \"{file_name}\" ####")

if file_name == "A6_T1_D1.txt":
    with open("A6_T1_D1.txt", "r") as file:
        print(file.read())

elif file_name == "A6_T1_D2.txt":
    with open("A6_T1_D2.txt", "r") as file:
        print(file.read())

elif file_name == "A6_T1_D3.txt":
    with open("A6_T1_D3.txt", "r") as file:
        print(file.read())
    
print(f"#### END \"{file_name}\" ####")
print("Program ending.")
