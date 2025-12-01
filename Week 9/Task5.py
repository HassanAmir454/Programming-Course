import sys

def colorcollected():
    red = input("Insert red:")
    try:
        red_1 = int(red)
        if not (0 <= red_1 <= 255):
            print(f"Value {red_1} is out of the range 0-255.")
            print("Couldn't perform the designed task due to the invalid input values.")
            print("Program ending")
            sys.exit(1)
            
        

            
    except ValueError:
        print(f"'{red}' is non-numeric value.")
        print("Couldn't perform the designed task due to the invalid input values.")
        print("Program ending")
        sys.exit(1)
    
    blue = input("Insert blue:")
    try:
        blue_1 = int(blue)
        if not (0 <= blue_1 <= 255):
            print(f"Value {blue_1} is out of the range 0-255.")
            print("Couldn't perform the designed task due to the invalid input values.")
            print("Program ending")
            sys.exit(1)
    except ValueError:
        print(f"'{blue}' is non-numeric value.")
        print("Couldn't perform the designed task due to the invalid input values.")
        print("Program ending")
        sys.exit(1)

    green = input("Insert green:")
    try:
        green_1 = int(green)
        if not (0 <= green_1 <= 255):
            print(f"Value {green_1} is out of the range 0-255.")
            print("Couldn't perform the designed task due to the invalid input values.")
            print("Program ending")
            sys.exit(1)
    except ValueError:
        print(f"'{green}' is non-numeric value.")
        print("Couldn't perform the designed task due to the invalid input values.")
        print("Program ending")
        sys.exit(1)
    return red_1 , blue_1, green_1


def main() -> None:
    print("Program starting: ")
    r, b, g = colorcollected()
    print("RGB Details:")
    print(f"- Red {r}")
    print(f"- Green {g}")
    print(f"- Blue {b}")

    hex_code = f"#{r:02x}{g:02x}{b:02x}".format(r, g, b)
    print(f"- Hex {hex_code}")
    print("Ending program.")
main()



