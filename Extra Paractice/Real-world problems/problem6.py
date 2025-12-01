# Program starting.

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 1

# Enter book title: Harry Potter
# Enter author: J.K. Rowling
# Enter genre: Fantasy
# Enter copies: 5
# Book added successfully.

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 2

# Enter member name: Ali
# Enter member ID: 101
# Member added successfully.

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 3

# Enter member ID: 101
# Enter book title: Harry Potter
# Book borrowed successfully.

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 6

# All Books:
# - Harry Potter | J.K. Rowling | Fantasy | Copies: 4

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 7

# All Members:
# - Ali (ID: 101) | Borrowed: Harry Potter

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 8

# Borrow History:
# Ali (ID: 101) borrowed 'Harry Potter' on 2025-02-14 13:45:22

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 4

# Enter member ID: 101
# Enter book title: Harry Potter
# Book returned successfully.

# Options:
# 1 - Add Book
# 2 - Add Member
# 3 - Borrow Book
# 4 - Return Book
# 5 - Search Book
# 6 - Show All Books
# 7 - Show All Members
# 8 - Borrow History
# 9 - Save Records
# 10 - Load Records
# 0 - Exit
# Your choice: 0

# Exiting program.
# Program ending.
import json
from datetime import datetime



def options():
    print("1 - Add Book")
    print("2 - Add Member")
    print("3 - Borrow Book")
    print("4 - Return Book")
    print("5 - Search Book")
    print("6 - Show All Books")
    print("7 - Show All Members")
    print("8 - Borrow History")
    print("9 - Save Records")
    print("10 - Load Records")
    print("0 - Exit")

Library = []
Members = []
Borrowhistory = []



def main() -> None:
    print("Program starting.")
    while True:
        options()
        choice = int(input("Your choice: "))
        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre:")
            copies = input("Enter copies:")
            print("Book added sucessfully")
            Library.append({
                "title": title,
                "author": author,
                "genre": genre,
                "copies": copies
            })
        elif choice == 2:
            membername = input("Enter member name: ")
            memberid = int(input("Enter member ID: "))
            print("Member added successfully.")
            Members.append({
                "name": membername,
                "member Id": memberid
            })
        elif choice == 3:
            memberid = int(input("Enter member ID: "))
            booktitle = input("Enter book title: ")
            print("Book borrowed successfully.")
            Borrowhistory.append({
                
                "memberid" : memberid,
                "book title" : booktitle,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        elif choice == 6:
            print("\nAll Books:")
            for book in Library:
                print(f"- {book['title']} | {book['author']} | {book['genre']} | Copies: {book['copies']}")
        elif choice == 7:
            print("\nAll Members:")
            for member in Members:
                print(f"- {member['name']} | {member['member Id']}")
        elif choice == 8:
            print("Borrow history:")
            for member in Borrowhistory:
                for m in Members:
                    if m['member Id'] == member['memberid']:
                        member_name = m['name']
                        break

                print(f"{member_name} ({member['memberid']})  borrowed {member['book title']} on {member['date']} ")
        elif choice == 4:
            memberid = int(input("Enter member ID: "))
            booktitle = input("Enter book title: ")
            
            for bor in Borrowhistory:
                if bor['memberid'] == memberid:
                    Borrowhistory.remove(bor)
                    print("Book returned successfully.")
                else:
                    print("No such borrow record found.")
        elif choice == 5:
            keyword = input("Enter some keyword to search book")
            for book in Library:
                if keyword == book['title'] or keyword == book['genre'] or keyword == book['author']:
                    print(f" {book['title']} by author: {book['author']} genre: {book['genre']} ")
                else:
                    print("No search found.")
        elif choice == 9:
            data = {
            "Library": Library,
            "Members": Members,
            "Borrowhistory": Borrowhistory
             }



            with open("library.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Records saved successfully.")

        elif choice == 10:
            try:
                with open("library.json", "r") as file:
                    data = json.load(file)
                    Library[:] = data["Library"]
                    Members[:] = data["Members"]
                    Borrowhistory[:] = data["Borrowhistory"]
                print("Records loaded successfully.")
            except FileNotFoundError:
                print("No saved data found.")



        elif choice == 0:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Try again.")

main()
            

                






            # Enter member ID: 101
# Enter book title: Harry Potter
# Book returned successfully.


            
# All Books:
# - Harry Potter | J.K. Rowling | Fantasy | Copies: 4











# 






# Enter book title: Harry Potter
# Enter author: J.K. Rowling
# Enter genre: Fantasy
# Enter copies: 5
# Book added successfully.