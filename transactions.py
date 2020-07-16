from account import Account

class Transactions:
    def __init__(self, transaction_id, account_number, transaction_type, transaction_amount):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
    
    
    
    def deposit(account_number): 
        Account(account_number, account_status, account_type, client_id, account_balance)
        while True:
            try:
                deposit_amount = float(input("Enter amount you wish to deposit: "))
                account_balance += deposit_amount
                return account_balance
                break
            except ValueError:
                print("Enter a number. Try again.")
            else:
                return deposit_amount
                break
    deposit()
    
    # def savings_deposit(balance_savings): 
    #     while True:
    #         try:
    #             deposit_amount = float(input("Enter amount you wish to deposit: "))
    #             self.balance_savings += deposit_amount
    #             return self.balance_savings
    #             break
    #         except ValueError:
    #             print("Enter a number. Try again.")
    #         else:
    #             return deposit_amount
    #             break

    
    def withdraw(account_number):
        while True:
            try:
                withdraw_amount = float(input("Enter amount you wish to deposit: "))
                account_balance-= withdraw_amount
                return account_balance
                break
            except ValueError:
                print("Enter a number. Try again.")
            else:
                return withdraw_amount
                break

    # def savings_withdraw(balance_savings): 
    #     while True:
    #         try:
    #             withdraw_amount = float(input("Enter amount you wish to withdraw: "))
    #             self.balance.savings += withdraw_amount
    #             return self.balance_savings
    #             break
    #         except ValueError:
    #             print("Enter a number. Try again.")
    #         else:
    #             return withdraw_amount
    #             break
    
    def transfer(balance_chequing, balance_savings):
        while True:
            try:
                transfer_select = int(input("Select 1 - to transfer funds from chequing account to savings account or 2 - to transfer funds from savings account to chequing account: "))
                while transfer_select>0 and transfer_select<3:
                    if transfer_select == 1:
                        print('Transfer funds from chequing account to savings account')
                        transfer_amount = float(input("Enter amount you wish to transfer: "))
                        self.balance_savings += transfer_amount
                        self.balance_chequing -= transfer_amount
                        return self.balance_savings, self.balance_chequing
                        break
                    elif transfer_select == 2:
                        print('Transfer funds from savings account to chequing account')
                        transfer_amount = float(input("Enter amount you wish to transfer: "))
                        self.balance_chequing += transfer_amount
                        self.balance_savings -= transfer_amount
                        return self.balance_chequing, self.balance_savings
                        break
                else:
                    print("Error - enter option from 1 to 2: ")
            except ValueError:
                print("Enter a number. Try again.")
            else:
                return transfer_select
                break
