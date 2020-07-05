
class Main:

    def role_verification(self):
        while True:
            try:
                role_number = int(input("Select your role: 1 - client, 2 - manager, 3 - maintenance: "))
            except ValueError:
                print("Enter a number. Try again.")
                continue
            else:
                return role_number
                break
    
    def assign_role(self, role_number):
        while role_number < 4 and role_number > 0:
            if role_number == 1:
                print("Welcome to the client account")
                while True:
                    try:
                        sign_in_sing_up = int(input("Press 1 to sign up / Press 2 to sign in: "))
                        while sign_in_sing_up < 3 and sign_in_sing_up > 0:
                            if sign_in_sing_up == 1:
                                print("Sign up - create a new client account")
                                break

                            elif sign_in_sing_up == 2:
                                print("Sign in to an existing client account")
                                break
                        else:
                            print("Try again, please enter 1 to sign up or 2 to sign in. ")
                            continue
                    except ValueError:
                        print("Enter a number. Try again.")
                        continue
                    else:
                        return sign_in_sing_up
                        break
                break
        else:
            role_number = input("Try again, enter 1 for client, 2 for manager, or 3 for maintenance: ")
            self.assign_role(role_number)
    def main():
        print('======================================')
        print("          Welcome to RBC              ")
        print('======================================')
        userID = Main()
        userPIN = userID.role_verification()
        print(userID.assign_role(userPIN))
    if __name__ == "__main__":
        main()