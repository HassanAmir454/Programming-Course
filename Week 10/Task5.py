
def Factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * Factorial(number - 1)






def main() -> None:
    print("Program starting.")
    number = int(input("Insert factorial:"))
    print(f"Factorial {number}!")
    result = Factorial(number)
    
    steps = "*".join(str(i) for i in range(1, number + 1))
    
    print(f"{steps} = ", result)
    
    print("Program ending.")
main()