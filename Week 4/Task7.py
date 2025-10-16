print("Program starting.\n")
print("Check multiplicative persistence.")
num = int(input("Insert an integer: "))
persistence = 0

while num >= 10:
    digits = [int(d) for d in str(num)]
    product = 1

    for i in range(len(digits)):
        product *= digits[i]
        print(digits[i], end="")
        if i != len(digits)-1:
            print(" * ", end ="")
            
    print(" =", product)
    num = product
    persistence += 1
print("No more steps.\n")
print(f"This program took {persistence} step(s)\n")
print("Program ending.")


        

        


