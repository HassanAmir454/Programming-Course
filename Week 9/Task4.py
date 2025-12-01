import sys
def collectedCelcious():
    feed = input("Insert Celsius:")
    try:
        celcious = float(feed)
    except ValueError:
        print(f"could not convert string to float: '{feed}'")
        print("Program ending.")
        sys.exit(1)
        
    return celcious

def main() -> None:
    print("Program Starting")
    value = collectedCelcious()
    if -273.17 <= value <= 10000:
        print(f"You inserted {value} °C")
    else:
        print(f"{value} temperature out of range.")
    print("Program ending.")

main()
