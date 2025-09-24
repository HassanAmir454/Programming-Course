print("Program starting.")

compound_word = input("Insert a closed compound word: ")

print(f"The word you inserted is '{compound_word}' and in reverse it is '{compound_word[::-1]}'.")

len_compound = len(compound_word)

print(f"The inserted word length is {len_compound}")
print(f"Last character is '{compound_word[-1]}'")

print("Take substring from the inserted word by inserting...")

starting = int(input("1) Starting point: "))
ending = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

print(f"The word '{compound_word}' sliced to the defined substring is '{compound_word[starting:ending:step]}'.")
print("Program ending.")
