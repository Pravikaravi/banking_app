import os

def create_admin():
    if not admin_exists():
        with open("Users.txt", "a") as file:
            file.write("U00000    | Admin  | Admin@123   | admin\n")
        print("Admin account created successfully!")
        print("Admin User ID: U00000")
        print("Secret pin must be given to admin manually.\n")

def admin_exists():
    if not os.path.exists("Users.txt"): 
        return False
    with open("Users.txt", "r") as file:
        for line in file:
            if "admin" in line.strip().lower(): # Check any line in the file has the word admin
                return True
    return False

def generate_user_id():
    digit = 0
    if os.path.exists("Users.txt"):
        with open("Users.txt", "r") as file:
            digit = len(file.readlines())
    user_id = "U" + str(digit).zfill(5)
    return user_id


def create_customer(user_id, name, password, role="user"):
    with open("Users.txt", "a") as file:
        file.write(f"{user_id:<10}| {name:<7}| {password:<12}| {role}\n")
    print("Customer created successfully!")

def verify_login(user_id, password):                          #Check user_id and password match
    if not os.path.exists("Users.txt"):                    #check Users.txt exists or not
        return None
    with open("Users.txt", "r") as file:                   #Open file in read mode
        for line in file:                                     #reads line by line
            parts = [p.strip() for p in line.split("|")]      #Split ech line using | as the separtor.    Ex: U00001 | Pravi | 1234 | "user"       (p is part of parts)
                                                                                                        # parts = ["U00001" , "Pravi" , "1234" , "user"]
            if len(parts) == 4 and parts[0] == user_id and parts[2] == password:                        # Make sure the line has 4 parts, and check part[0] == user_id and part[2] == password                         
                return parts[3]                                                                         # Return role (admin/user)
    return None


def generate_customer_id():
    digit = 1
    if os.path.exists("Customers.txt"):
        with open("Customers.txt", "r") as file:
            digit = len(file.readlines())
    customer_id = "C" + str(digit).zfill(5)
    return customer_id

def create_customer_file(customer_id, name, user_id):
    with open("Customers.txt", "a") as file:
        file.write(f"{customer_id:<10}| {name:<12}| {user_id:<12}\n")


def show_all_customers():
    if os.path.exists("Users.txt"):
        print(f"{'User ID':<10}| {'Name':<12}| {'Password':<12}| {'Role'}")
        print("-" * 50)
        with open("Users.txt", "r") as file:
            for line in file:
                parts = [p.strip() for p in line.strip().split("|")]
                if len(parts) == 4:
                    print(f"{parts[0]:<10}| {parts[1]:<9}| {parts[2]:<13}| {parts[3]}")
    else:
        print("No customer data found.")


def generate_account_id():
    digit = 1
    if os.path.exists("Accounts.txt"):
        with open("Accouts.txt", "r") as file:
            digit = len(file.readlines())
    account_id = "AC" + str(digit).zfill(5)
    return account_id

def create_account_file(account_id, user_id, customer_id, balance):
    with open("Accounts.txt", "a") as file:
        file.write(f"{account_id:<10}| {user_id:<10}| {customer_id:<10}| {balance:<50}\n")
    
# def view_user_details(user_id):
#     name = ""
#     role = ""
#     print("\n--- Your Profile Details ---")
    
#     # Fetch user details from Users.txt
#     if os.path.exists("Users.txt"):
#         with open("Users.txt", "r") as f:
#             for line in f:
#                 parts = [p.strip() for p in line.strip().split("|")]
#                 if len(parts) == 4 and parts[0] == user_id:
#                     name = parts[1]
#                     role = parts[3]
#                     print(f"User ID   : {parts[0]}")
#                     print(f"Name      : {parts[1]}")
#                     print(f"Password  : {parts[2]}")
#                     print(f"Role      : {parts[3]}")
#                     break

#     # Fetch some user details from Customers.txt
#     if os.path.exists("Customers.txt"):
#         with open("Customers.txt", "r") as f:
#             for line in f:
#                 parts = [p.strip() for p in line.strip().split("|")]
#                 if len(parts) == 3 and parts[2] == user_id:
#                     print(f"Customer ID: {parts[0]}")
#                     break

def view_all_balances():
    if not os.path.exists("Accounts.txt") and not os.path.exists("Users.txt"):
        print("Accouts file not found")
        return
    
    user_names = {}
    with open("Users.txt","r") as Users_file:
        for line in Users_file:
            parts = [p.strip() for p in line.strip().split("|") ]
            if len(parts) >= 2:
                user_id = parts[0]
                user_name = parts[1]
                user_names[user_id] = user_name

    print("\n-------------- All User Balances --------------")
    print(f"\n{"Account_Number":<10} | {"       Name":<20} | {"Balance"}")


# ----------------- FOR ADMIN ----------------- #

def admin_dashboard():
    while True:
        print("\nAdmin Dashboard:")
        print("1. Create new customer")
        print("2. View all users")
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
                account_id = generate_account_id()
                user_id = generate_user_id()
                customer_id = generate_customer_id()
                create_customer(user_id, name, password, role="user")
                create_customer_file(customer_id, name, user_id)
                create_account_file(account_id, user_id, customer_id, balance)
            elif choice == 2:
                show_all_customers()
            elif choice == 3:
                view_all_balances()
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a number.")

create_admin()  # Run once at start (Auto create user_id for Admin)

# ----------------- FOR USER ----------------- #

def user_panel():
    while True:
            print("1. View your details")
            print("2. View your balance")
            print("3. Withdraw money")
            print("4. Deposit money")
            print("5. Money transfer")
            print("6. View transaction history")
            print("7.Exit")
            try:
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    view_user_details()
                else :
                    print("Invlid choice")

            except ValueError:
                print(" Enter numbers only!")


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
            pin = input("Enter admin password: ")
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
                user_panel()
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
