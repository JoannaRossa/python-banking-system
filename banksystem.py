

def role_verification():
    while True:
        try:
            role_number = int(input("Select your role: 1 - client, 2 - manager, 3 - maintenance: "))
        except ValueError:
            print("Enter a number. Try again.")
            continue
        else:
            return role_number
            break
def sign_into_existing_account():
    


def assign_role(role_number):
    while role_number < 4 and role_number > 0:
        if role_number == 1:
            print("Welcome to the client account")
            while True:
                try:
                    sign_in_sign_up = int(input("Press 1 to sign up / Press 2 to sign in: "))
                    while sign_in_sign_up < 3 and sign_in_sign_up > 0:
                        if sign_in_sign_up == 1:
                            print("Sign up - create a new client account")
                            break
                        elif sign_in_sign_up == 2:
                            print("Sign in to an existing client account")
                            while True:
                                # fix validation for this block
                                try:
                                    log_in_client_id = int(input("Enter your client ID: "))
                                    log_in_password = int(input("Enter password: "))
                                    # if log_in_client_id == client_id from the database
                                    # and if log_in_password == password from database
                                    while True:
                                        try:
                                            select_menu_option = int(input("Select from the following menu: 1 - access chequing account, 2 - access savings account, 3 - access personal details, 4 - show balance, 5 - contact the manager: "))
                                            while select_menu_option < 6 and select_menu_option > 0:
                                                if select_menu_option == 1:
                                                    print("Chequing account")
                                                    while True:
                                                        try:
                                                            select_account_operation = int(input("Select: 1 - deposit, 2 - withdrawal, 3 - transfer, 4 - account details: "))
                                                            while select_menu_option < 5 and select_menu_option < 0:
                                                                if select_menu_option == 1:
                                                                    print("Deposit")
                                                                    break
                                                                elif select_menu_option == 2:
                                                                    print("Withdraw")
                                                                    break
                                                                elif select_menu_option == 3:
                                                                    print("Transfer")
                                                                    break
                                                                elif select_menu_option == 4:
                                                                    print("Account details")
                                                                    break
                                                                else:                             
                                                                    print("Error - enter option number from 1 to 4: ")
                                                                    continue
                                                        except ValueError:
                                                            print("Enter a number. Try again.")
                                                        else:
                                                            return select_menu_option
                                                            break
                                                    break
                                                elif select_menu_option == 2:
                                                    print("Savings account")
                                                    while True:
                                                        try:
                                                            select_account_operation = int(input("Select: 1 - deposit, 2 - withdrawal, 3 - transfer, 4 - account details: "))
                                                            while select_menu_option < 5 and select_menu_option < 0:
                                                                if select_menu_option == 1:
                                                                    print("Deposit")
                                                                    break
                                                                elif select_menu_option == 2:
                                                                    print("Withdraw")
                                                                    break
                                                                elif select_menu_option == 3:
                                                                    print("Transfer")
                                                                    break
                                                                elif select_menu_option == 4:
                                                                    print("Account details")
                                                                    break
                                                                else:
                                                                    print("Error - enter option number from 1 to 4: ")
                                                                    continue
                                                        except ValueError:
                                                            print("Enter a number. Try again.")
                                                        else:
                                                            return select_menu_option
                                                            break
                                                    break
                                                elif select_menu_option == 3:
                                                    print("Personal details")
                                                    # accounts table
                                                    break
                                                elif select_menu_option == 4:
                                                    print("Your balance")
                                                    break
                                                elif select_menu_option == 5:
                                                    print("Contact the manager")
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
                                                        else:
                                                            return contact_manager_option
                                                    break
                                                    
                                        except ValueError:
                                            print("Enter a number. Try again.")
                                            continue
                                        else:
                                            return select_menu_option
                                            break
                                    else:
                                        print("Try again, please enter option 1-5. ")
                                        continue
                
                except ValueError:
                    print("Enter a number. Try again.")
                    continue
                else:
                    return sign_in_sign_up
                    break
            else:
                print("Try again, please enter 1 to sign up or 2 to sign in. ")
                continue
        
        elif role_number == 2:
            print("Welcome to the manager account")  
        elif role_number == 3:
            print("Welcome to the maintenance account")
    else:
        role_number = input("Try again, enter 1 for client, 2 for manager, or 3 for maintenance: ")
        assign_role(role_number)


def main():
    print('======================================')
    print("          Welcome to RBC              ")
    print('======================================')
    userPIN = role_verification()
    print(assign_role(userPIN))
if __name__ == "__main__":
    main()