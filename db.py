import sqlite3
from account import Account
from client import Client
from manager import Manager

conn = sqlite3.connect('bank_database.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

def create_table():
    # Create table - CLIENTS that client can display
    c.execute('''CREATE TABLE IF NOT EXISTS CLIENTS (
        CLIENT_ID INT PRIMARY KEY NOT NULL,
        CLIENT_PASSWORD INT NOT NULL,
        FIRST_NAME TEXT NOT NULL, 
        LAST_NAME TEXT NOT NULL, 
        AGE TEXT NOT NULL,
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE TEXT NOT NULL,
        EMAIL TEXT NOT NULL)''')
    
    # Create table - CLIENTS ACCOUNT CREATION that client can create
    c.execute('''CREATE TABLE IF NOT EXISTS CLIENTS_ACCOUNT_CREATION (
        FIRST_NAME TEXT NOT NULL, 
        LAST_NAME TEXT NOT NULL, 
        AGE TEXT NOT NULL,
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
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
    
    # Create table - MANAGER
    c.execute('''CREATE TABLE IF NOT EXISTS MANAGER(
        MANAGER_ID INT PRIMARY KEY NOT NULL,
        MANAGER_PASSWORD INT NOT NULL,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL,
        AGE TEXT NOT NULL,
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE TEXT NOT NULL,
        EMAIL TEXT NOT NULL)''')

conn.commit()

def fetch_account_details():
    pass

def fetch_client_details(client_id, client_password):
    c.execute("SELECT * from CLIENTS WHERE CLIENT_ID=? AND CLIENT_PASSWORD=? ", (client_id, client_password))
    rows = c.fetchall()
    if len(rows)>0:
        return rows[0]
    return None

def insert_client_details(client_id ):
    pass

def fetch_manager_details(manager_id, manager_password):
    c.execute("SELECT * from MANAGER WHERE MANAGER_ID=? AND MANAGER_PASSWORD=? ", (manager_id, manager_password))
    rows = c.fetchall()
    if len(rows)>0:
        return rows[0] #a tuple with all the elements in that 
    return None

def data_entry():
    c.execute('''INSERT INTO MANAGER(MANAGER_ID, MANAGER_PASSWORD, FIRST_NAME, LAST_NAME, AGE, GENDER, STREET, CITY, PROVINCE, POSTAL_CODE, PHONE, EMAIL) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                (19051999, 1973, 'Joanna', 'Rossa', '21', 'F', '22 Heaven St.', 'Aurora', 'ON', 'L8T4J2', '2897009049', 'asia.rossa@hotmail.com'))
    
    c.execute('''INSERT INTO CLIENTS(CLIENT_ID, CLIENT_PASSWORD, FIRST_NAME, LAST_NAME, AGE, GENDER, STREET, CITY, PROVINCE, POSTAL_CODE, PHONE, EMAIL) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                (22011973, 1999, 'Edyta', 'Holyst', '47', 'F', '888 Pine St.', 'Burlington', 'ON', 'N5X6JZ', '2894894010', 'edyta-holyst@wp.pl'))
    
    c.execute('''INSERT INTO ACCOUNTS(ACCOUNT_NUMBER, ACCOUNT_STATUS, ACCOUNT_TYPE, CLIENT_ID, CURRENT_BALANCE) VALUES (?,?,?,?,?)''',
                (11111111, 'Open', 'Chequing', 22011973, 10000))
    
    c.execute('''INSERT INTO TRANSACTIONS(TRANSACTION_ID, ACCOUNT_NUMBER, TRANSACTION_TYPE, TRANSACTION_AMOUNT) VALUES (?,?,?,?)''',
                (22222222, 11111111, 'Deposit', 1000))
    
    conn.commit()
    c.close()
    conn.close()

# create_table()
# data_entry()
# fetch_client_details(client_id,client_password)

# conn.commit()
