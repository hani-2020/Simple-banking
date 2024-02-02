import sqlite3 #importing sqlite3 for handling sql

#connecting to database and defining a cursor
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#creating table with colomns username, password and amount
cursor.execute('''
          CREATE TABLE IF NOT EXISTS user
          ([user_name] TEXT, [password] TEXT, [balance] REAL)
          ''')                    

#username and password validation function, both can't contain only spaces or quotation marks
def signinVerif(username, password):
    if "'" in username or '"' in username or username.isspace()==True:
        userValid=False
        print("Do not put only whitespaces or quotation marks in the username")
    else:
        userValid=True
    if "'" in password or '"' in password or password.isspace()==True:
        passValid=False
        print("Do not put only whitespaces or quotation marks in the password")
    else:
        passValid=True
    if userValid==True:
        data=cursor.execute("SELECT EXISTS (SELECT 1 FROM user WHERE user_name = ?)", (username,))
        data=cursor.fetchone()
        if data[0]==0 and passValid==True:
            return True
        else:
            print("username already exists")
            return False

#sign in function, will ask user for username and password. After validation will store in database
def signin():
    username=input("enter username: ")
    password=input("enter password: ")
    valid=signinVerif(username, password)
    if valid==True:
        cursor.execute( f"INSERT INTO user (user_name, password, balance) VALUES ('{username}', '{password}', {0})") 
        print("new customer registered")
        app()
    else:
        print("not a valid customer")
        app()
        return

#money deposit function, will accept username and add amount to that username
def deposit(username):
    validAmount=True
    while validAmount==True:
        amount=input("Amount to deposit: ")
        if amount.isdigit()==True:
            amount=float(amount)
        else:
            print("Invalid amount. Try again")
            validAmount=False
            deposit(username)
            return
        if amount>0:
            balance=cursor.execute(f"SELECT balance FROM user WHERE user_name='{username}'")
            balance=cursor.fetchone()
            newBalance=balance[0]+amount
            cursor.execute(f"UPDATE user SET balance={newBalance} WHERE user_name='{username}'")
            showBalance(username)
            return
        else:
            print("Invalid amount. Try again")
            validAmount=False
            deposit(username)

#money withdrawal function, will accept username and subtract amount from that username
def withdraw(username):
    validAmount=True
    while validAmount==True:
        amount=input("Amount to withdraw: ")
        if amount.isdigit()==True:
            amount=float(amount)
        else:
            print("Invalid amount. Try again")
            validAmount=False
            withdraw(username)
            return
        balance=cursor.execute(f"SELECT balance FROM user WHERE user_name='{username}'")
        balance=cursor.fetchone()
        balance=balance[0]
        if balance>=amount:
            lesser=True
        else:
            lesser=False
        if amount>0 and lesser==True:
            newBalance=balance-amount
            cursor.execute(f"UPDATE user SET balance={newBalance} WHERE user_name='{username}'")
            showBalance(username)
            return
        else:
            print("Invalid amount. Try again")
            validAmount=False
            withdraw(username)

#function to show balance, will accept username and show balace present in that account
def showBalance(username):
    balance=cursor.execute(f"SELECT balance FROM user WHERE user_name='{username}'")
    balance=cursor.fetchone()
    print("current balance:",balance[0])
    return

def verify(username, password):
    pw=cursor.execute(f"SELECT password FROM user WHERE user_name = '{username}'")
    pw=cursor.fetchone()
    if pw[0]==password:
        return True
    else:
        return False

#login function will accept username and password as input from user, which after verification with database will allow access to further control
def login():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    verdict=verify(username, password)
    if verdict==True:
        print("Welcome "+ username)
        showPage=True
        while showPage==True:
            print("Account Details")
            print("a) Amount Deposit")
            print("b) Amount Withdrawal")
            print("c) Check Balance")
            print("d) Exit")
            inp=input("Choose a task: ")
            if inp=="d":
                app()
                return
            elif inp=="c":
                showBalance(username)
            elif inp=="b":
                withdraw(username)
            elif inp=="a":
                deposit(username)
            else:
                print("Invalid input. Try again")
    else:
        print("Invalid username or password. Try again")
        app()
        return

#main function which starts the app, will request input from user to go to login page, sign up page or exit.
def app():
    showPage=True
    while showPage==True:
        print("Customer")
        print("1. Customer Login")
        print("2. New Customer Sign in")
        print("3. Exit")
        inp=input("Choose a task: ")
        if inp=="3":
            print("Exited Application successfully")
            return
        elif inp=="2":
            signin()
            showPage=False
        elif inp=="1":
            login()
            showPage=False
        else:
            print("Invalid input. Try again")
app()

#commiting and closing sql connection
conn.commit()
conn.close()