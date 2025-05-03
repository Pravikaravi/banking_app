import os

def create_admin():
    if not admin_exists():
        with open("User.txt", "a") as file:
            file.write("U00000    |     Admin  | Admin@123   | admin\n")
        print("Admin account created successfully!")
        print("Admin User ID: U00000")
        print("Secret pin must be given to admin manually.\n")

def admin_exists():
    if not os.path.exists("User.txt"): 
        return False
    with open("User.txt", "r") as file:
        for line in file:
            if "admin" in line.strip().lower(): # Check any line in the file has the word admin
                return True
    return False

def generate_user_id():
    digit = 0
    if os.path.exists("User.txt"):
        with open("User.txt", "r") as file:
            digit = len(file.readlines())
    user_id = "U" + str(digit).zfill(5)
    return user_id


def create_customer(user_id, name, password, role="user"):
    with open("User.txt", "a") as file:
        file.write(f"{user_id:<10}| {name:<7}| {password:<12}| {role}\n")
    print("Customer created successfully!")

def verify_login(user_id, password):                          #Check user_id and password match
    if not os.path.exists("User.txt"):                    #check User.txt exists or not
        return None
    with open("User.txt", "r") as file:                   #Open file in read mode
        for line in file:                                     #reads line by line
            parts = [p.strip() for p in line.split("|")]      #Split ech line using | as the separtor.    Ex: U00001 | Pravi | 1234 | "user"       (p is part of parts)
                                                                                                        # parts = ["U00001" , "Pravi" , "1234" , "user"]
            if len(parts) == 4 and parts[0] == user_id and parts[2] == password:                        # Make sure the line has 4 parts, and check part[0] == user_id and part[2] == password                         
                return parts[3]                                                                         # Return role (admin/user)
    return None

def show_all_customers():
    if os.path.exists("User.txt"):
        print(f"{'User ID':<10}| {'Name':<12}| {'Password':<12}| {'Role'}")
        print("-" * 50)
        with open("User.txt", "r") as file:
            for line in file:
                parts = [p.strip() for p in line.strip().split("|")]
                if len(parts) == 4:
                    print(f"{parts[0]:<10}| {parts[1]:<9}| {parts[2]:<13}| {parts[3]}")
    else:
        print("No customer data found.")


def generate_customer_id():
    digit = 1
    if os.path.exists("Customer.txt"):
        with open("Customer.txt", "r") as file:
            digit = len(file.readlines())
    customer_id = "C" + str(digit).zfill(5)
    return customer_id

def create_customer_file(customer_id, name, user_id):
    with open("Customer.txt", "a") as file:
        file.write(f"{customer_id:<10}| {name:<12}| {user_id:<12}\n")

def create_account_file(user_id, customer_id, balance):
    with open("Account.txt", "a") as file:
        file.write(f"{user_id:<10}| {customer_id:<10}| {balance:<50}\n")
    


# ----------------- FOR ADMIN ----------------- #

def admin_dashboard():
    while True:
        print("\nAdmin Dashboard:")
        print("1. Create new customer")
        print("2. View all customers")
        print("3. View all customer balance")
        print("4. Search customer")
        print("5. Delete customer")
        print("6. View all transactions")
        print("7. Exit admin dashboard")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter customer name: ")
                password = input("Set temporary password: ")
                balance = float(input("Enter initial balance: "))
                user_id = generate_user_id()
                customer_id = generate_customer_id()
                create_customer(user_id, name, password, role="user")
                create_customer_file(customer_id, name, user_id)
                create_account_file(user_id, customer_id, balance)
            elif choice == 2:
                show_all_customers()
            elif choice == 3:
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a number.")

create_admin()  # Run once at start (Auto create user_id for Admin)

# ----------------- FOR USER ----------------- #

while True:
    print("-" * 50) 
    print("      Welcome to the Mini Bank System",)
    print("-" * 50) 
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            u_id = input("Enter admin user ID: ")
            pin = input("Enter admin pin: ")
            role = verify_login(u_id, pin)
            if role == "admin":
                print(f"\nWelcome Admin {u_id}!")
                admin_dashboard()
            else:
                print("Incorrect admin credentials.")

        elif choice == 2:
            u_id = input("Enter your user ID: ")
            pw = input("Enter your password: ")
            role = verify_login(u_id, pw)
            if role == "user":
                print(f"\nWelcome User {u_id}!")
            elif role == "admin":
                print("This is an admin account. Use Admin Login.")
            else:
                print("Invalid user id or password.")

        elif choice == 3:
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try 1–3.")

    except ValueError:
        print(" Enter numbers only!")