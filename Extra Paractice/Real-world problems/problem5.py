# Program starting.

# Options:
# 1 - Add patient
# 2 - Discharge patient
# 3 - Search patient
# 4 - Show admitted patients
# 5 - Save records
# 6 - Load records
# 0 - Exit
# Your choice: 1

# Enter name: Hassan
# Enter age: 22
# Enter disease: Fever
# Patient admitted.

# Options:
# 1 - Add patient
# 2 - Discharge patient
# 3 - Search patient
# 4 - Show admitted patients
# 5 - Save records
# 6 - Load records
# 0 - Exit
# Your choice: 1

# Enter name: Sara
# Enter age: 30
# Enter disease: Flu
# Patient admitted.

# Options:
# 1 - Add patient
# 2 - Discharge patient
# 3 - Search patient
# 4 - Show admitted patients
# 5 - Save records
# 6 - Load records
# 0 - Exit
# Your choice: 4

# Admitted Patients:
# - Hassan (22) — Fever
# - Sara (30) — Flu

# Options:
# 1 - Add patient
# 2 - Discharge patient
# 3 - Search patient
# 4 - Show admitted patients
# 5 - Save records
# 6 - Load records
# 0 - Exit
# Your choice: 2

# Enter patient name to discharge: Hassan
# Patient discharged.

# Options:
# 1 - Add patient
# 2 - Discharge patient
# 3 - Search patient
# 4 - Show admitted patients
# 5 - Save records
# 6 - Load records
# 0 - Exit
# Your choice: 0

# Exiting program.
# Program ending.

def options():
    print("\nOptions:")
    print("1 - Add patient")
    print("2 - Discharge patient")
    print("3 - Search patient")
    print("4 - Show admitted patients")
    print("5 - Save records")
    print("6 - Load records")
    print("0 - Exit")
Patients = []
def main() -> None:
    print("Program starting.")
    while True:
        options()
        choice = int(input("Your choice: "))
        if choice == 1:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            disease = input("Enter disease: ")
            print("Patient admitted.")
            Patients.append({
                "name": name,
                "age": age,
                "disease": disease
            })
        elif choice == 2:
            namee= input("Enter patient name: ")
            found = False
            for patient in Patients:
                if patient["name"] == namee:
                    Patients.remove(patient)
                    print("Patient discharged.")
                    found = True
                    break
            if not found:
                print("Patient not found.")
        elif choice == 3:
            nameee = input("Enter patient name: ")
            found = False
            for patient in Patients:
                if patient["name"] == nameee:
                    print(f"Patient found: {patient['name']} ({patient['age']}) — {patient['disease']}")
                    found = True
                    break
            if not found:
                print("Patient not found.")
        elif choice == 4:
            print("\nAdmitted Patients:")
            if not Patients == "":

                for patient in Patients:
                    print(f"- {patient['name']} ({patient['age']}) — {patient['disease']}")
            else:
                print("No patients available")
        elif choice == 5:
            if not Patients == "":
                with open("patients.txt", "w") as file:
                    for patient in Patients:
                        file.write(f"{patient['name']},{patient['age']},{patient['disease']}\n")
                print("Saving records...")
                print("Records saved.")
            else:
                print("Saving records...")
                print("Data not found")
        elif choice == 6:
            try:
                with open("patients.txt", "r") as f:
                    for line in f:
                        name, age, disease = line.strip().split(",")
                        Patients.append({"name": name, "age": int(age), "disease": disease})
                        print("Records loaded.")

            except FileNotFoundError:
                print("File not found")
        elif choice == 0:
            print("Exiting Program")
            break
main()




