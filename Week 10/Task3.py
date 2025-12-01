import sys

def readFile(filename: str) -> list[int]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        return [int(x.strip()) for x in lines if x.strip() != ""]

def bubbleSort(asc_value: list[int], Asc: bool = True):
    n = len(asc_value)
    for i in range(n-1):
        for j in range(n-i-1):
            if Asc and asc_value[j] > asc_value[j+1]:
                asc_value[j], asc_value[j+1] = asc_value[j+1], asc_value[j]

            elif not Asc and asc_value[j] < asc_value[j+1]:
                asc_value[j], asc_value[j+1] = asc_value[j+1], asc_value[j]


        # if Asc == True:
        #     if i > largenumber:
        #         largenumber = i
        #         asc_value.append(int(largenumber))
        #         pass
        # else:
        #     if i < largenumber:
        #         largenumber = i
        #         asc_value.append(int(largenumber))
        #         pass



def main() -> None:
    print("Program starting")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert file name: ")

    values = readFile(filename)
    print(f"Raw '{filename}' -> {', '.join(str(v) for v in values) }")

    asc_value = values.copy()
    bubbleSort(asc_value, True)
    print(f"Accending '{filename}' -> {', '.join(str(v) for v in asc_value) }")

    dec_value = values.copy()
    bubbleSort(dec_value, False)
    print(f"Decending '{filename}' -> {', '.join(str(v) for v in dec_value) }")

    print("Program ending.")
main()


# python "Week 10\Task3.py" "A10_D10.txt" 

    

    