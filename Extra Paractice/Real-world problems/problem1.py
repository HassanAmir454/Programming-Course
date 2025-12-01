# Program starting.

# Options:
# 1 - Add student
# 2 - Search student
# 3 - Update marks
# 4 - Show all students
# 5 - Show top student
# 0 - Exit
# Your choice: 1

# Enter name: Ali
# Enter roll number: 12
# How many subjects? 3
# Enter mark 1: 80
# Enter mark 2: 75
# Enter mark 3: 90
# Student added.

# Options:
# 1 - Add student
# 2 - Search student
# 3 - Update marks
# 4 - Show all students
# 5 - Show top student
# 0 - Exit
# Your choice: 1

# Enter name: Sara
# Enter roll number: 15
# How many subjects? 3
# Enter mark 1: 92
# Enter mark 2: 88
# Enter mark 3: 95
# Student added.

# Options:
# 1 - Add student
# 2 - Search student
# 3 - Update marks
# 4 - Show all students
# 5 - Show top student
# 0 - Exit
# Your choice: 4

# Students List:
# - Ali (Roll: 12) Average: 81.67 Grade: B
# - Sara (Roll: 15) Average: 91.67 Grade: A

# Options:
# 1 - Add student
# 2 - Search student
# 3 - Update marks
# 4 - Show all students
# 5 - Show top student
# 0 - Exit
# Your choice: 5

# Top student is: Sara
# Average: 91.67
# Grade: A

# Options:
# 1 - Add student
# 2 - Search student
# 3 - Update marks
# 4 - Show all students
# 5 - Show top student
# 0 - Exit
# Your choice: 0

# Exiting program.
# Program ending.
# def askRollnum(askrollnum, students):
#     for i in students:
#         return students[askrollnum]
def askRollnum(rollnum, students):
    return students.get(rollnum)
students = {}
def main() -> None:
    print("Program starting.")
    
    updatedmarks = 0
    

    while True:
        print("\nOptions:")
        print("1 - Add student")
        print("2 - Search student")
        print("3 - Update marks")
        print("4 - Show all students")
        print("5 - Show top student")
        print("0 - Exit")
        choice = int(input("Your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            rollnum = input("Enter roll number: ")
            subjectscount = int(input("How many subjects? "))
            totalmarks = 0
            for i in range(1, subjectscount + 1):
                marks = int(input(f"Enter mark {i}: "))
                totalmarks += marks
            average = totalmarks/subjectscount
            grade = ""
            if 90 <= average <= 100:
                grade = "A"
            elif 80 <= average < 90:
                grade = "B"
            elif 50 <= average < 80:
                grade = "C"
            elif 0 < average <= 50:
                grade = "F"

            # rollnum = {"name": name, "marks":totalmarks, "average": average, "grade": grade}
            # students.append(rollnum)
            students[rollnum] = {"name": name, "marks":totalmarks, "average": average, "grade": grade}
            print("student added.")
        elif choice == 2:
            askrollnum = input("Enter roll number:")
            data = askRollnum(askrollnum, students)
            if data: 
                print("Student found:")
                print("Name:", data["name"])
                print("Marks:", data["marks"])
                print("Average:", data["average"])
                print("Grade:", data["grade"])
            else:
                print("Student not found")
        elif choice == 3:
            updatemarks=0
            rollnum = input("Enter roll number to update marks: ")
            student = askRollnum(rollnum, students)
            if student:
                subjectscount = int(input("How many subjects? "))
                updatemarks = 0
                for i in range(1, subjectscount + 1):
                    marks = int(input(f"Enter mark {i}: "))
                    updatemarks += marks
                average = updatemarks / subjectscount
                grade = ""
                if 90 <= average <= 100:
                    grade = "A"
                elif 80 <= average < 90:
                    grade = "B"
                elif 50 <= average < 80:
                    grade = "C"
                elif 0 <= average < 50:
                    grade = "F"
                students[rollnum].update({"marks": updatemarks, "average": average, "grade": grade})
                print("Marks updated.")
            else:
                print("Student not found")
        # elif choice == 4:
        #     for s in students:
        #         print("Students List:")
        #         for rollnum, s in students.items():
        #             print(f"- {s['name']} (Roll: {rollnum} Average: {s['average']:.2f} Grade: {s['grade']}")
        elif choice == 4:
            if students:
                print("Students List:")
                for rollnum, s in students.items():
                    print(f"- {s['name']} (Roll: {rollnum}) Average: {s['average']:.2f} Grade: {s['grade']}")
            else:
                print("No students found.")
        elif choice == 5:
            if students:
                topstudent = None
                highestavg = -1
                for rollnum, s in students.items():
                    if s['average'] > highestavg:
                        highestavg = s['average']
                        topstudent = s
                print(f"Top_student is {topstudent['name']}")
                print(f"Top_student's average is {topstudent['average']:.2f}")
                print(f"Top_student's grade is {topstudent['grade']}")
            else:
                print("Student not found")
        
        elif choice == 0:
            print("Exiting program.")
            print("Program ending")
main()




        

                











            # Enter name: Ali
# Enter roll number: 12
# How many subjects? 3