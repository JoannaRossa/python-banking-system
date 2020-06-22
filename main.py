# import sqlite3
import db

# #Connecting to sqlite
# conn = sqlite3.connect('bank.db')

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()


# #Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS USER")

# #Creating table as per requirement
# sql ='''CREATE TABLE USER(
#    FIRST_NAME CHAR(20) NOT NULL,
#    LAST_NAME CHAR(20),
#    AGE INT,
#    SEX CHAR(1)
# )'''


# sql2 = '''INSERT INTO USER(
#    FIRST_NAME, LAST_NAME, AGE, SEX) VALUES 
#    ('Joanna', 'Rossa', 27, 'F')'''

# sql3 = 
# # sql ='''CREATE TABLE USER(
# #    FIRST_NAME CHAR(20) NOT NULL,
# #    LAST_NAME CHAR(20),
# #    AGE INT,
# #    SEX CHAR(1)
# # )'''

# cursor.execute(sql)


# cursor.execute(sql2)





# # Commit your changes in the database
# conn.commit()

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

    

    