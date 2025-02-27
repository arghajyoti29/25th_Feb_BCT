from prettytable import PrettyTable  

def get_user_input():
    email = input("\nEnter Email ID: ").strip()
    if email in user_data:
        print("User already exists! Try logging in.\n")
        return None, None
    
    name = input("Enter Name: ").strip()
    password = input("Enter Password: ").strip()
    age = input("Enter Age: ").strip()
    role = input("Enter Role: ").strip()
    
    return email, {"name": name, "password": password, "age": age, "role": role}

def signup():
    email, details = get_user_input()
    if email and details:
        user_data[email] = details
        print("\nSignup successful!")

def login():
    email = input("\nEnter Email ID: ").strip()
    password = input("Enter Password: ").strip()

    if email in user_data and user_data[email]["password"] == password:
        print(f"\nLogin successful! Welcome, {user_data[email]['name']}.")
    else:
        print("\nInvalid email or password. Please try again.")

def show_data():
    if not user_data:
        print("\nNo user data available.")
    else:
        print("\nUser Data:")
        table = PrettyTable(["Name", "Email", "Age", "Role"])
        for email, details in user_data.items():
            table.add_row([details["name"], email, details["age"], details["role"]])
        print(table)  

def delete_user():
    email = input("\nEnter Email ID to delete: ").strip()
    if email in user_data:
        del user_data[email]
        print("\nUser deleted successfully.")
    else:
        print("\nUser not found.")

user_data = {}

while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Show User Data")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        show_data()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("\nExiting portal. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")