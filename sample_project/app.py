# app.py
# Simple user registration/login system (insecure by default)
import hashlib
import re
users = {}
#Task 2.1 Input Validation. Validate user input for registration and login. Ensure that usernames are alphanumeric and between 3 to 20 characters long. Passwords should be hashed before storing."""
def register():
    print("=== Register ===")
    username = input("Enter username: ")
    if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
        print("Invalid username")
        exit()
#Task 2.2 Password Hashing. Use a secure hashing algorithm (e.g., SHA-256)
# to hash passwords before storing them. This prevents storing plaintext
#  passwords and enhances security.
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Vulnerable: storing plaintext password
    users[username] = hashed_password
    print("Hashed password:", hashed_password)
    print("Users registered successfully!")

def login():
    print("=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Vulnerable: plain comparison, no hashing
    if username in users and users[username] == hashed_password:
        print("Login successful!")
    else:
        print("Login failed!")
# Task 2.3 Error Handling. Implement error handling to manage unexpected
#  situations gracefully.
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option")
# Task 2.3 Secure Error Handling. Implement error handling to manage unexpected
#  situations gracefully.
if __name__ == "__main__":
    
    try:
        # vulnerable code
        main()
    except Exception:
        print("An error occurred. Please try again.")

    
