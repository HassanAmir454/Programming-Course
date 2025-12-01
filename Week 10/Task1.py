# Program starting.
# Insert filename: A10_D10.txt
# # --- Vertically --- #
# 1000
# 221
# 392
# 621
# 47
# 448
# 163
# 120
# 197
# 781
# # --- Vertically --- #
# # --- Horizontally --- #
# 1000, 221, 392, 621, 47, 448, 163, 120, 197, 781
# # --- Horizontally --- #
# Program ending.
def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    print("# --- Vertically --- #")
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:      
                print(line)
    print("# --- Vertically --- #")
    print("# --- Horizontally --- #")
    with open(filename, "r") as file:
        lines = file.read().strip().split()
        number = [line.strip() for line in lines]
        print(", ".join(number))
    print("# --- Horizontally --- #")
    print("Program ending.")
    





# def main() -> None:
#     print("Program starting.")
#     filename = input("Insert filename: ")
#     print("# --- Vertically --- #")
#     with open(filename, "r") as file:
#         lines = file.readlines()
#         for line in lines:
#             line = line.strip()
#             if line:      
#                 print(line)
#     print("# --- Vertically --- #")
#     print("# --- Horizontally --- #")
#     with open(filename, "r") as file:
#         lines = file.readlines()
#         for line in lines:
#             line = line.strip()
#             if line:      
#                 print(line, end=", ")
#     print("\n# --- Horizontally --- #")
   

            
       
main()