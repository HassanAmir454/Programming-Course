print("Program starting")
num = int(input("Insert a positive integer:"))
stepcount = 0
while num != 1:
    print(int(num), end="->")
    if num%2 != 0:
        num = num * 3 + 1
    else:
        num = num /2 
    stepcount += 1
print(1)
print(f"Sequence had {stepcount} total steps")
print("/nProgram ending.")
    
