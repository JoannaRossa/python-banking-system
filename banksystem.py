from db import fetch_manager_details, fetch_client_details, insert_client_form_details, fetch_client_form_details, fetch_account_details, fetch_all_accounts, insert_transactions
from manager import Manager
from client import Client
from account import Account
from transactions import *


def client_return_to(client):
    while True:
        try:
            return_to=int(input("Select from the following menu: 1 - return to client account menu, 2 - end your session: "))
            while return_to < 3 and return_to > 0:
                if return_to == 1:
                    client_account_menu(client)
                    break
                elif return_to == 2:
                    main()
                    break
            else:
                print("Try again, please enter option 1 or 2.")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return return_to
            break
def manager_account_menu():
    while True:
        try:
            select_menu_option=int(input("Select from the following menu: 1 - view account requests, 2 - close an existing account: "))
            while select_menu_option < 3 and select_menu_option > 0:
                if select_menu_option == 1:
                    print("Account creation requests")
                    open_new_account()
                    break
                elif select_menu_option == 2:
                    print("Account closure requests")
                    close_existing_account()
                    break
            else:
                print("Try again, please enter option 1 or 2.")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return select_menu_option
            break

def manager_signin():
    while True:
        log_in_manager_id = input("Enter your manager ID: ")
        log_in_manager_password = input("Enter password: ")
        manager_details = fetch_manager_details(log_in_manager_id,log_in_manager_password)
        if manager_details is not None:
            manager_id = manager_details[0]
            manager_password = manager_details[1]
            if log_in_manager_id == str(manager_id) and log_in_manager_password == str(manager_password):
                return Manager(manager_id, manager_password, manager_details[2], manager_details[3],manager_details[4],manager_details[5],manager_details[6],manager_details[7],manager_details[8],manager_details[9],manager_details[10],manager_details[11]) 
        else:
            print("Invalid ID or password, please try again.")  

