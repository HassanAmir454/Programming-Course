print("Program starting.")
print("\nCollecting plain text rows for ciphering.")
words= []
while True:
    word = input("Insert row(empty stops): ")
    if word == "":
        break
    words.append(word)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def rot13(word):
    result = ""
    for char in word:
        if char in LOWER_ALPHABETS:
            index = LOWER_ALPHABETS.index(char)
            result += LOWER_ALPHABETS[(index + 13) % 26]
        elif char in UPPER_ALPHABETS:
            index = UPPER_ALPHABETS.index(char)
            result += UPPER_ALPHABETS[(index + 13) % 26]
        else:
            result += char  # keep punctuation, numbers same
    return result

# Step 4: cipher all collected lines
ciphered = []
for word in words:
    new_word = rot13(word)
    ciphered.append(new_word)
print("\n#### Ciphered text ####")
for word in ciphered:
    print(word)
print("\n #### Ciphered text ####")
file_name = input("Insert filename to save:")
if file_name.strip() != "":
    with open(f"{file_name}", "w") as file:
        file.write(word)
    print("Ciphered text saved!")
else:
    print("File name not defined.")
    print("Aborting save operation.")

print("Program ending.")









# mira test pass
# LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
# UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# def shiftCharacter(ch, alphabet):
#     # Shift the character by 13 positions within the given alphabet
#     if ch in alphabet:
#         pos = alphabet.index(ch)
#         new_pos = (pos + 13) % 26
#         return alphabet[new_pos]
#     else:
#         return ch


# def rot13(text):
#     # Apply ROT13 transformation to the given text
#     result = ""
#     for ch in text:
#         if ch in LOWER_ALPHABETS:
#             result = result + shiftCharacter(ch, LOWER_ALPHABETS)
#         elif ch in UPPER_ALPHABETS:
#             result = result + shiftCharacter(ch, UPPER_ALPHABETS)
#         else:
#             result = result + ch
#     return result


# def writeFile(filename, content):
#     # Write the content to a file in UTF-8 encoding
#     with open(filename, 'w', encoding="UTF-8") as f:
#         f.write(content)


