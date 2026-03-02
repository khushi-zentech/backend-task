"""
Task - 29: OOP and Database Task with existing ATM Task (Task-12).
"""

# import psycopg2 library to connect Database from PostgreSQL
import psycopg2

# import randint function from random library to generate random card and pin
from random import randint

# define Database_Connection class to manage database connections
class DatabaseConnection:
    # constructor to connect with database
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", database="atm_system", user="postgres", password="LJIET")
        self.cursor = self.conn.cursor()

    # define function to execute query
    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()

    # define function to fetch detail
    def fetchone_query(self):
        return self.cursor.fetchone()

    # define function to fetch all details
    def fetchall_data(self):
        return self.cursor.fetchall()
    
    # define function to close connection
    def close_conn(self):
        self.cursor.close()
        self.conn.close()
    
# create global object of DatabaseConnection to call it's method
db = DatabaseConnection()
    
# define Bank class to manage Bank details
class Bank:
    # constructor to initialize bank details
    def __init__(self, bank_name, bank_balance):
        self.bank_name = bank_name
        self.bank_balance = bank_balance

    # define function to insert bank 
    def insert_bank(self):
        query = "INSERT INTO banks(bank_name, bank_balance) VALUES (%s, %s)"
        db.execute_query(query, (self.bank_name, self.bank_balance))

    # define staticmethod to update bank balance
    @staticmethod
    def update_bank(bank_name, new_balance):
        query = "UPDATE banks SET bank_balance = %s WHERE bank_name = %s"
        db.execute_query(query, (new_balance, bank_name))

    # define staticmethod to delete bank
    @staticmethod
    def delete_bank(bank_name):
        query = "DELETE FROM banks WHERE bank_name = %s"
        db.execute_query(query, (bank_name,))
        
    # define staticmehtod to get bank details
    @staticmethod
    def get_bank(bank_name):
        query = "SELECT * FROM banks WHERE bank_name = %s"
        db.execute_query(query, (bank_name,))
        
        return db.fetchone_query()
    
# define ATM class to manage ATM details
class ATM:
    # constructor to initialize ATM details
    def __init__(self, atm_name, bank_name, atm_balance):
        self.atm_name = atm_name
        self.bank_name = bank_name
        self.atm_balance = atm_balance

    # define function to insert ATM
    def insert_atm(self):
        query = "INSERT INTO atms(atm_name, bank_name, atm_balance) VALUES (%s, %s, %s)"
        db.execute_query(query, (self.atm_name, self.bank_name, self.atm_balance))

    # define staticmethod to update ATM balance
    @staticmethod
    def update_atm(atm_name, new_balance):
        query = "UPDATE atms SET atm_balance = %s WHERE atm_name = %s"
        db.execute_query(query, (new_balance, atm_name))

    # define staticmethod to delete ATM
    @staticmethod
    def delete_atm(atm_name):
        query = "DELETE FROM atms WHERE atm_name = %s"
        db.execute_query(query, (atm_name,))
    
    # define staticmethod to get ATM details
    @staticmethod
    def get_atm(atm_name):
        query = "SELECT * FROM atms WHERE atm_name = %s"
        db.execute_query(query, (atm_name,))
        
        return db.fetchone_query()

