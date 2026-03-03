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

from random import randint # to generate card number and pin number randomly
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
    
    def __init__(self, name, bank, balance):
        '''constructor to intialize ATM details'''
        self.name = name
        self.bank = bank
        self.balance = balance
class User:
    '''This model manages user details'''
    
    def __init__(self, name, bank):
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
    
    DAY_TRANSACTION_LIMIT = 50
    USER_TRANSACTION_LIMIT = 3
    SINGLE_TRANSACTION_LIMIT = 10000
    TRANSACTION_COUNT = 0

    def __init__(self):
        '''constructor to intialize data dictionary'''
        self.banks = {}
        self.atms = {}
        self.users = {}
        
    def create_bank(self, name, balance):
        if name in self.banks:
            return {"Success": False, "Message": "\nBank already exists!"}

        bank = Bank(name, balance)
        self.banks[name] = bank
        return True
    
    def create_atm(self, bank_name, atm_name, balance):
        bank = self.banks.get(bank_name)
        
        if not bank:
            return {"Success": False, "Message": "\nBank not Found!"}

        if atm_name in self.atms:
            return {"Success": False, "Message": "\nATM already exists!"}

        atm = ATM(atm_name, bank, balance)
        self.atms[atm_name] = atm
        bank.atms[atm_name] = atm

        return True
    
    def create_user(self, user_name, bank_name):
        bank = self.banks.get(bank_name)
        
        if not bank:
            return {"Success": False, "Message": "\nBank not Found!"}

        if user_name in self.users:
            return False

        user = User(user_name, bank)
        self.users[user_name] = user
        bank.users[user_name] = user

        return {"Success": True, "Card": user.card, "PIN": user.pin}
    
    def authenticate_user(self, user_name, card, pin):
        user = self.users.get(user_name)
        
        if not user:
            return False

        return user.card == card and user.pin == pin
    
    def check_conditions(self, user_name, atm_name, amount):
        if ATMSystemController.TRANSACTION_COUNT >= ATMSystemController.DAY_TRANSACTION_LIMIT:
            return {"Success": False, "Message": "\nDaily transaction limit reached."}

        user = self.users.get(user_name)
        atm = self.atms.get(atm_name)

        if not user:
            return {"Success": False, "Message": "\nUser not Found!"}

        if not atm:
            return {"Success": False, "Message": "\nATM not Found!"}

        if user.daily_transaction_count >= ATMSystemController.USER_TRANSACTION_LIMIT:
            return {"Success": False, "Message": "\nUser's daily transaction limit reached."}

        if amount <= 0:
            return {"Success": False, "Message": "\nInvalid amount!"}

        if amount > ATMSystemController.SINGLE_TRANSACTION_LIMIT:
            return {"Success": False, "Message": "\nSingle transaction limit exceeded."}
        
        return {"Success": True, "Message": None}
    
    def deposit(self, user_name, atm_name, amount):
        result = self.check_conditions(user_name, atm_name, amount)
        
        if result.get("Success"):
            user = self.users.get(user_name)
            atm = self.atms.get(atm_name)
        
            if user.bank != atm.bank:
                return {"Success": False, "Message": "\nDeposit allowed only in Your Bank's ATM."}
            
            user.balance += amount
            atm.balance += amount
            user.bank.balance += amount

            user.daily_transaction_count += 1
            ATMSystemController.TRANSACTION_COUNT += 1
            
            return {"Success": True, "Message": f"\n{amount} Rs. deposited Successfully.\nCurrent Balance: {user.balance}"}
        else:
            return {"Success": False, "Message": result.get("Message")}
        
    def withdraw(self, user_name, atm_name, amount):
        result = self.check_conditions(user_name, atm_name, amount)
        
        if result.get("Success"):
            user = self.users.get(user_name)
            atm = self.atms.get(atm_name)
            
            extra_charge = 0
            if user.bank != atm.bank:
                extra_charge = amount * 0.05

            total_amount = amount + extra_charge

            if user.balance < total_amount:
                return {"Success": False, "Message": "\nInsufficient Balance!"}

            if atm.balance < amount:
                return {"Success": False, "Message": "\nATM has Insufficient Cash!"}

            user.balance -= total_amount
            atm.balance -= amount
            user.bank.balance -= amount

            user.daily_transaction_count += 1
            ATMSystemController.TRANSACTION_COUNT += 1

            return {"Success": True, "Message": f"\n{amount} Rs. withdrawn Successfully.\nCurrent Balance: {user.balance}"}
        else:
            return {"Success": False, "Message": result.get("Message")}
        
    def get_user_details(self, user_name):
        user = self.users.get(user_name)
        
        if not user:
            return None

        return {"Name": user.name, "Bank": user.bank.name, "Card": user.card, "Balance": user.balance}
    
def menu():
    '''This view interact with user'''
    
    atm_system = ATMSystemController()

    # create Bank and ATM with object
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
                        bank_name = input("\nEnter Bank Name: ")
                        
                        result = atm_system.create_user(user_name, bank_name)

                        if not result.get("Success"):
                            print(result.get("Message"))
                            continue

                        print("\nUser created successfully!\nHere is Your Credentials:")
                        print(f"\nUser Name: {user_name}\nCard: {result.get('Card')}\nPIN: {result.get('PIN')}")
                        print("\nPlease Login Again.")
                        
                        continue

                    try:
                        card = int(input("\nEnter Card: "))
                        pin = int(input("\nEnter PIN: "))
                    except ValueError:
                        print("\nValueError: Please Enter valid value of input.")
                        continue

                    if not atm_system.authenticate_user(user_name, card, pin):
                        print("Invalid Credentials!")
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
                                    atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ")
                                    
                                    if atm_name.lower() == "quit":
                                        continue

                                    amount = input("\nEnter amount or Quit to this operation: ")
                                    
                                    if amount.lower() == "quit":
                                        continue
                                except ValueError:
                                    print("\nValueError: Please Enter valid value of input.")
                            
                                result = atm_system.deposit(user_name, atm_name, float(amount))
                                
                                if result.get("Success"):
                                    print(result.get('Message'))
                                else:
                                    print(result.get("Message"))
                            elif user_choice == 2:
                                try:
                                    atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ")

                                    if atm_name.lower() == "quit":
                                        continue

                                    amount = input("\nEnter amount or Quit to this operation: ")
                                        
                                    if amount.lower() == "quit":
                                        continue
                                except ValueError:
                                    print("\nValueError: Please Enter valid value of input.")
                                
                                result = atm_system.withdraw(user_name, atm_name, float(amount))
                                
                                if result.get("Success"):
                                    print(result.get("Message"))
                                else:
                                    print(result.get("Message"))
                            elif user_choice == 3:
                                details = atm_system.get_user_details(user_name)
                                
                                print("\nHere is your details:")
                                for key, value in details.items():
                                    print(f"{key}: {value}")
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