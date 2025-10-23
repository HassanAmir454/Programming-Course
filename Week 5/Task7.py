DELIMITER = ","

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops):")
        
        if word == "":
            break
        words.append(word)
    
    collected = DELIMITER.join(words)
    return collected

        
def analyseWords(words):
    word_list = words.split(DELIMITER)
    total_words = len(word_list)

    total_chars = sum(len(word) for word in word_list)
    if total_words > 0:
        avg = total_chars/total_words
    else:
        avg = 0
    
    print(f"- {total_words} Words")
    print(f"- {total_chars} Characters")
    print("- {:.2f} Average word length".format(avg))



def main():

    print("Program starting.")
    all_words = collectWords()
    analyseWords(all_words)
    print("Program ending.")
main()


# DELIMITER = ","

# def collectWords():
#     words = []
#     while True:
#         word = input("Insert word (empty stops): ")
#         if word == "":
#             break
#         words.append(word)
#     collected = DELIMITER.join(words)
#     return collected


# def analyseWords(words):
#     word_list = words.split(DELIMITER)
#     total_words = len(word_list)
#     total_chars = sum(len(word) for word in word_list)

#     avg = total_chars / total_words 
#     if total_words > 0:
#         avg = total_chars/total_words
#     else:
#         avg = 0

#     print(f"{total_words} Words")
#     print(f"{total_chars} Characters")
#     print("- {:.2f} Average word length".format(avg))


# def main():
#     print("Program starting.")
#     all_words = collectWords()
#     analyseWords(all_words)
#     print("Program ending.")


# main()