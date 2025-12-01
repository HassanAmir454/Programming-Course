import copy
import time
from typing import Callable

def readValues(PValues: list[int]) -> str:
    PValues.clear()
    filename = input("Insert dataset filename: ")
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line != "":
                PValues.append(int(line))
    print(f"Dataset '{filename}' loaded with {len(PValues)} values.")
    return filename

def BubbleSort(Pnum: list[int]) -> None:
    n = len(Pnum)
    for i in range(n -1):
        for j in range(n- i - 1):
            if Pnum[j] > Pnum[j+1]:
                Pnum[j], Pnum[j+1] = Pnum[j+1], Pnum[j]
    
def quickSort(PNums: list[int]) -> None:
    def _quickSort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quickSort(arr, low, pivot_index-1)
            _quickSort(arr, pivot_index+1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    _quickSort(PNums, 0, len(PNums)-1)


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime

def main() -> None:
    Values = []
    Results = {}
    Datasetnames = ""
    print("Program starting.")
    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            Datasetnames = readValues(Values)

        elif choice == "2":
            if not Values:
                print("No dataset loaded! Please load a dataset first.")
                continue
            print(f"\nMeasured speeds for dataset '{Datasetnames}':\n")
            Results["Built-in sorted"] = measureSortingTime(sorted, copy.deepcopy(Values))
            Results["Bubble sort"] = measureSortingTime(BubbleSort, copy.deepcopy(Values))
            Results["Quick sort"] = measureSortingTime(quickSort, copy.deepcopy(Values))

            for algo, ns in Results.items():
                print(f" - {algo} {ns} ns\n")
            
        
        elif choice == "3":
            if not Results:
                print("No results to save! Please measure speeds first.")
                continue
            save_file = input("Insert results filename: ").strip()
            with open(save_file, "w") as file:
                file.write(f"Measured speeds for dataset '{Datasetnames}':\n")
                for algo, ns in Results.items():
                    file.write(f" - {algo} {ns} ns\n")
            print(f"Results saved in '{save_file}'.")
        elif choice == "0":
            print("Exiting program.")
            break
main()
                
