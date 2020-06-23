class Bank:
   
   #open/close


    def__init__(self): 
        self.id = None #based on id, the role will be assigned
        self.balance = 0   #should I initialize to zero or to balance variable
        self.deposit = 0
        self.withdraw = 0
        self.transfer = 0
    
    
    def deposit(self, amount):

        #update balance
        self.balance += amount
        #update deposit
        self.deposit += amount
        #display updated data
        print("You deposited: " + amount)
        print("Your current balance is: " + self.balance)
        data = 
        conn.send(data.encode())

    def withdrawal(self, amount, conn):

        #update balance
        self.balance -= amount
        #update withdrawal
        self.withdrawal -= amount
        #display updated data
        print("You withdrew: " + amount)
        print("Your current balance is: " + self.balance)

        data = 
        conn.send(data.encode())

    
    def transfer(self, amount, conn):

        #update balance
        self.balance -= amount
        #update transfer
        self.transfer -= amount
        print("You transferred: " + amount)
        print("Your current balance is: " + self.balance)
        data = conn.send(data.encode())

    # def balance
    def getBalance(self):
        return self.balance
    
    def close(self, amount):
        if self.balance = 0


            #close account
        




#call account so that it performs withdrawals/deposits
