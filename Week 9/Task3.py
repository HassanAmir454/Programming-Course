import sys
def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    try:
        with open(filename, "r") as file:
            print(f"## {filename} ##")
            print(file.read(), end="")
            print(f"## {filename} ##")
            print("Program ending.")
            
    except FileNotFoundError:
        print(f"Couldn't read file \"{filename}\".")
        sys.exit(1)
main()
# A9_T3_D1.txt