# define User class to manage User details
class User:
    # constructor to intialize user details
    def __init__(self, user_name, bank_name, atm_name):
        self.user_name = user_name
        self.bank_name = bank_name
        self.atm_name = atm_name

        self.card = User.generate_card()
        self.pin = User.generate_pin()

        self.balance = 1000.0
        self.day_transaction_count = 0

    # define function to insert user
    def insert_user(self):
        query = "INSERT INTO users(user_name, bank_name, atm_name, card, pin, balance, day_transaction_count) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        db.execute_query(query, (self.user_name, self.bank_name, self.atm_name, self.card, self.pin, self.balance, self.day_transaction_count))

        print("\nUser Created Successfully!")
        print("Card Number:", self.card)
        print("PIN:", self.pin)

    # define staticmethod to update user PIN
    @staticmethod
    def update_user(user_name, new_pin):
        query = "UPDATE users SET pin = %s WHERE user_name = %s"
        
        db.execute_query(query, (new_pin, user_name))
        print("\nPIN Changed Successfully.")

    # define staticmethod to delete user
    @staticmethod
    def delete_user(user_name):
        query = "DELETE FROM users WHERE user_name = %s"
        db.execute_query(query, (user_name,))
        
    # define staticmethod to generate random card of user
    @staticmethod
    def generate_card():
        return randint(10**15, (10**16 - 1))

    # define staticmethod to generate random pin of user
    @staticmethod
    def generate_pin():
        return randint(1000, 9999)
    
    # define staticmethod to get user details
    @staticmethod
    def get_user(user_name):
        query = "SELECT * FROM users WHERE user_name = %s"
        db.execute_query(query, (user_name,))
        
        return db.fetchone_query()

    # define staticmethod to display user details
    @staticmethod
    def display_details(user_name):
        query = "SELECT * FROM users WHERE user_name = %s"
        db.execute_query(query, (user_name,))
        
        user = db.fetchone_query()

        if user:
            print("\nUser Name:", user[1])
            print("Bank Name:", user[2])
            print("ATM Name:", user[3])
            print("Card Number:", user[4])
            print("Current Balance:", user[6])
        else:
            print("\nUser not Found!")
      
# define ATM_System class to manage daily transactions   
class ATM_System:
    day_transaction_limit = 50
    user_transaction_limit = 3
    single_transaction_limit = 10000
    transaction_count = 0
            
    # define staticmethod to deposite money
    @staticmethod
    def deposit(user_name, atm_name, amount):
        if ATM_System.transaction_count >= ATM_System.day_transaction_limit:
            print("\nDaily transaction limit reached.")
            return

        db.execute_query("SELECT * FROM users WHERE user_name = %s", (user_name,))
        user = db.fetchone_query()

        if not user:
            print("\nUser not Found!")
            return

        db.execute_query("SELECT * FROM atms WHERE atm_name = %s", (atm_name,))
        atm = db.fetchone_query()

        if not atm:
            print("\nATM not Found!")
            return

        user_bank = user[2]
        atm_bank = atm[2]

        if user_bank != atm_bank:
            print("\nDeposit not allowed from different Bank's ATM.")
            return

        if amount <= 0:
            print("\nInvalid amount!")
            return

        if amount > ATM_System.single_transaction_limit:
            print("\nSingle transaction limit exceeded.")
            return

        if user[7] >= ATM_System.user_transaction_limit:
            print("\nUser's daily transaction limit reached.")
            return

        new_user_balance = user[6] + amount
        new_atm_balance = atm[3] + amount

        db.execute_query("UPDATE users SET balance=%s, day_transaction_count=%s WHERE user_name=%s", (new_user_balance, user[7] + 1, user_name))
        db.execute_query("UPDATE atms SET atm_balance=%s WHERE atm_name=%s", (new_atm_balance, atm_name))
        db.execute_query("UPDATE banks SET bank_balance = bank_balance + %s WHERE bank_name=%s", (amount, user_bank))

        ATM_System.transaction_count += 1

        print(f"\n{amount} Rs. deposited successfully.")
        print("Current Balance:", new_user_balance)
        
    # define staticmethod to withdraw money
    @staticmethod
    def withdraw(user_name, atm_name, amount):
        if ATM_System.transaction_count >= ATM_System.day_transaction_limit:
            print("\nDaily transaction limit reached.")
            return

        db.execute_query("SELECT * FROM users WHERE user_name=%s", (user_name,))
        user = db.fetchone_query()

        db.execute_query("SELECT * FROM atms WHERE atm_name=%s", (atm_name,))
        atm = db.fetchone_query()

        if not user:
            print("\nUser not Found!")
            return

        if not atm:
            print("\nATM not Found!")
            return
        
        if amount <= 0:
            print("\nInvalid amount!")
            return

        user_bank = user[2]
        atm_bank = atm[2]

        extra_charge = 0
        if user_bank != atm_bank:
            extra_charge = amount * 0.05

        total_amount = amount + extra_charge
        if total_amount > user[6]:
            print("\nInsufficient Balance!")
            return

        if amount > atm[3]:
            print("\nATM has Insufficient Cash!")
            return

        if amount > ATM_System.single_transaction_limit:
            print("\nSingle transaction limit exceeded.")
            return

        if user[7] >= ATM_System.user_transaction_limit:
            print("\nUser's daily transaction limit reached.")
            return

        new_user_balance = user[6] - total_amount
        new_atm_balance = atm[3] - amount

        db.execute_query("UPDATE users SET balance=%s, day_transaction_count=%s WHERE user_name=%s", (new_user_balance, user[7] + 1, user_name))
        db.execute_query("UPDATE atms SET atm_balance=%s WHERE atm_name=%s", (new_atm_balance, atm_name))
        db.execute_query("UPDATE banks SET bank_balance = bank_balance - %s WHERE bank_name=%s", (amount, user_bank))

        ATM_System.transaction_count += 1

        if extra_charge > 0:
            print(f"\n{amount} Rs. withdrawn with 5% extra charge.")
        else:
            print(f"\n{amount} Rs. withdrawn Successfully.")

        print("Current Balance:", new_user_balance)
        
