# Program starting.
# This program can copy a file.
# Insert source filename: A6_T3_D1.txt
# Insert destination filename: A6_T3_F1.txt
# Reading file 'A6_T3_D1.txt' content.
# File content ready in memory.
# Writing content into file 'A6_T3_F1.txt'.
# Copying operation complete.
# Program ending.

print("Program starting.")
print("This program can copy a file.")
source_file = input("Insert source filename:")
destination_file = input("Insert destination filename:")
print(f"Reading file {source_file} content.")
with open(f"{source_file}", "r") as source:
    copy_content = source.read()
print("File content ready in memory.")
print(f"Writing content into file {destination_file}")
with open(f"{destination_file}", "w") as file:
    file.write(copy_content)
print("Copying operation complete.")
print("Program ending.")