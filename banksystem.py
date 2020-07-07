from db import fetch_manager_details
from manager import Manager
from db import fetch_client_details
from client import Client
from account import Account


def manager_signin():
    while True:
        log_in_manager_id = input("Enter your manager ID: ")
        log_in_manager_password = input("Enter password: ")
        manager_details = fetch_manager_details(log_in_manager_id,log_in_manager_password)
        if manager_details is not None:
            manager_id = manager_details[0]
            manager_password = manager_details[1]
            if log_in_manager_id == manager_id and log_in_manager_password == manager_password:
                # Successful login
                return Manager(manager_id, manager_password, manager_details[2], manager_details[3],manager_details[4],manager_details[5],manager_details[6],manager_details[7],manager_details[8],manager_details[9],manager_details[10],manager_details[11])
            print("Successful login")
            break
        else:
            print("Invalid ID or password, please try again.")  

def contact_manager():
    while True:
        try:
            contact_manager_option = int(input("Select: 1 - to request to open a new account, 2 - to request to close an existing account"))
            while contact_manager_option < 3 and contact_manager_option > 0:
                if contact_manager_option == 1:
                    print("Open a new account")
                elif contact_manager_option == 2:
                    print("Close an existing account")
            else:
                print("Error - enter option number from 1 to 2: ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return contact_manager_option
            break

# def total_balance():
    # balance sum of all possessed accounts

# def personal_details():
    # accounts table

def savings_account():
    while True:
        try:
            select_account_operation = int(input("Select: 1 - deposit, 2 - withdrawal, 3 - transfer, 4 - account details: "))
            while select_account_operation < 5 and select_account_operation > 0:
                if select_account_operation == 1:
                    print("Deposit")
        
                    # deposit will be our next function
                    break
                elif select_account_operation == 2:
                    print("Withdraw")
                    break
                elif select_account_operation == 3:
                    print("Transfer")
                    break
                elif select_account_operation == 4:
                    print("Account details")
                    break
            else:
                print("Error - enter option number from 1 to 4: ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return select_account_operation
            break

def chequing_account():
    while True:
        try:
            select_account_operation = int(input("Select: 1 - deposit, 2 - withdrawal, 3 - transfer, 4 - account details: "))
            while select_account_operation < 5 and select_account_operation > 0:
                if select_account_operation == 1:
                    print("Deposit")
                    break
                elif select_account_operation == 2:
                    print("Withdraw")
                    break
                elif select_account_operation == 3:
                    print("Transfer")
                    break
                elif select_account_operation == 4:
                    print("Account details")
                    break
            else:                             
                print("Try again, please enter option number from 1 to 4: ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
        else:
            return select_account_operation
            break

def client_account_menu():
    while True:
        try:
            select_menu_option = int(input("Select from the following menu: 1 - access chequing account, 2 - access savings account, 3 - access personal details, 4 - show balance, 5 - contact the manager: "))
            while select_menu_option < 6 and select_menu_option > 0:
                if select_menu_option == 1:
                    print("Chequing account")
                    chequing_account()
                    break
                elif select_menu_option == 2:
                    print("Savings account")
                    savings_account()
                    break
                elif select_menu_option == 3:
                    print("Personal details")
                    # personal_details(personal_info)
                    break
                elif select_menu_option == 4:
                    print("Your balance")
                    # total_balance(current_balance)
                    break
                elif select_menu_option == 5:
                    print("Contact the manager")
                    contact_manager()
            else:
                print("Try again, please enter option 1-5. ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return select_menu_option
            break

def client_signup():
    print("Please provide your personal information")
    sign_up_first_name = input("First name: ")
    sign_up_last_name = input("Last name: ")
    sign_up_occupation = input("Occupation: ")
    sign_up_age = input("Age: ")
    sign_up_gender = input("Gender: ")
    sign_up_street = input("Street: ")
    sign_up_city = input("City: ")
    sign_up_province = input("Province: ")
    sign_up_postal_code = input("Postal Code: ")
    sign_up_phone = input("Phone: ")
    sign_up_email = input("E-mail: ")
    while True:
        try:  
            sign_up_account_type = int(input("Select account type you wish to open: 1 - chequing, 2 - savings, 3 - both: "))
            while sign_up_account_type > 0 and sign_up_account_type < 4:
                if sign_up_account_type == 1:
                    print("Chequing account")
                    break
                elif sign_up_account_type == 2:
                    print("Savings account")
                    break
                elif sign_up_account_type == 3:
                    print("Chequing and Savings account")
                    break
            else:
                print("Try again, please enter option 1-3.")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return sign_up_account_type
            break

def client_signin():
    while True:
        log_in_client_id = input("Enter your client ID: ")
        log_in_client_password = input("Enter password: ")
        client_details = fetch_client_details(log_in_client_id,log_in_client_password)
        if client_details is not None:
            client_id = client_details[0]
            client_password = client_details[1]
            if log_in_client_id == client_id and log_in_client_password == client_password:
                # Successful login
                return Client(client_id, client_password, client_details[2], client_details[3],client_details[4],client_details[5],client_details[6],client_details[7],client_details[8],client_details[9],client_details[10],client_details[11])
            print("Successful login") 
            client_account_menu()
            break   
        else:
            print("Invalid ID or password, please try again.")
 
def client_signin_signup():
    while True:
        try:
            sign_in_sign_up = int(input("Press 1 to sign up / Press 2 to sign in: "))
            while sign_in_sign_up < 3 and sign_in_sign_up > 0:
                if sign_in_sign_up == 1:
                    print("Sign up - create a new client account")
                    client_signup()
                    break
                elif sign_in_sign_up == 2:
                    print("Sign in to an existing client account")
                    client_signin()
                    break
            else:
                print("Try again, please enter 1 to sign up or 2 to sign in. ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return sign_in_sign_up
            break

def role_verification():
    while True:
        try:
            role_number = int(input("Select your role: 1 - client, 2 - manager, 3 - maintenance: "))  
            while role_number > 0 and role_number < 4:
                if role_number == 1:
                    print("Welcome to the client account")
                    client_signin_signup()
                    break
                
                elif role_number == 2:
                    print("Welcome to the manager account")
                    manager = manager_signin()
                    break
                 
                elif role_number == 3:
                    print("Welcome to the maintenance account")
                    # maintenance = maintenance_signin()
                    
                    break
            else:
                print("Try again, enter 1 for client, 2 for manager, or 3 for maintenance: ")
                continue
            break
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return role_number
            break

def main():
    print('===============================================')
    print("             Welcome to Bank of JOJO           ")
    print('===============================================')
    print(role_verification())
if __name__ == "__main__":
    main()