# define function to interact with user
def menu():
    # create object of Bank, ATM and ATM_System
    bank_object_1 = Bank("SBI", 500000)
    # bank_object_1.insert_bank()
    
    atm_object_1 = ATM("SBI-ATM", "SBI", 250000)
    # atm_object_1.insert_atm()
    
    bank_object_2 = Bank("HDFC", 300000)
    # bank_object_2.insert_bank()
    
    atm_object_2 = ATM("HDFC-ATM", "HDFC", 150000)
    # atm_object_2.insert_atm()

    bank_object_3 = Bank("BOI", 400000)
    # bank_object_3.insert_bank()
    
    atm_object_3 = ATM("BOI-ATM", "BOI", 200000)
    # atm_object_3.insert_atm()
    
    atm_system = ATM_System()
    
    print("\nWelcome to an ATM!")

    while True:
        print("\n1. Login")
        print("2. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                user_name = input("\nEnter User Name: ")

                user = User.get_user(user_name)

                if not user:
                    bank_name = input("\nEnter Bank Name: ")

                    bank = Bank.get_bank(bank_name)
                    if not bank:
                        print("\nInvalid Bank Name!")
                        continue

                    atm_name = input("\nEnter ATM Name (Bank-ATM): ")

                    atm = ATM.get_atm(atm_name)
                    if not atm or atm[2] != bank_name:
                        print("\nInvalid ATM name for Selected Bank!")
                        continue

                    user_object = User(user_name, bank_name, atm_name)
                    user_object.insert_user()

                    print("\nPlease Login Again.")
                    continue

                card_number = int(input("\nEnter Card Number: "))
                pin_number = int(input("Enter PIN: "))

                if user[4] == card_number and user[5] == pin_number:
                    print(f"\nWelcome {user_name}!")

                    while True:
                        print("\n1. Deposit")
                        print("2. Withdraw")
                        print("3. Display Details")
                        print("4. Change PIN")
                        print("5. Logout")

                        try:
                            user_choice = int(input("\nEnter choice: "))

                            if user_choice == 1:
                                atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ")
                                
                                if atm_name == "Quit" or atm_name == "quit":
                                    continue

                                amount = input("\nEnter amount to deposit or Quit to this operation: ")
                                if amount == "Quit" or amount == "quit":
                                    continue

                                atm_system.deposit(user_name, atm_name, float(amount))
                            elif user_choice == 2:
                                atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ")

                                if atm_name == "Quit" or atm_name == "quit":
                                    continue

                                amount = input("\nEnter amount to withdraw or Quit to this operation: ") 
                                if amount == "Quit" or amount == "quit":
                                    continue

                                atm_system.withdraw(user_name, atm_name, float(amount))
                            elif user_choice == 3:
                                User.display_details(user_name)
                            elif user_choice == 4:
                                new_pin = int(input("\nEnter New PIN: "))
                                User.update_user(user_name, new_pin)
                            elif user_choice == 5:
                                print("\nLogged out Successfully!")
                                break
                            else:
                                print("\nPlease enter valid choice (1-5).")
                        except ValueError:
                            print("\nValueError: Please Enter valid input only!")
                else:
                    print("\nInvalid Credentials!")
            elif choice == 2:
                print("\nYou selected Exit.\nThank You!")
                db.close_conn()
                break
            else:
                print("\nPlease enter valid choice (1-2).")
        except ValueError:
            print("\nValueError: Please Enter valid input only!")
            
# start ATM_System from here
menu()