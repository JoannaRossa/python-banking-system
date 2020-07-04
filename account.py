class Account:
   
   #open/close


    def __init__(self, client_id, first_name, last_name, balance, deposit, withdrawal, transfer): 
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.transfer = transfer

    def checkPIN(self,value):
        return self.client_id==value
    
    #deposit function
    def deposit(self, amount, conn):
        #update balance
        self.balance += amount
        return self.balance
        #update deposit
        self.deposit += amount
        return self.deposit
        #display updated data
        # print("Deposit was $%.2f, current balance is $%.2f" % (amount, self.account_balance))
        print("You deposited: " + amount)
        print("Your current balance is: " + self.balance)
        data = "Deposit was $%.2f, current balance is $%.2f" % (amount, self.balance)
        conn.send(data.encode())

    #withdrawal function
    def withdrawal(self, amount, conn):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            #withdraw and update balance
            self.balance -= amount
            return self.balance
            #update withdrawal
            self.withdrawal -= amount
            return self.withdrawal
            #display updated data
            print("You withdrew: " + amount)
            print("Your current balance is: " + self.balance)
            data = "Withdrawal was $%.2f, current balance is $%.2f" % (amount, self.balance)
            conn.send(data.encode())

        #transfer function
        def transfer(self, amount, conn):
            if amount>self.balance:
                print("Insufficient funds")
            else:
                #transfer and update balance
                self.balance -= amount
                #update transfer
                self.transfer -= amount
                print("You transferred: " + amount)
                print("Your current balance is: " + self.balance)
                data = "Transfer was $%.2f, current balance is $%.2f" % (amount, self.balance)
                data = conn.send(data.encode())

    #return balance method
    def getBalance(self):
        return self.balance

    def current_balance(self, conn):
        print("Your current balance: $%.2f" % self.balance)
        data = "Your current balance: $%.2f" % self.balance
        conn.send(data.encode())

# account = Account()
# account.deposit(100)
# print(account.getBalance())    
    #close an account
    # def close(self, amount):
        # if self.balance = 0
            #close account
        
 #extend this account to either savings or chequing to work with the features



#call account so that it performs withdrawals/deposits