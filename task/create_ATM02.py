"""
Task - 12: Create an ATM machine.
- User should be able get money out of it.
- User should be able to deposite money into it.
- You must ask card number and pin before any transaction.
- User can get overall information about his bank account.
- There should be a limit in one time transaction and total transaction in a day.
(Consider day as from starting of script to exit)

- Limit on number of transaction.
- Let user choose the bank of ATM.
- Every ATM will have some initial balance.
- Every user has it's own bank.
- If user takes money from an ATM other than his bank take 5% cut in withdrawl amount.

Nice to have features:
- Insert, update and delete users. (Generate card number and PIN randomly)
- Insert, update and delete ATMs.
- Insert, update and delete banks.
- Insert money into ATM. (No database is needed for this it can be managed using dicts)

Hint: You can manage all this with data dictionary data type.
"""

from random import randint # Generate card number and PIN

class Bank:
    '''This model manages bank details'''
    
    def __init__(self, name, balance):
        '''constructor to intialize bank details'''
        self.name = name
        self.balance = balance
        
        self.atms = {}
        self.users = {}
        
class ATM:
    '''This model manages ATM details'''
    
    def __init__(self, name, bank: Bank, balance):
        '''constructor to intialize ATM details'''
        self.name = name
        self.bank = bank
        self.balance = balance
        
class User:
    '''This model manages user details'''
    
    def __init__(self, name, bank: Bank):
        '''constructor to intialize user details'''
        self.name = name
        self.bank = bank
        
        self.card = User.generate_card()
        self.pin = User.generate_pin()
        
        self.balance = 1000.0
        self.daily_transaction_count = 0

    @staticmethod
    def generate_card():
        return randint(10**15, (10**16 - 1))

    @staticmethod
    def generate_pin():
        return randint(1000, 9999) 
    
class ATMSystemController:
    '''This controller manages ATM System'''

    def __init__(self):
        '''constructor to intialize data dictionary'''
        self.banks = {}
        self.atms = {}
        self.users = {}
        
        self.day_transaction_limit = 50
        self.user_transaction_limit = 3
        self.single_transaction_limit = 10000
        self.transaction_count = 0
        
    def create_bank(self, name, balance):
        if name in self.banks:
            return {"success": False, "message": "\nBank already exists!"}

        bank = Bank(name, balance)
        self.banks[name] = bank
        return {"success": True, "message": "\nBank created Successfully."}
    
    def create_atm(self, bank_name, atm_name, balance):
        bank = self.banks.get(bank_name)
        
        if not bank:
            return {"success": False, "message": "\nBank not Found!"}

        if atm_name in self.atms:
            return {"success": False, "message": "\nATM already exists!"}

        atm = ATM(atm_name, bank, balance)
        self.atms[atm_name] = atm
        bank.atms[atm_name] = atm

        return {"success": True, "message": "\nATM created Successfully."}
    
    def create_user(self, user_name, bank_name):
        bank = self.banks.get(bank_name)
        
        if not bank:
            return {"success": False, "message": "\nBank not Found!"}

        if user_name in self.users:
            return {"success": False, "message": "\nUser already exists!"}

        user = User(user_name, bank)
        self.users[user_name] = user
        bank.users[user_name] = user

        return {"success": True, "card": user.card, "pin": user.pin}
    
    def authenticate_user(self, user_name, card, pin):
        user = self.users.get(user_name)

        if not user:
            return {"success": False, "message": "\nUser not Found!"}

        if user.card == card and user.pin == pin:
            return {"success": True}

        return {"success": False, "message": "\nInvalid Credentials!"}
        
    
    def check_conditions(self, user_name, atm_name, amount):
        user = self.users.get(user_name)
        atm = self.atms.get(atm_name)

        if self.transaction_count >= self.day_transaction_limit:
            return {"success": False, "message": "\nDaily transaction limit reached."}

        if not user:
            return {"success": False, "message": "\nUser not Found!"}

        if not atm:
            return {"success": False, "message": "\nATM not Found!"}

        if user.daily_transaction_count >= self.user_transaction_limit:
            return {"success": False, "message": "\nUser's daily transaction limit reached."}

        if amount <= 0:
            return {"success": False, "message": "\nInvalid amount!"}

        if amount > self.single_transaction_limit:
            return {"success": False, "message": "\nSingle transaction limit exceeded."}
        
        return {"success": True, "user": user, "atm": atm}
    
    def deposit(self, user_name, atm_name, amount):
        result = self.check_conditions(user_name, atm_name, amount)

        if not result.get("success"):
            return result

        user = result.get("user")
        atm = result.get("atm")
        
        if user.bank != atm.bank:
            return {"success": False, "message": "\nDeposit allowed only in Your Bank's ATM."}
            
        user.balance += amount
        atm.balance += amount
        user.bank.balance += amount

        user.daily_transaction_count += 1
        self.transaction_count += 1
            
        return {"success": True, "message": f"\n{amount} Rs. deposited Successfully.\nCurrent Balance: {user.balance}"}
        
    def withdraw(self, user_name, atm_name, amount):
        result = self.check_conditions(user_name, atm_name, amount)

        if not result.get("success"):
            return result

        user = result.get("user")
        atm = result.get("atm")
    
        extra_charge = 0
        if user.bank != atm.bank:
            extra_charge = amount * 0.05

        total_amount = amount + extra_charge

        if user.balance < total_amount:
            return {"success": False, "message": "\nInsufficient Balance!"}

        if atm.balance < amount:
            return {"success": False, "message": "\nATM has Insufficient Cash!"}

        user.balance -= total_amount
        user.bank.balance -= amount
        atm.balance -= amount
        atm.bank.balance += extra_charge

        user.daily_transaction_count += 1
        self.transaction_count += 1
        
        if extra_charge > 0:
            return {"success": True, "message": f"\n{amount} Rs. withdrawn Successfully with 5% extra charge (Using another Bank's ATM).\nExtra Charge: {extra_charge}\nCurrent Balance: {user.balance}"}
        else:
            return {"success": True, "message": f"\n{amount} Rs. withdrawn Successfully.\nCurrent Balance: {user.balance}"}
        
    def get_user_details(self, user_name):
        user = self.users.get(user_name)

        if not user:
            return {"success": False, "message": "\nUser not Found!"}

        return {"success": True, "data": {"name": user.name, "bank": user.bank.name, "card": user.card, "balance": user.balance}}

