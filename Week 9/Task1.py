# Program starting.

# Insert a floating-point value (0 to stop): 3.5
# Insert a floating-point value (0 to stop): aaaaa
# Error! 'aaaaa' couldn't be converted to float.
# Insert a floating-point value (0 to stop): 1.5
# Insert a floating-point value (0 to stop): 0

# Final sum is 5.00
# Program ending.
summ = 0.0
def add_value(value):
    global summ
    summ += value

def main() -> None:
    print("Program starting.")
    while True:
        raw = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(raw)
        except ValueError:
            print(f"Error! '{raw}' couldn't be converted to float.")
            continue
        if value == 0:
            print(f"final sum is {summ:.2f}")
            print("exiting program")
            break
        add_value(value)

main()