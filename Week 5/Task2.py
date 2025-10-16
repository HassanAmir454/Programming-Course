def frameWord(PWord) -> None:
    print("*" * (len(PWord)+ 4))
    print(f"* {PWord} *")
    print("*" * (len(PWord)+ 4))
    return None


def main() -> None:
    print("Program starting.")
    word = str(input("Insert word: "))
    print()
    frameWord(word)
    print()
    print("Program ending.")
    return None
    
main()
