print("Program starting.")
print("Estimate how many minutes you spent on programming...")

task1 = float(input("A1_T1:"))
task2 = float(input("A1_T2:"))
task3 = float(input("A1_T3:"))
task4 = float(input("A1_T4:"))
task5 = float(input("A1_T5:"))
task6 = float(input("A1_T6:"))
task7 = float(input("A1_T7:"))

Sum = task1 + task2 + task3 + task4 + task5 + task6 + task7
Average = Sum/7
Average = float(Average)

print(f"In total you spent {Sum} minutes on programming")

print(f"Average per task was {round(Average,2)} min and same rounded to the nearest integer {round(Average)}.")

print("Ending program")









