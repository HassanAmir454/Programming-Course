# Program starting.

# Loading menu...
# Menu loaded.

# Menu:
# 1 - Burger (5.0 €)
# 2 - Fries (3.0 €)
# 3 - Pizza (8.5 €)
# 0 - Finish order

# Choose item number: 1
# Quantity: 2
# Added to order.

# Choose item number: 3
# Quantity: 1
# Added to order.

# Choose item number: 0

# Calculating bill...
# Subtotal: 18.5 €
# Tax (16%): 2.96 €
# Final amount: 21.46 €

# Save receipt to file? (yes/no): yes
# Enter filename: receipt.txt
# Receipt saved.

# Program ending.
def calculateBiling(subtotal):
    totaltax = subtotal * 0.16
    finalamount = subtotal+totaltax
    print(f"Subtotal: {subtotal} €")
    print(f"Tax (16%): {totaltax:.2f} €")
    print(f"Final amount: {finalamount:.2f} €")
    receipt = (
        f"Subtotal: {subtotal} €\n"
        f"Tax (16%): {totaltax:.2f} €\n"
        f"Final amount: {finalamount:.2f} €\n"
    )
    return receipt

def main() -> None:
    print("Program starting.")
    print("Loading menu...")
    print("Menu loaded.")
    subtotal = 0
    
    

    while True:
        print("\nMenu:")
        print("1 - Burger (5.0 €)")
        print("2 - Fries (3.0 €)")
        print("3 - Pizza (8.5 €)")
        print("0 - Finish order")
        choice = int(input("Choose item number: "))
        
        if choice == 1:
            quantity = int(input("Quantity: "))
            total = 5.0 * quantity
            subtotal+= total
            print("Added to order.")
        elif choice == 2:
            quantity = int(input("Quantity: "))
            total = 3.0 * quantity
            subtotal+= total
            print("Added to order.")
        elif choice == 3:
            quantity = int(input("Quantity: "))
            total = 8.5 * quantity
            subtotal+= total
            print("Added to order.")
        
        elif choice == 0:
            print("\nCalculating bill...")
            calculating = calculateBiling(subtotal)
            receipt = input("\nSave receipt to file? (yes/no): ").lower()
            if receipt == "yes":
                filename = input("Enter file name: ")
                with open(filename, "a") as file:
                    file.write(calculating)
                print("Receipt saved.")
                print("\nProgram ending.")
                break
            else:
                print("Ok, Thanks for order.")
                print("\nProgram ending.")
                break

        else:
            print("Invalid input")

main()
