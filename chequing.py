from account import Account

class Chequing(Account):
    def __init__(self):
        self.tier = 0
        self.interest = 0
        self.balance = 0
    #rate interests
    def tier(interest, balance):
        if (balance<=200):
            self.interest=0.01
        if(200.01<=balance<=400):
            self.interest=0.02
        if(400.01<=balance<=600):
            self.interest=0.03
        if(balance>=600.01):
            self.interest=0.04
            

