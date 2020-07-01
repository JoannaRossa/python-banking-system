import sqlite3
from account import Account
from client import Client

conn = sqlite3.connect('bank_database.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

def create_table():
    # Create table - CLIENTS that client can display
    c.execute('''CREATE TABLE IF NOT EXISTS CLIENTS (
        CLIENT ID INT PRIMARY KEY NOT NULL,
        FIRST NAME TEXT NOT NULL, 
        LAST NAME TEXT NOT NULL, 
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL CODE TEXT NOT NULL,
        PHONE INT NOT NULL,
        EMAIL TEXT NOT NULL)''')
    conn.commit()

    # Create table - ACCOUNTS 
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNTS (
        ACCOUNT NUMBER INT PRIMARY KEY NOT NULL,
        ACCOUNT STATUS TEXT NOT NULL,
        ACCOUNT TYPE TEXT NOT NULL,
        CLIENT ID INT NOT NULL, 
        CURRENT BALANCE REAL NOT NULL,
        FOREIGN KEY(ACCOUNT STATUS) REFERENCES ACCOUNT STATUS(ACCOUNT STATUS),
        FOREIGN KEY(ACCOUNT TYPE) REFERENCES ACCOUNT TYPE(ACCOUNT TYPE),
        FOREIGN KEY(CLIENT ID) REFERENCES CLIENT(CLIENT ID))''')
    conn.commit()
    # Create table - ACCOUNT TYPE 
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT TYPE (
        ACCOUNT TYPE TEXT PRIMARY KEY NOT NULL)''')
    conn.commit()
    # Create table - ACCOUNT STATUS
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT STATUS (
        ACCOUNT STATUS TEXT PRIMARY KEY NOT NULL)''')
    conn.commit()
    # Create table - TRANSACTIONS
    c.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS (
        TRANSACTION ID INT PRIMARY KEY NOT NULL,
        ACCOUNT NUMBER INT NOT NULL,
        TRANSACTION TYPE TEXT NOT NULL,
        TRANSACTION AMOUNT REAL NOT NULL,
        FOREIGN KEY(ACCOUNT NUMBER) REFERENCES ACCOUNTS(ACCOUNT NUMBER),
        FOREIGN KEY(TRANSACTION TYPE) REFERENCES TRANSACTION TYPE(TRANSACTION TYPE))''')
    conn.commit()
    # Create table - TRANSACTION TYPE
    c.execute('''CREATE TABLE IF NOT EXISTS TRANSACTION TYPE (
        TRANSACTION TYPE TEXT PRIMARY KEY NOT NULL)''')
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
