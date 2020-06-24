from account import Account

class System:

    #first step in the banking system
    #method requesting user PIN and handling errors
    def getPIN(self):
        while True:
            try:
                pin = int(input("Enter PIN: "))
            except ValueError:
                print("Enter a number. Try again.")
                continue
            else:
                return pin
                break
    
    #method that assigns a role to the user based on their PIN
    def assignRole(self, pin):
        first_char = str(pin)[0]
        while first_char > "0" and first_char < "4":
            #if id starts with 0 it is the manager-open manager class
            if first_char == "1":
                print('Welcome to the manager account')
                print("Please select from the following options: 1 - open client account, 2 - display client info, 3 - display database info, 4 - close client account")
                option=int(input("Enter option: "))
                while option > 0 and option < 5:
                    if option == 1:
                        print("Open client account")
                        break
                    elif option == 2:
                        print("Display client info")
                        break
                    elif option == 3:
                        print("Display database info")
                        break
                    elif option == 4:
                        print("Close client account")  
                        break   
                    else:
                        option = input("Error - enter option number from 1 to 4: ")                   
                break
    
            #if id starts with 1 it is the client-open client class
            elif first_char == "2":
                print('Welcome to the client account')
                print("Please select from the following options: 1 - account details, 2 - deposit, 3 - withdraw, 4 - transfer, 5 - contact manager")
                option=int(input("Enter option: "))
                while option > 0 and option < 5:
                    if option == 1:
                        print("account details")
                        break
                    elif option == 2:
                        print("deposit")
                        break
                    elif option == 3:
                        print("withdraw")
                        break
                    elif option == 4:
                        print("transfer")  
                        break 
                    elif option == 5:  
                        print("contact manager")
                    
                    else:
                        option = input("Error - enter option number from 1 to 4: ")
                                   
                break
            #if id starts with 2 it is the maintenance-open maintenance class
            elif first_char == "3":
                print('Welcome to the maintenance accont')
                
                break
        
        else:
            pin = input("Error - enter PIN starting with a digit from 1 to 3: ")
            self.assignRole(pin)
    

def main():
    print('======================================')
    print("          Welcome to RBC              ")
    print('======================================')

    userID = System()
    userPIN = userID.getPIN()
    print(userID.assignRole(userPIN))


    
    # print(System().assignRole(System().getPIN()))
    # userID2 = Account()

    # print(s1.getId())
    #user1.getId()
    #pin is obtained, system assigns pin to a role and displays:
    #if it is a client then:
    # user1.show() #display first name and last name of the user
    # print("Select an account: ")
    # account=input("") #depending on what the input is, system will give access to that account
    # print("Select a transaction: ") #...
    # print
    # print("Enter amount: ")
    # amount=input("") #deal with it and when done:
    # print("Would you like to make another transaction?")
    # #input, if yes then repeat the steps, if no then end a session and print a message:
    # print("Thank you for being a part of RBC")
    
    
if __name__ == "__main__":
    main()
# obj1 = System()
# obj2 = System()
# #demo
# # System.getId(obj1)
# # System.getId(obj2)
# #but use this syntax:
# obj1.getId()
# obj2.getId()


        

    


