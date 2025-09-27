print("Program starting.")
print("Testing decision structures.")
Value = int(input("Insert an integer: "))
print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    print("Using one multi-branched decision structure.")
    if Value >= 400:
        result = Value + 44
        print(f"Result is {result}\n")
    elif Value >= 200:
        result = Value + 22
        print(f"Result is {result}\n")
    elif Value >= 100:
        result = Value + 11
        print(f"Result is {result}\n")
elif choice == 2:
    print("Using multiple independent if-statements structure.")
    if Value >= 400:
        result = Value + 44 + 22 + 11
        print(f"Result is {result}\n")
    elif Value >= 200:
        result = Value + 22 + 11
        print(f"Result is {result}\n")
    elif Value >= 100:
        result = Value + 11
        print(f"Result is {result}\n")
elif choice == 0:
    print("Exting...\n")
else:
    print("Unknown option.\n")
print("Program ending")