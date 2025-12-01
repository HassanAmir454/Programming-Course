

def readFile(filename):
    values = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                values.append(int(line))
    return values

def sumof(values):
    total = 0
    for i in values:
        total += i
    return total

def productof(values):
    product = 1
    for i in values:
        product *= i
    return product


def main() -> None:
    print("Program starting")
    filename = input("Insert filename: ")
    values = readFile(filename)
    print("# --- Sum of numbers --- #")
    print(sumof(values))
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(productof(values))
    print("# --- Product of numbers --- #")
    print("Program ending")
main()