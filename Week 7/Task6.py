# import random
# print("Program starting.")
# print("Welcome to the rock-paper-scissors game!")
# username = input("Insert player name: ")
# print(f"Welcome {username}!")
# print("Your opponent is RPS-3PO.")
# print("Game starts...")

# print("Options: ")
# print("1 - Rock")
# print("2 - Paper")
# print("3 - Scissors")
# print("0 - Quit game")
# choice = int(input("Your_choice: "))
# print("Rock! Paper! Scissors! Shoot!")
# username_wins = 0
# username_lose = 0
# computer = "RPS-3PO"
# computer_wins = 0
# computer_lose = 0
# draw = 0

# if choice == 1:
#     print("#########################")
#     print(f"{username} chose rock.")
#     print("")
#     print("    _______")
#     print("---'   ____)")
#     print("      (_____)")
#     print("      (_____)")
#     print("      (____)")
#     print("---.__(___)")

# elif choice == 2:
#     print("#########################")
#     print(f"{username} chose paper.")
#     print("")
#     print("     _______")
#     print("---'    ____)____")
#     print("           ______)")
#     print("       __________)")
#     print("         _______)")
#     print("---.__________)")
# elif choice == 3:
#     print("#########################")
#     print(f"{username} chose scissor.")
#     print("")
#     print("    _______")
#     print("---'   ____)____")
#     print("          ______)")
#     print("       __________)")
#     print("      (____)")
#     print("---.__(___)")
# elif choice == 0:
#     print("Results:")
#     print(f"{username} - wins\({username_wins}\), losses\({username_lose}\), draws\({draw}\)")
#     print(f"{computer} - wins\({computer_wins}\), losses\({computer_lose}\), draws\({draw}\)")

# num = random.randint(1, 3)
# if num == 1:
#     print("#########################")
#     print("RPS-3PO chose Rock")
#     print("")
#     print("    _______")
#     print("---'   ____)")
#     print("      (_____)")
#     print("      (_____)")
#     print("      (____)")
#     print("---.__(___)")
# elif num == 2:
#     print("#########################")
#     print("RPS-3PO chose Paper")
#     print(f"{username} chose paper.")
#     print("")
#     print("     _______")
#     print("---'    ____)____")
#     print("           ______)")
#     print("       __________)")
#     print("         _______)")
#     print("---.__________)")
# elif num == 3:
#     print("#########################")
#     print("RPS-3PO chose scissor")
#     print("")
#     print("    _______")
#     print("---'   ____)____")
#     print("          ______)")
#     print("       __________)")
#     print("      (____)")
#     print("---.__(___)")



# if choice == num:
#     print("It's a draw!")
#     draw += 1

# elif (choice == 1 and num == 3) or \
#      (choice == 2 and num == 1) or \
#      (choice == 3 and num == 2):
#     print(f"{username} wins this round!")
#     username_wins += 1
#     computer_lose += 1

# elif (num == 1 and choice == 3) or \
#      (num == 2 and choice == 1) or \
#      (num == 3 and choice == 2):
#     print("RPS-3PO wins this round!")
#     computer_wins += 1
#     username_lose += 1

# else:
#     print("Invalid choice!")


import random

print("Program starting.")
print("Welcome to the rock-paper-scissors game!")
username = input("Insert player name: ")
print(f"Welcome {username}!")
print("Your opponent is RPS-3PO.")
print("Game starts...\n")

# initialize score counters
username_wins = 0
username_lose = 0
computer_wins = 0
computer_lose = 0
draw = 0
computer = "RPS-3PO"

while True:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    choice = int(input("Your choice: "))
    print("Rock! Paper! Scissors! Shoot!\n")

    if choice == 0:
        print("\nResults:")
        print(f"{username} - wins ({username_wins}), losses ({username_lose}), draws ({draw})")
        print(f"{computer} - wins ({computer_wins}), losses ({computer_lose}), draws ({draw})")
        print("\nProgram ending.")
        break

    # --- USER CHOICE DISPLAY ---
    if choice == 1:
        print("#########################")
        print(f"{username} chose rock.\n")
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)\n")

    elif choice == 2:
        print("#########################")
        print(f"{username} chose paper.\n")
        print("     _______")
        print("---'    ____)____")
        print("           ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)\n")

    elif choice == 3:
        print("#########################")
        print(f"{username} chose scissors.\n")
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)\n")

    else:
        print("Invalid choice! Try again.\n")
        continue

    # --- COMPUTER CHOICE ---
    num = random.randint(1, 3)

    if num == 1:
        print("#########################")
        print("RPS-3PO chose rock.\n")
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)\n")

    elif num == 2:
        print("#########################")
        print("RPS-3PO chose paper.\n")
        print("     _______")
        print("---'    ____)____")
        print("           ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)\n")

    elif num == 3:
        print("#########################")
        print("RPS-3PO chose scissors.\n")
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)\n")

    # --- GAME LOGIC ---
    print("#########################\n")
    if choice == num:
        print(f"Draw! Both players chose {['rock','paper','scissors'][choice-1]}.\n")
        draw += 1

    elif (choice == 1 and num == 3) or \
         (choice == 2 and num == 1) or \
         (choice == 3 and num == 2):
        print(f"{username} {['rock','paper','scissors'][choice-1]} beats RPS-3PO {['rock','paper','scissors'][num-1]}.\n")
        username_wins += 1
        computer_lose += 1

    else:
        print(f"RPS-3PO {['rock','paper','scissors'][num-1]} beats {username} {['rock','paper','scissors'][choice-1]}.\n")
        computer_wins += 1
        username_lose += 1



