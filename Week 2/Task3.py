print("Program starting")

frist_word = input("Insert frist word:")
second_word = input("Insert second word:")

len1 = len(frist_word)
len2 = len(second_word)

print(f"1st word is {len1} characters long")
print(f"2nd word is {len2} characters long")

compound = frist_word + second_word
print(f"Words together makes one closed compound \"{compound}\" ")

print("Ending program")