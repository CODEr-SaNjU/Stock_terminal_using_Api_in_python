import sqlite3
import time
import sys
from wrapper import Markit
from datetime import datetime
from datetime import date

SearchObj = Markit()
conn = sqlite3.connect("Stock.db")
cursor = conn.cursor()

def UserName_check_from_db():
    while True:
        try:
            UserName = input("Please Enter your UserName here ::")
            with conn as db:
                cursor = db.cursor()
            check_user = ("SELECT * FROM Users_data WHERE UserName=?")
            cursor.execute(check_user,[(UserName)])
            results = cursor.fetchall()
            if results:
                Avilable_Amount = int(input("Please Enter your Amount here you want add in your wallet::"))
                insert_Avilable_Amount_add_in_db(Avilable_Amount,UserName)
                
            else:
                print("UserName didnot found ")
                again = input("Do you want to try again(y/n) :: ")
                if again.lower() == "n":
                    time.sleep(1)
                    return("exit")
                    break
        except ValueError:
            print("Invalid Choice. ")
    exit

    UserName = input()
def showAppstartingoption():
    '''Reads options from Viewer'''
    print("Hello, Welcome to the StockTerminalApp")
    print("\nPlease! Choose an option from the below list : ")
    print("--------------------------------------")

    print("[A] : If you are a register user ")
    print("[B] : If you want to register here ")
    print("[C] : If you are super user ")
    print("[D]: If you want to Quit this game")
    while True:
        try:
            user_option = input("\n[INPUT] :: Please enter an option :: ")
            if user_option == 'A':
                print("Please Enter your details here")
                print("--------------------------------------")
                while True:
                    try:
                        UserName = input("Please Enter your UserName here ::")
                        Password = input("please Enter your Password here :: ")
                        with conn as db:
                            cursor = db.cursor()
                        check_user = ("SELECT * FROM Users_data WHERE UserName=? And Password = ?")
                        cursor.execute(check_user,[(UserName),(Password)])
                        results = cursor.fetchall()
                        print(results)
                        if results:
                            for i in results:
                                showUserOptions()
                                break
                        else:
                            print("UserName and password didnot match ") 
                            again = input("Do you want to try again(y/n):")
                            if again.lower() == "n":
                                time.sleep(1)
                                return("exit")
                                break
                    except ValueError:
                        print("Invalid Choice. ")
                exit    
            elif user_option == 'B':
                user_data()
                break
            elif user_option == 'C':
                print("C")
                break
            elif user_option == 'D':
                time.sleep(1)
                print("Thank you ")
                break
            else:
                print("Invalid Choice. Enter A-D")
                showAppstartingoption()
                break

        except ValueError:
            print("Invalid Choice. Enter A-D ")
    exit


def showUserOptions():
    while True:
        '''Reads options from User
        @:param Username - Just to show a customized message'''

        print(f"\nPlease ! Choose an option from the below list : ")
        print("--------------------------------------")

        print("[A] : If you want to check your stock")
        print("[B] : If you want to Add Money in your wallet ")
        print("[C] : If you want to sell your stock ")
        print("[D] : If you want to buy stock ")
        print("[E] : search your company here you want to check stock price ")
        print("[L] : Logout")
        try:
            user_option = input("\n[INPUT] :: Please enter an option :: ")
            if user_option.upper() == "A":
                print("User stock show in terminal")
            elif user_option.upper() == "B":   
                print("Please Enter your details here")
                print("--------------------------------------")
                while True:
                    try:
                        UserName_check_from_db()
                        break
                    except ValueError:
                        print("Invalid  Amount ")
                exit
            elif user_option.upper() == 'C':
                print("sell stock any company ")
                break
            elif user_option.upper() == 'D':
                Buy_stock(SearchObj)

            elif user_option.upper() == 'E':
                user_Search_company(SearchObj)
            elif  user_option.upper() == 'L':
                time.sleep(1)
                return("exit")
                break
            else:
                print("Invalid Choice. Enter Valid data ")
                showAppstartingoption()
                break
        except ValueError:
            print("Invalid Choice. Enter A-D ")
exit




def insert_stock_data(share_quantity):
    cursor.execute('''INSERT INTO Stock_data() ''')


def insert_users_data(Name,UserName,Password,Avilable_Amount):
    cursor.execute(''' INSERT INTO Users_data (Name,UserName,Password,Avilable_Amount)
                            VALUES(?,?,?,?) ''',(Name,UserName,Password,Avilable_Amount))
    conn.commit()
    print(UserName,"Registration successful")
def time_Stamp():
    pass
def user_data():
    Name = input("Please Enter your Name here ::")
    UserName = input("Please Enter your UserName here ::")
    Password = input("Please Enter your Password here::")
    Avilable_Amount = input("please Enter your Balnce you want to add in wallet::")
    insert_users_data(Name,UserName,Password,Avilable_Amount)


    ###############for money add in wallet###

def insert_Avilable_Amount_add_in_db(Avilable_Amount,UserName):
    cursor.execute('UPDATE Users_data SET Avilable_Amount = (?) WHERE UserName = (?) ', (Avilable_Amount,UserName))
    conn.commit()
    print(" Money add successfully in Wallet ")

    ###########for user input add money##############


 
    



def user_Search_company(SearchObj):
    if (SearchObj != None ):
        print("\n Company details ")
        print("================================")
        company = input("search your company name ::")
        if __name__ == '__main__':
            SearchObj = Markit()
            SearchObj.company_search(company)
            SearchObj.get_quote(company)

def processing_of_Avilable_Amount():
    pass
    


def Buy_stock(SearchObj):
    company = input("please enter company name/company symbol you want to buy stock :: ")
    if __name__ == '__main__':
        SearchObj = Markit()
        SearchObj.company_search(company)
        SearchObj.get_quote(company)
    data = input("If you want to buy stock y/n ::")
    if data == 'y':
        take_money = int(input("please enter your amount you want to buy stock ::"))
        with sqlite3.connect("Stock.db") as db:
            cursor = db.cursor()
            check_user_amount = ("SELECT * FROM Users_data WHERE Avilable_Amount=?")
            cursor.execute(check_user_amount,[(take_money)])
            results = cursor.fetchall()
            if results:
                stock = take_money/company_stock_price





    











































































 
#main function    
showAppstartingoption()