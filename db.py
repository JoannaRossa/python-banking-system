import sqlite3

conn = sqlite3.connect('bank_database.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

def create_table():

    # Create table - TRANSACTIONS
    c.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS (
        TRANSACTION_ID INT PRIMARY KEY NOT NULL,
        ACCOUNT_NUMBER INT NOT NULL,
        TRANSACTION_TYPE TEXT NOT NULL,
        TRANSACTION_AMOUNT REAL NOT NULL,
        FOREIGN KEY(ACCOUNT_NUMBER) REFERENCES ACCOUNTS(ACCOUNT_NUMBER))''')
    
    # Create table - ACCOUNTS 
    c.execute('''CREATE TABLE IF NOT EXISTS ACCOUNTS (
        ACCOUNT_NUMBER INT PRIMARY KEY NOT NULL,
        ACCOUNT_STATUS TEXT NOT NULL,
        ACCOUNT_TYPE TEXT NOT NULL,
        CLIENT_ID INT NOT NULL, 
        CURRENT_BALANCE REAL NOT NULL,
        FOREIGN KEY(CLIENT_ID) REFERENCES CLIENT(CLIENT_ID))''')
    
    # Create table - CLIENTS ACCOUNT CREATION that client can create
    c.execute('''CREATE TABLE IF NOT EXISTS CLIENTS_ACCOUNT_CREATION (
        FIRST_NAME TEXT NOT NULL, 
        LAST_NAME TEXT NOT NULL, 
        OCCUPATION TEXT NOT NULL,
        AGE TEXT NOT NULL,
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        ACCOUNT_TYPE NOT NULL)''') 
    
    
    # Create table - CLIENTS that displays all clients in the system
    c.execute('''CREATE TABLE IF NOT EXISTS CLIENTS (
        CLIENT_ID INT PRIMARY KEY NOT NULL,
        CLIENT_PASSWORD INT NOT NULL,
        FIRST_NAME TEXT NOT NULL, 
        LAST_NAME TEXT NOT NULL, 
        OCCUPATION TEXT NOT NULL,
        AGE TEXT NOT NULL,
        GENDER TEXT NOT NULL,
        STREET TEXT NOT NULL,
        CITY TEXT NOT NULL,
        PROVINCE TEXT NOT NULL,
        POSTAL_CODE TEXT NOT NULL,
        PHONE TEXT NOT NULL,
        EMAIL TEXT NOT NULL)''')

    # Create table - MANAGER that displays all managers (there is only one manager)
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


def insert_transactions(client_id, account_type):
    c.execute('''INSERT INTO TRANSACTIONS(TRANSACTION_ID, ACCOUNT_NUMBER, TRANSACTION_TYPE, TRANSACTION_AMOUNT) VALUES (?,?,?,?)''',
                (transaction_id, account_number, transaction_type, transaction_amount))
    conn.commit()

    account_details = fetch_account_details(client.client_id, 'Chequing')

def open_account():
    pass

def fetch_all_transactions(account_number):
    c.execute("SELECT * from TRANSACTIONS WHERE ACCOUNT_NUMBER=?", (account_number))
    rows = c.fetchall()
    if len(rows)>0:
        return rows[0]
    return None

def update_balance(client_id, current_balance, account_type):
    c.execute('''UPDATE ACCOUNTS SET CURRENT_BALANCE=? WHERE CLIENT_ID=? AND ACCOUNT_TYPE=?''', (current_balance, client_id, account_type))
    conn.commit()

def insert_transactions(transaction_type, transaction_amount):
    c.execute('''INSERT INTO TRANSACTIONS(TRANSACTION_TYPE, TRANSACTION_AMOUNT) VALUES (?,?)''',
                (transaction_type, transaction_amount))
    conn.commit()



def fetch_transaction_details(transaction_id):
    c.execute("SELECT * from TRANSACTIONS WHERE TRANSACTION_ID=? ", (transaction_id))
    rows = c.fetchall()
    if len(rows)>0:
        return rows[0]
    return None

# this works

def fetch_all_accounts(client_id):
    c.execute("SELECT * from ACCOUNTS WHERE CLIENT_ID=?", (client_id))
    rows = c.fetchall()
    if len(rows) > 0:
        return rows[0]
    return None

def fetch_account_details(client_id, account_type):
    c.execute("SELECT * from ACCOUNTS WHERE CLIENT_ID=? AND ACCOUNT_TYPE=?", (client_id, account_type))
    rows = c.fetchall()
    if len(rows) > 0:
        return rows[0]
    return None

def fetch_client_details(client_id, client_password):
    c.execute("SELECT * from CLIENTS WHERE CLIENT_ID=? AND CLIENT_PASSWORD=? ", (client_id, client_password))
    rows = c.fetchall()
    if len(rows)>0:
        return rows[0]
    return None


# copy and paste data from CLIENTS ACCOUNT CREATION  to CLIENTS
def transfer_clientinput_to_clientsdatabase():
    pass

def fetch_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender, sign_up_street,sign_up_city, sign_up_province,sign_up_postal_code, sign_up_phone,sign_up_email,sign_up_account_type):
    c.execute("SELECT * from CLIENTS_ACCOUNT_CREATION WHERE FIRST_NAME=? AND LAST_NAME=? AND OCCUPATION=? AND AGE=? AND GENDER=? AND STREET=? AND CITY=? AND PROVINCE=? AND POSTAL_CODE=? AND PHONE=? AND EMAIL=? AND ACCOUNT_TYPE=?", (sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender, sign_up_street,sign_up_city,sign_up_province,sign_up_postal_code, sign_up_phone,sign_up_email,sign_up_account_type))
    rows = c.fetchall()
    if len(rows)>0:
        return rows[0]
    return None

# this works
def insert_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender,sign_up_street,sign_up_city,sign_up_province,sign_up_postal_code, sign_up_phone,sign_up_email, sign_up_account_type):
    c.execute('''INSERT INTO CLIENTS_ACCOUNT_CREATION(FIRST_NAME, LAST_NAME, OCCUPATION, AGE, GENDER, STREET, CITY, PROVINCE, POSTAL_CODE, PHONE, EMAIL, ACCOUNT_TYPE) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                (sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender,sign_up_street,sign_up_city,sign_up_province,sign_up_postal_code, sign_up_phone, sign_up_email,sign_up_account_type))
    conn.commit()

