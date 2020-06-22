# import db
import sqlite3
from account import Account
from client import Client

#Connecting to sqlite
conn = sqlite3.connect('bank.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping user table if already exists.
# cursor.execute("DROP TABLE IF USER EXISTS")

#Creating table as per requirement
cursor.execute =("""CREATE TABLE client (
    id integer
    first text
    last text
    )""")

def insert_client(client):
    with conn: #contex manager; we don't need commit statement after if we use this feature
        cursor.execute("INSERT INTO client VALUES (:id, :first_name, :last_name)", {'id': client.id, 'first_name': client.first_name, 'last_name': client.last_name}

def get_client_by_id(id):
    cursor.execute("SELECT * FROM client WHERE id=:id" ('id': id})
    return cursor.fetchall() #returns all the clients

# def update

def remove_client(client):
    with conn:
        cursor.execute("DELETE from client WHERE id = :id AND first_name = :first_name, last_name = :last_name", {'id': client.id, 'first_name': client.first_name, 'last_name': client.last_name})

user_1 = Client(999, "Joanna", "Rossa")
print(user_1.id)
print(user_1.first_name)
print(user_1.last_name)


#display individual client's details
print(cursor.fetchone())
#display all clients' details
print(cursor.fetchall())

# Save changes in the database
#conn.commit()

#Close the connection if done with it
conn.close()

def main():
    print("Welcome to ATM")
    print("Enter your pin: ")
    id=input("")
    #pin is obtained, system assigns pin to a role and displays:
    #if it is a client then:
    print() #display first name and last name of the user
    print("Select an account: ")
    account=input("") #depending on what the input is, system will give access to that account
    print("Select a transaction: ") #...
    print
    print("Enter amount: ")
    amount=input("") #deal with it and when done:
    print("Would you like to make another transaction?")
    #input, if yes then repeat the steps, if no then end a session and print a message:
    print("Thank you for using ATM")

    

    