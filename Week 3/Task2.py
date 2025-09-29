print("program starting.")
print("String comparison")
word1= input("Insert a first word: ")
character= input("Insert a character: ")
if character in word1:
    print(f"Word \"{word1}\" contains character \"{character}\"")
else:
    print(f"Word \"{word1}\" does not contain character \"{character}\"")
word2= input("Insert a second word: ")
if word1 > word2:
    print(f"The second word \"{word2}\" is before the first word \"{word1}\" alphabetically")
elif word1 < word2:
    print(f"The first word \"{word1}\" is before the second word \"{word2}\" alphabetically")
else:
    print("Both inserted words are the same alphabetically,\"{word1}\"")
print("Program endeing.")