def delete_client_details(client_id, client_password):
    c.execute("DELETE * from CLIENTS WHERE CLIENT_ID=? AND CLIENT_PASSWORD=? ", (client_id, client_password))
    
    conn.commit()

def create_account():
    pass
def delete_account():
    pass

# this works
def fetch_manager_details(manager_id, manager_password):
    c.execute("SELECT * from MANAGER WHERE MANAGER_ID=? AND MANAGER_PASSWORD=? ", (manager_id, manager_password))
    rows = c.fetchall()
    if len(rows)>0:
        return rows[0] #a tuple with all the elements in that 
    
    return None

# this works
def data_entry():
    c.execute('''INSERT INTO MANAGER(MANAGER_ID, MANAGER_PASSWORD, FIRST_NAME, LAST_NAME, AGE, GENDER, STREET, CITY, PROVINCE, POSTAL_CODE, PHONE, EMAIL) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                (19051999, 1973, 'Joanna', 'Rossa', '21', 'F', '22 Heaven St.', 'Aurora', 'ON', 'L8T4J2', '2897009049', 'asia.rossa@hotmail.com'))
    
    c.execute('''INSERT INTO CLIENTS(CLIENT_ID, CLIENT_PASSWORD, FIRST_NAME, LAST_NAME, OCCUPATION, AGE, GENDER, STREET, CITY, PROVINCE, POSTAL_CODE, PHONE, EMAIL) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                (22011973, 1999, 'Edyta', 'Holyst', 'Business Services', '47', 'F', '888 Pine St.', 'Burlington', 'ON', 'N5X6JZ', '2894894010', 'edyta-holyst@wp.pl'))
    
    c.execute('''INSERT INTO ACCOUNTS(ACCOUNT_NUMBER, ACCOUNT_STATUS, ACCOUNT_TYPE, CLIENT_ID, CURRENT_BALANCE) VALUES (?,?,?,?,?)''',
                (11111111, 'Open', 'Chequing', 22011973, 10000))
    
    c.execute('''INSERT INTO ACCOUNTS(ACCOUNT_NUMBER, ACCOUNT_STATUS, ACCOUNT_TYPE, CLIENT_ID, CURRENT_BALANCE) VALUES (?,?,?,?,?)''',
                (22222222, 'Open', 'Savings', 22011973, 20000))
    
    c.execute('''INSERT INTO ACCOUNTS(ACCOUNT_NUMBER, ACCOUNT_STATUS, ACCOUNT_TYPE, CLIENT_ID, CURRENT_BALANCE) VALUES (?,?,?,?,?)''',
                (33333333, 'Open', 'Savings', 22011973, 30000))
    
    c.execute('''INSERT INTO TRANSACTIONS(TRANSACTION_ID, ACCOUNT_NUMBER, TRANSACTION_TYPE, TRANSACTION_AMOUNT) VALUES (?,?,?,?)''',
                (22222222, 11111111, 'Deposit', 1000))
    
    conn.commit()
    c.close()
    conn.close()


# sql = 'DELETE FROM ACCOUNTS WHERE ACCOUNT_NUMBER=?'
# c.execute(sql, ('33333333',))
# conn.commit()

# create_table()
# data_entry()
#insert_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender,sign_up_street,sign_up_city,sign_up_province,sign_up_postal_code, sign_up_phone, sign_up_email)

#fetch_client_form_details(sign_up_first_name, sign_up_last_name,sign_up_occupation,sign_up_age,sign_up_gender, sign_up_street,sign_up_city, sign_up_province,sign_up_postal_code, sign_up_phone,sign_up_email)

#delete_client_details(client_id, client_password)

