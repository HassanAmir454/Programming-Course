print("Program starting.")
num = int(input("Insert a positive integer:"))
print(f"{num}", end="")

stepcount = 0
while num != 1:
    if num%2 != 0:
        num = num * 3 + 1
    else:
        num = num /2 
    print(f" -> {num}", end="")
    stepcount += 1

print()
print(f"Sequence had {stepcount} total steps.\n")
print("\nProgram ending.")
    