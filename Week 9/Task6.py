import sys

def main():
    print("Program starting.")
    lines = []

    try:
        while True:
            print("\nOptions:")
            print("1 - Insert line")
            print("2 - Save lines")
            print("0 - Exit")
            choice = input("Your choice: ").strip()

            if choice == "1":
                try:
                    
                    text = input("Insert text: ")
                    if text == "":
                        print("Program ending")
                        break
                    lines.append(text)
                except KeyboardInterrupt:
                    if len(lines) == 0:
                        print("\n^CClosing suddenly.")
                        print("Program ending.")
                        sys.exit(1)
                    else:
                        print("\n^CKeyboard interrupt and unsaved progress!")
                        save = input("Save before quit(y/n)?: ").lower()
                        if save == "y":
                            filename = input("Insert filename: ")
                            with open(filename, "a") as f:
                                f.write("\n".join(lines) + "\n")
                        print("Program ending.")
                        sys.exit(0)

            elif choice == "2":
                if len(lines) == 0:
                    print("No lines to save.")
                else:
                    filename = input("Insert filename: ")
                    with open(filename, "a") as f:
                        f.write("\n".join(lines) + "\n")
                    print("Lines saved successfully.")

            elif choice == "0":
                print("Exiting program.")
                print("Program ending.")
                sys.exit(0)

            else:
                print("Unknown option!")

    except KeyboardInterrupt:
        if len(lines) == 0:
            print("\n^CClosing suddenly.")
        else:
            print("\n^CKeyboard interrupt and unsaved progress!")
            save = input("Save before quit(y/n)?: ").lower()
            if save == "y":
                filename = input("Insert filename: ")
                with open(filename, "a") as f:
                    f.write("\n".join(lines) + "\n")
        print("Program ending.")
        sys.exit(0)

if __name__ == "__main__":
    main()
