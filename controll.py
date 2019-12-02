import sqlite3
conn = sqlite3.connect("test1.db")
c = conn.cursor()

def insert_user(Name,UserName,Password,Avilable_Amount):
    c.execute(''' INSERT INTO Users_data (Name,UserName,Password,Avilable_Amount)
                    VALUES(?,?,?,?,?)''', (Name,UserName,Password,Avilable_Amount))
    conn.commit()
    print(Name, "added successfully.")


def insert_stock(UserName,Stock_symbol,share_quantity,Brought_price):
    c.execute(''' INSERT INTO Stock_data (UserName,Stock_symbol,share_quantity,Brought_price)
                        VALUES(?,?,?)''', (UserName,Stock_symbol,share_quantity,Brought_price))
    conn.commit()
    print( "stock successfully.")
