import sys

def main() -> None:
    print("Program Starting")

    try:
        code = int(input("Insert exit code(0-255): "))
    except ValueError:
        print("Error! Please enter a valid integer.")
        
    if 0 <= code <= 255:
        if code == 0:
            print("Clean exit.")
        else:
            print("Error code.")
        sys.exit(code)
    else:
        print("Error! Exit code must be between 0 and 255.")
main()


