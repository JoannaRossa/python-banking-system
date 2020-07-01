import sqlite3

conn = sqlite3.connect('temp.db')

cursor = conn.cursor()
# #Creating table as per requirement
# cursor.execute("""CREATE TABLE manager (
#     id integer,
#     username text,
#     pin text
#     )""")

# sql2 = '''INSERT INTO manager(
#    username, pin) VALUES 
#    ('joannarossa', '2345')'''

# cursor.execute(sql2)  
# conn.commit()

user_name = input("Enter username")
pin = input("Enter pin")

cursor.execute("SELECT pin, ag FROM manager WHERE username = ?",(user_name,))
rows = cursor.fetchall()
# print("pin " + pin)
# print("database recieeivd pin " + rows[0][0])

# print("\n\n\n")
# print(type(pin))
# print(type(rows[0][0]))
if pin == rows[0][0]:
    print("same")
else:
    print("not same")