print("Program starting.")

word_count = 0
characters = 0

while True:
    word = input("Insert word (empty stops):")
    if word == "":
        break
    word_count += 1
    characters += len(word)

print("You inserted:")
print(f"- {word_count} words")
print(f"- {characters} characters")

print("Program ending.")




    

