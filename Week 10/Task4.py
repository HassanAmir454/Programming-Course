import sys

def readFile(filename: str) -> list[int]:
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        return [int(x.strip()) for x in lines if x.strip() != ""]
    
def merge(Pleft, Pright, Pvalue, Asc: bool =True):
    i =j =k=0
    while i < len(Pleft) and j < len(Pright):
        if Asc:
            if Pleft[i] <= Pright[j]:
                Pvalue[k] = Pleft[i]
                i += 1
            else:
                Pvalue[k] = Pright[j]
                j+=1
        else:
            if Pleft[i] >= Pright[j]:
                Pvalue[k] = Pleft[i]
                i += 1
            else:
                Pvalue[k] = Pright[j]
                j+=1

        k+=1
     
    while i < len(Pleft):
        Pvalue[k] = Pleft[i]
        i +=1
        k+=1

    while j < len(Pright):
        Pvalue[k] = Pright[j]
        j +=1
        k+=1




def mergeSort(Pvalue: list[int], Asc: bool = True):
    if len(Pvalue) <= 1:
     return
    mid = len(Pvalue)//2

    left = Pvalue[0: mid]
    right = Pvalue[mid: ]


    mergeSort(left, Asc)
    mergeSort(right, Asc)

    merge(left, right, Pvalue, Asc)
        


def main() -> None:
    print("Program starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert filename: ")
        
    values = readFile(filename)
    print(f"Raw '{filename}' -> {', '.join(str(v) for v in values) }")

    asc_val = values.copy()
    mergeSort(asc_val, True)
    print(f"Accending '{filename}' -> {', '.join(str(v) for v in asc_val) }")


    dsc_val = values.copy()
    mergeSort(dsc_val, False)
    print(f"Descending '{filename}' -> {', '.join(str(v) for v in dsc_val) }")

    print("Program ending")
main()

    # python "Week 10\Task4.py" "A10_D10.txt" 