def close_existing_account():
    while True:
        try:
            close_account_option = int(input("Select: 1 - to close chequing account, 2 - to close savings account, 3 - to close both accounts (close client account with Bank of JOJO): "))
            while close_account_option < 4 and close_account_option > 0:
                if close_account_option == 1:
                    print("Close chequing account")
                    # client_chequing_account = delete
                    break
                elif close_account_option == 2:
                    print("Close savings account")
                    break
                elif close_account_option == 3:
                    print("Close both accounts (close client account with Bank of JOJO")
                    delete_client_details(client_id, client_password)
                    break
            else:
                print("Error - enter option number from 1 to 2: ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return close_account_option
            break 

    # delete client details at the particular account number


    # delete client profile entirely by client id and client password
    delete_client_details(client_id, client_password)
def open_new_account():
    while True:
        try:
            open_account_option = int(input("Select: 1 - to open chequing account, 2 - to open savings account, 3 - to open both accounts: "))
            while open_account_option < 4 and open_account_option > 0:
                if open_account_option == 1:
                    print("Open chequing account")
                    # client_chequing_account = delete
                    break
                elif open_account_option == 2:
                    print("Open savings account")
                    break
                elif open_account_option == 3:
                    print("Open both accounts")
                    break
            else:
                print("Error - enter option number from 1 to 2: ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return open_account_option
            break 

    # see requests from existing clients

    # # see requests from new clients
    # display_new_client_requests = fetch_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender, sign_up_street,sign_up_city, sign_up_province,sign_up_postal_code, sign_up_phone,sign_up_email,sign_up_account_type)
    # if display_new_client_requests is not None:
        # pass       
#     # if client exists in the db
#     client_details = fetch_client_details(client_id, client_password)
#     # elif client does not exist
#     # and assign client to account he chosen
#     client_form_details = fetch_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender, sign_up_street,sign_up_city, sign_up_province,sign_up_postal_code, sign_up_phone,sign_up_email)
#     generate_login_and_password()
def contact_manager():
    while True:
        try:
            contact_manager_option = int(input("Select: 1 - to request to open a new account, 2 - to request to close an existing account: "))
            while contact_manager_option < 3 and contact_manager_option > 0:
                if contact_manager_option == 1:
                    print("Open a new account")
                    # client_form_detail = fetch_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender, sign_up_street,sign_up_city, sign_up_province,sign_up_postal_code, sign_up_phone,sign_up_email,sign_up_account_type)
                    open_new_account()
                    break
                elif contact_manager_option == 2:
                    print("Close an existing account")
                    close_existing_account()
                    break
            else:
                print("Error - enter option number from 1 to 2: ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return contact_manager_option
            break


def generate_login_and_password():
    # manager will generate unique login and password for user
    # once generated, give it to the user and let him sign in
    client_signin()

def choose_new_account_type():
    while True:
        try:  
            sign_up_account_type = int(input("Select account type you wish to open: 1 - chequing, 2 - savings, 3 - both: "))
            while sign_up_account_type > 0 and sign_up_account_type < 4:
                if sign_up_account_type == 1:
                    print("Chequing account")

                    # create new db for chequing account
                    break
                elif sign_up_account_type == 2:
                    print("Savings account")
                    savings_account()
                    # create new db for savings account
                    break
                elif sign_up_account_type == 3:
                    print("Chequing and Savings account")
                    # create new db for chequing account and create new db for savings account
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

def client_signup_form():
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
    # intert input into "input database"
    sign_up_account_type = choose_new_account_type()
    insert_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender,sign_up_street,sign_up_city,sign_up_province,sign_up_postal_code,sign_up_phone,sign_up_email, sign_up_account_type)
    

def total_balance():
    # balance sum of all possessed accounts
    pass

def personal_details():
    # accounts table
    pass

# WORK HERE WITH existing DB AND CLASSES
def savings_account(client):
    while True:
        try:
            select_account_operation = int(input("Select: 1 - deposit, 2 - withdrawal, 3 - transfer, 4 - account details, 5 - savings account balance: "))
            while select_account_operation < 5 and select_account_operation > 0:
                if select_account_operation == 1:
                    print("Deposit")
                    deposit(account_number)
                    # deposit will be our next function
                
                    break
                elif select_account_operation == 2:
                    print("Withdraw")
                    # withdrawal will be our next function
                    
                    break
                elif select_account_operation == 3:
                    print("Transfer")
                    # transfer will be our next function
                    
                    break
        
                elif select_account_operation == 4:
                    print("Account details")
                    print(' number     status  type      client ID balance')
                    account_details = fetch_account_details(client.client_id, 'Savings')
                    print(account_details)
                    # account_saving = Saving()
                    # account details will be our next function
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
        
# WORK HERE WITH existing DB AND CLASSES
def chequing_account(client):
    while True:
        try:
            select_account_operation = int(input("Select: 1 - deposit, 2 - withdrawal, 3 - transfer, 4 - account details, 5 - chequing account balance: "))
            while select_account_operation < 6 and select_account_operation > 0:
                if select_account_operation == 1:
                    print("Deposit")
                    while True:
                        try:
                            transaction_amount = float(input("Enter amount you wish to deposit: "))
                            account_balance += transaction_amount
                            insert_transactions(transaction_id, account_number, transaction_type, transaction_amount)
                            return account_balance
                            break
                        except ValueError:
                            print("Enter a number. Try again.")
                        else:
                            return transaction_amount
                            break
    
                    break
                elif select_account_operation == 2:
                    print("Withdraw")
                    break
                elif select_account_operation == 3:
                    print("Transfer")
                    break
                elif select_account_operation == 4:
                    print("Account details")
                    print(' number     status  type       client ID balance')
                    account_details = fetch_account_details(client.client_id, 'Chequing')
                    # show account detals
                    print(account_details) 
                    client_return_to(client)
                    break
                elif select_account_operation == 5:
                    print("Chequing account balance")
                    break
            else:                             
                print("Try again, please enter option number from 1 to 5: ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
        else:
            return select_account_operation
            break

# works
def client_account_menu(client):
    while True:
        try:
            select_menu_option = int(input("Select from the following menu: 1 - access chequing account, 2 - access savings account, 3 - access personal details, 4 - show accounts, 5 - contact the manager: "))
            while select_menu_option < 6 and select_menu_option > 0:
                if select_menu_option == 1:
                    print("Chequing account")
                    chequing_account_fetch = fetch_account_details(client.client_id,'Chequing')
                    print(chequing_account_fetch)
                    chequing_account(client)
                    break
                elif select_menu_option == 2:
                    print("Savings account")
                    savings_account_fetch = fetch_account_details(client.client_id,'Savings')
                    savings_account(client)
                    break
                # works
                elif select_menu_option == 3:
                    print("Personal details")
                    print(" account   pin    first last name    occupation           age   sex  street          city          prov  postal    phone         e-mail  ")
                    personal_details = fetch_client_details(client.client_id, client.client_password)
                    print(personal_details)
                    break
                elif select_menu_option == 4:
                    print("Your accounts")
                    accounts = fetch_all_accounts(client.client_id)
                    print(accounts)
                    
                    break
                elif select_menu_option == 5:
                    print("Contact the manager")
                    contact_manager()
                    break
            else:
                print("Try again, please enter option 1-5. ")
                continue
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return select_menu_option
            break
# works
def client_signin():
    while True:
        log_in_client_id = input("Enter your client ID: ")
        log_in_client_password = input("Enter password: ")
        client_details = fetch_client_details(log_in_client_id,log_in_client_password)
        if client_details is not None:
            client_id = client_details[0]
            client_password = client_details[1]
            if log_in_client_id == str(client_id) and log_in_client_password == str(client_password):
                return Client(client_id, client_password, client_details[2], client_details[3],client_details[4],client_details[5],client_details[6],client_details[7],client_details[8],client_details[9],client_details[10],client_details[11], client_details[12])             
        else:
            print("Invalid ID or password, please try again.")
# works
def client_signin_signup():
    while True:
        try:
            sign_in_sign_up = int(input("Press 1 to sign up / Press 2 to sign in: "))
            while sign_in_sign_up < 3 and sign_in_sign_up > 0:
                if sign_in_sign_up == 1:
                    print("Sign up - create a new client account")
                    client_signup_form()
                    break
                elif sign_in_sign_up == 2:
                    print("Sign in to an existing client account")
                    client = client_signin()
                    print("Successful Login")
                    client_account_menu(client)
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
# works
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
                    print("Successful login")
                    manager_account_menu()
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
# works
def main():
    print('===============================================')
    print("             Welcome to Bank of JOJO           ")
    print('===============================================')
    print(role_verification())
if __name__ == "__main__":
    main()
# add return and exit options after each selected option
# incorporate account, chequing account and savings account
# create a dynamic client table form
# make the manager take user input 
# progress from client sign up to sign in