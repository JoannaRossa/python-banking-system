import sqlite3
from account import Account
from client import Client

conn = sqlite3.connect('bank_database.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

def create_table():
    # Create table - CLIENTS that client can display
    c.execute('''CREATE TABLE IF NOT EXISTS CLIENTS (
        CLIENT_ID INT PRIMARY KEY NOT NULL,
        FIRST_NAME TEXT NOT NULL, 
        LAST_NAME TEXT NOT NULL, 
        AGE INT NOT NULL,
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE INT NOT NULL,
        EMAIL TEXT NOT NULL)''')
    
    # Create table - CLIENTS ACCOUNT CREATION that client can display
    c.execute('''CREATE TABLE IF NOT EXISTS CLIENTS_ACCOUNT_CREATION (
        FIRST_NAME TEXT NOT NULL, 
        LAST_NAME TEXT NOT NULL, 
        AGE INT NOT NULL,
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE INT NOT NULL,
        EMAIL TEXT NOT NULL
        ACCOUNT_TYPE TEXT NOT NULL)''')
    

    # Create table - ACCOUNTS 
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNTS (
        ACCOUNT_NUMBER INT PRIMARY KEY NOT NULL,
        ACCOUNT_STATUS TEXT NOT NULL,
        ACCOUNT_TYPE TEXT NOT NULL,
        CLIENT_ID INT NOT NULL, 
        CURRENT_BALANCE REAL NOT NULL,
        FOREIGN KEY(CLIENT_ID) REFERENCES CLIENT(CLIENT_ID))''')

    
    # Create table - TRANSACTIONS
    c.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS (
        TRANSACTION_ID INT PRIMARY KEY NOT NULL,
        ACCOUNT_NUMBER INT NOT NULL,
        TRANSACTION_TYPE TEXT NOT NULL,
        TRANSACTION_AMOUNT REAL NOT NULL,
        FOREIGN KEY(ACCOUNT_NUMBER) REFERENCES ACCOUNTS(ACCOUNT_NUMBER))''')
    


conn.commit()

# def data_entry():
#     c.execute('''INSERT INTO ACCOUNT_status VALUES('Closed')''')
#     conn.commit()
#     c.close()
#     conn.close()

def dynamic_data_entry(self):
    c.execute('''INSERT INTO CLIENTS(client_id, first_name, last_name, age, gender, street, city, province, postal_code, phone, email) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                (client_id, first_name, last_name, age, gender, street, city, province, postal_code, phone, email))
    conn.commit()
    c.close()
    conn.close()

create_table()
# dynamic_data_entry()


# conn.commit()
