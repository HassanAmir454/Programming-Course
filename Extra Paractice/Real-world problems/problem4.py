# Program starting.

# Options:
# 1 - Add movie
# 2 - Book ticket
# 3 - Cancel ticket
# 4 - View movies
# 5 - Save & Exit
# Your choice: 1

# Enter movie title: Avatar
# Enter total seats: 100
# Movie added.

# Options:
# 1 - Add movie
# 2 - Book ticket
# 3 - Cancel ticket
# 4 - View movies
# 5 - Save & Exit
# Your choice: 2

# Enter movie title: Avatar
# How many tickets? 3
# Booking successful. Seats left: 97

# Options:
# 1 - Add movie
# 2 - Book ticket
# 3 - Cancel ticket
# 4 - View movies
# 5 - Save & Exit
# Your choice: 4

# Movies:
# - Avatar | Total: 100 | Booked: 3 | Available: 97

# Options:
# 1 - Add movie
# 2 - Book ticket
# 3 - Cancel ticket
# 4 - View movies
# 5 - Save & Exit
# Your choice: 5

# Saving data...
# Data saved.
# Program ending.

def options():
    print("\nOptions:")
    print("1 - Add movie")
    print("2 - Book ticket")
    print("3 - Cancel ticket")
    print("4 - View movies")
    print("5 - Save & Exit")
Movies = []
def main() -> None:
    print("Program starting.")
    while True:
        options()
        choice = int(input("Your choice: "))
        if choice == 1:
            name = input("Enter movie title: ")
            seats = input("Enter total seats: ")
            print("Movie added.")
            Movies.append({
                "Name": name,
                "Total" : int(seats),
                "Booked" : 0
                })
        elif choice == 2:
            namee = input("Enter movie title: ")
            tickets = int(input("How many tickets?"))
            for movie in Movies:
                if movie["Name"] == namee:
                    seatsleft = movie['Total'] - movie['Booked']
                    if seatsleft >= tickets:
                        movie['Booked'] += tickets
                        print(f"Booking successful. Seats left: {seatsleft - tickets}")
                    else:
                        print("Not enough seats available.")
                else:
                    print("Movie not found")
                    
        elif choice == 3:
            nameee = input("Enter movie title: ")
            cancel_no = int(input(" How many tickets to cancel?"))
            
            for movie in Movies:
                if movie['Name'] == nameee:

                    
                    if movie['Booked'] >= cancel_no:
                        movie['Booked'] -= cancel_no

                        print(f"Cancellation successful. Seats left: {movie['Total'] - movie['Booked']}")
                    else:
                        print("You have booked less tickets")
                else:
                    print("Movie not found")
        elif choice == 4:
            print("\nMovies:")
            for movie in Movies:
                seatsavaiable = movie['Total'] - movie['Booked']
                print(f" - {movie['Name']} | Total: {movie['Total']} | Booked: {movie['Booked']} | Available: {seatsavaiable}")
        elif choice == 5:
            
            with open("movies.txt", "w") as file:
                for movie in Movies:
                    file.write(str(Movies) + "\n")

                
            print("\nSaving data...")
            print("File saved")
            print("Program ending.")
main()

        








