import hashlib
CREDENTIALS_FILE = "credentials.txt"
def showOptions() -> None:
    print("\nOptions:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def register_user():
    username = input("Insert username: ")
    password = input("Insert password: ")
    hashed_pass = hash_password(password)
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{username};{hashed_pass}\n")
    print("User registration completed!")

def login_user():
    username = input("Insert username: ")
    password = input("Insert password: ")
    hashed_pass = hash_password(password)
    with open(CREDENTIALS_FILE, "r") as f:
        for index, line in enumerate(f, start=0):
            stored_username, stored_password = line.strip().split(";")
            if stored_username == username and stored_password == hashed_pass:
                print("Authentication successful!")
                user_menu(index, username)
                return
    print("Invalid username or password.")

def user_menu(index, username):
    while True:
        print("\nUser menu:")
        print("1 - View profile")
        print("2 - Change password (not implemented)")
        print("0 - Logout")
        choice2 = int(input("Your choice:"))
        if choice2 == 0:
            print("Logging out...")
            break
        if choice2 == 1:
            print(f"Profile ID {index} - {username}")
        if choice2 == 2:
            print("Not implemented")
        

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = int(input("Your choice: "))
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            login_user()
        elif choice == 2:
            register_user()

                    
    print("Program ending.")
if __name__ == "__main__":
    main()

        