def menu():
    '''This view interact with user'''
    
    atm_system = ATMSystemController()

    # create Bank and ATM 
    atm_system.create_bank("SBI", 500000)
    atm_system.create_bank("HDFC", 300000)
    atm_system.create_bank("BOI", 400000)

    atm_system.create_atm("SBI", "SBI-ATM", 250000)
    atm_system.create_atm("HDFC", "HDFC-ATM", 150000)
    atm_system.create_atm("BOI", "BOI-ATM", 200000)

    print("\nWelcome to an ATM!")

    while True:
        print("\n1. Login")
        print("2. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                try:
                    user_name = input("\nEnter User Name: ")

                    if user_name not in atm_system.users:
                        bank_name = input("\nEnter Bank Name: ").upper()
                        
                        result = atm_system.create_user(user_name, bank_name)

                        if not result.get("success"):
                            print(result.get("message"))
                            continue

                        print("\nUser created Successfully!\nHere is Your Credentials:")
                        print(f"\nUser Name: {user_name}\nCard: {result.get('card')}\nPIN: {result.get('pin')}")
                        print("\nPlease Login Again.")
                        
                        continue

                    try:
                        card = int(input("\nEnter Card: "))
                        pin = int(input("\nEnter PIN: "))
                    except ValueError:
                        print("\nValueError: Please Enter valid value of input.")
                        continue

                    authenticate_result = atm_system.authenticate_user(user_name, card, pin)

                    if not authenticate_result.get("success"):
                        print(authenticate_result.get("message"))
                        continue

                    print(f"\nWelcome {user_name}!")
                    while True:
                        print("\n1. Deposit")
                        print("2. Withdraw")
                        print("3. Display Details")
                        print("4. Logout")
                        
                        try:
                            user_choice = int(input("\nEnter choice: "))

                            if user_choice == 1:
                                try:
                                    atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ").upper()
                                    
                                    if atm_name == "QUIT":
                                        continue

                                    amount = input("\nEnter amount or Quit to this operation: ")

                                    if amount.lower() == "quit":
                                        continue

                                    try:
                                        amount = float(amount)
                                    except ValueError:
                                        print("\nInvalid amount!")
                                        continue
                                except ValueError:
                                    print("\nValueError: Please Enter valid value of input.")
                            
                                result = atm_system.deposit(user_name, atm_name, amount)
                                
                                if result.get("success"):
                                    print(result.get('message'))
                                else:
                                    print(result.get("message"))
                            elif user_choice == 2:
                                try:
                                    atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ").upper()

                                    if atm_name == "QUIT":
                                        continue

                                    amount = input("\nEnter amount or Quit to this operation: ")

                                    if amount.lower() == "quit":
                                        continue

                                    try:
                                        amount = float(amount)
                                    except ValueError:
                                        print("\nInvalid amount!")
                                        continue
                                except ValueError:
                                    print("\nValueError: Please Enter valid value of input.")
                                
                                result = atm_system.withdraw(user_name, atm_name, amount)
                                
                                if result.get("success"):
                                    print(result.get("message"))
                                else:
                                    print(result.get("message"))
                            elif user_choice == 3:
                                details = atm_system.get_user_details(user_name)

                                if not details.get("success"):
                                    print(details.get("message"))
                                else:
                                    print("\nHere is your details:")
                                    
                                    for key, value in details.get("data").items():
                                        print(f"{key.capitalize()}: {value}")
                            elif user_choice == 4:
                                print("\nLogged out Successfully!")   
                                break
                            else:
                                print("\nPlease Enter valid choice (1-4).")
                        except ValueError:
                            print("\nValueError: Please Enter valid value of input.")
                        except Exception:
                            print("\nPlease Enter valid input only.")
                except ValueError:
                    print("\nValueError: Please Enter valid value of input.")
                except Exception:
                    print("\nPlease Enter valid input only.")
            elif choice == 2:
                print("\nYou selected Exit.\nThank you!")
                break
            else:
                print("\nPlease Enter valid choice (1-2).")
        except ValueError:
            print("\nValueError: Please Enter valid value of input.")
        except Exception:
            print("\nPlease Enter valid integer input only.")

menu() # start ATM System from here