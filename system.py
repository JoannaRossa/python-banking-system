class System(Account):

#first step in the banking system
    def __init__(self, pin):
        self.pin = pin
    
    #method requesting user PIN and handling errors
    def getPIN(self):
        print("Please enter your PIN: ")
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
        first_char = self.pin[0]
        while(first_char > 0 and first_char < 4):
            #if id starts with 0 it is the manager-open manager class
            if (first_char == 1):
                print('Welcome to the manager account')
                
                break
            #if id starts with 1 it is the client-open client class
            elif (first_char == 2):
                print('Welcome to the client account')

                break
            #if id starts with 2 it is the maintenance-open maintenance class
            elif (first_char == 3):
                print('Welcome to the maintenance accont')
                
                break
        
        else:
            inputID = int(input("Error - enter PIN starting with a digit from 0 to 2: "))
            assignRole(inputPIN)
    

def main():
    print('======================================')
    print("          Welcome to RBC              ")
    print('======================================')
    userID = System()
    print(userID.getPIN)
    
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


        

    


