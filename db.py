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
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE INT NOT NULL,
        EMAIL TEXT NOT NULL)''')
    

    # Create table - ACCOUNTS 
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNTS (
        ACCOUNT_NUMBER INT PRIMARY KEY NOT NULL,
        ACCOUNT_STATUS TEXT NOT NULL,
        ACCOUNT_TYPE TEXT NOT NULL,
        CLIENT_ID INT NOT NULL, 
        CURRENT_BALANCE REAL NOT NULL,
        FOREIGN KEY(ACCOUNT_STATUS) REFERENCES ACCOUNT STATUS(ACCOUNT_STATUS),
        FOREIGN KEY(ACCOUNT_TYPE) REFERENCES ACCOUNT TYPE(ACCOUNT_TYPE),
        FOREIGN KEY(CLIENT_ID) REFERENCES CLIENT(CLIENT_ID))''')
    
    # Create table - ACCOUNT TYPE 
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT TYPE (
        ACCOUNT_TYPE TEXT PRIMARY KEY NOT NULL)''')
    
    # Create table - ACCOUNT STATUS
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT STATUS (
        ACCOUNT_STATUS TEXT PRIMARY KEY NOT NULL)''')
    
    # Create table - TRANSACTIONS
    c.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS (
        TRANSACTION_ID INT PRIMARY KEY NOT NULL,
        ACCOUNT_NUMBER INT NOT NULL,
        TRANSACTION_TYPE TEXT NOT NULL,
        TRANSACTION_AMOUNT REAL NOT NULL,
        FOREIGN KEY(ACCOUNT_NUMBER) REFERENCES ACCOUNTS(ACCOUNT_NUMBER),
        FOREIGN KEY(TRANSACTION_TYPE) REFERENCES TRANSACTION TYPE(TRANSACTION_TYPE))''')
    
    # Create table - TRANSACTION TYPE
    c.execute('''CREATE TABLE IF NOT EXISTS TRANSACTION TYPE (
        TRANSACTION_TYPE TEXT PRIMARY KEY NOT NULL)''')

conn.commit()

def data_entry():
    c.execute('''INSERT INTO CLIENTS VALUES(456, 'JO', 'RO', 'F', 'GARTH', 'HAMONT', 'ON', 'X', 289, 'ASIA') ''')
    conn.commit()
    c.close()
    conn.close()

# def dynamic_data_entry():
#     c.execute('''INSERT INTO CLIENTS(client_id, first_name, last_name, gender, street, city, province, postal_code, phone, email) VALUES (?,?,?,?,?,?,?,?,?,?)''',
#                 (pin, first_name, last_name, gender, street, city, province, postal_code, phone, email))



create_table()
data_entry()


# conn.commit()
