print('''
Hello, Welcome to the StockTerminalApp
If you are a register user, Enter 1
If you are want to register here Enter 2 
If you are super user, Enter 3''')
p0 = int(input(">"))
if p0 == 1:
    UserName = input("Enter your UserName here :")
    Password = input("Enter your password here :")

    check_username = login_details_check_from_db(UserName)
    check_pw = login_details_check_from_db(Password)
    if check_username and check_pw == True:
        print('''You are logged in :)
        Enter 1 for buy stocks
        Enter 2 for sell stock
        Enter 3 for Add Amount
        Enter 4 for check your data 
        Enter 5 for search company stock''')
        q1 = int(input(">"))
        Exit = False
        if q1 == 1:
            while Exit == False:
                stock_buy = input(int("Enter Amount of Money you want to buys shares "))
                if 
                n_date = input("Enter the date(dd/mm/yyyy):")
                n_user = input("Enter your username:")
                rent_book(n_date, n_user, to_be_rented)
                print("Do you wish to rent another?")
                a1 = input("Enter Yes/No").lower()
                if a1 == "no":
                    Exit = True
                else:
                    continue
        elif q1 == 2:
            while Exit == False:
                rentedbookname = input("Which book do you wish to return?")
                d_borrow = c.execute('''SELECT Rented_date FROM Books WHERE Name = (?)''', (rentedbookname,))
                et = str(d_borrow.fetchall()[0][0])
                # print(et)
                T = date.today()
                T2 = str(T)
                e = datetime.strptime(T2, "%Y-%m-%d")
                d = datetime.strptime(et, "%d/%m/%Y")
                t = str(e - d)
                y = t[0:-14]    #no of days rented
                y_int = int(y)
                print("Number of days rented:", y , "days")
                count_amount(y_int)
                Exit = True

        elif q1 == 3:
            while Exit == False:

        elif q1 == 4:
            while Exit == False:
        

        elif q1 == 5:
            while Exit == False:

    elif check_pw == False:
        print("Incorrect password!")
    elif check_username == False:
        print("Incorrect username!")
    else:
        print("Invalid values")

elif p0 == 2:
    print('''
    Enter 1 for register your self ''')
    p1 = int(input(">"))
    Exit = False
    while Exit == False:
        if p1 == 1:
        while Exit == False:
            #Adding users
            user_name = input("Name:")
            address = input("Address:")
            phone = input("Phone number:")
            reg_n = input("Registration Name:")
            password = input("Password:")
            insert_user(user_name, address, phone, reg_n, password)
            print("Do you wish to add another?")
            a1 = input("Enter Yes/No").lower()
            if a1 == "no":
                Exit = True
            else:
                continue
            else:
                print("Enter a valid value")

    else:
        print("Please enter valid values")
    elif p0 == 3:
        UserName = input("Enter your UserName here :")
        Password = input("Enter your password here :")


else:
    print("Please enter valid values")
c.close()
conn.close()

input('Press ENTER to exit')