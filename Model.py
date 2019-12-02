import sqlite3

conn = sqlite3.connect("Stock.db")
cursor = conn.cursor()
#user table create 
cursor.execute('''CREATE TABLE IF NOT EXISTS Users_data
        (Name TEXT NOT NULL,
        UserName VARCHAR NOT NULL,
        Password VARCHAR NOT NULL,
        Avilable_Amount float )''')
print("Table User created successfully.")

#create libaraian table
cursor.execute('''CREATE TABLE IF NOT EXISTS Stock_data
        (UserName VARCHAR,
        Stock_symbol TEXT,
        share_quantity INT,
        TimeStamp REAL, 
        Brought_price float)''')
print("Table Stock created successfully.")

cursor.close()
conn.commit()
conn.close()                 
