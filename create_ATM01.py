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

# import randint function to generate random card number and pin number
from random import randint

# define Bank class to manage Bank details
class Bank:
    banks = {}

    # constructor to initialize bank details
    def __init__(self, bank_name, bank_balance):
        self.bank_name = bank_name
        self.bank_balance = bank_balance
        
        self.atms = {}
        self.users = {}

        Bank.banks[bank_name] = self

    # define function to insert bank object
    def insert_bank(self):
        Bank.banks[self.bank_name] = self

    # define function to insert atm 
    def insert_atm(self, atm):
        self.atms[atm.atm_name] = atm

    # define function to insert user
    def insert_user(self, user):
        self.users[user.user_name] = user

    # define staticmethod to update bank details
    @staticmethod
    def update_bank(bank_name, bank_balance):
        if Bank.bank_exist(bank_name):
            Bank.banks[bank_name].bank_balance = bank_balance
        else:
            print("\nBank does not exist.")

    # define staticmethod to delete bank object
    @staticmethod
    def delete_bank(bank_name):
        if Bank.bank_exist(bank_name):
            bank = Bank.banks[bank_name]

            for atm in list(bank.atms.keys()):
                ATM.delete_atm(atm)

            for user in list(bank.users.keys()):
                User.delete_user(user)

            del Bank.banks[bank_name]
        else:
            print("\nBank does not exist.")

    # define classmethod to check if bank exist or not
    @classmethod
    def bank_exist(cls, bank_name):
        return bank_name in cls.banks

    # define classmethod to get bank details
    @classmethod
    def get_bank(cls, bank_name):
        return cls.banks.get(bank_name)

# define ATM class to manage ATM details
class ATM:
    atms = {}

    # constructor to initialize ATM details
    def __init__(self, bank, atm_name, atm_balance):
        if isinstance(bank, str):
            bank = Bank.get_bank(bank)

        self.bank = bank
        self.atm_name = atm_name
        self.atm_balance = atm_balance

        ATM.atms[atm_name] = self

        if bank:
            bank.insert_atm(self)

    # define function to insert ATM object
    def insert_atm(self):
        ATM.atms[self.atm_name] = self

    # define staticmethod to update ATM details
    @staticmethod
    def update_atm(atm_name, atm_balance):
        if atm_name in ATM.atms:
            ATM.atms[atm_name].atm_balance = atm_balance
        else:
            print("\nATM does not exist.")

    # define staticmethod to delete ATM object
    @staticmethod
    def delete_atm(atm_name):
        if atm_name in ATM.atms:
            atm = ATM.atms[atm_name]
            
            if atm.bank and atm_name in atm.bank.atms:
                del atm.bank.atms[atm_name]
            
            del ATM.atms[atm_name]
        else:
            print("\nATM does not exist.")

    # define classmethod to get ATM and Bank details
    @classmethod
    def get_atm_bank(cls, atm_name):
        atm = cls.atms.get(atm_name)

        if atm:
            return atm.bank.bank_name
        
        return None

    # define classmethod to get ATM details
    @classmethod
    def get_atm(cls, atm_name):
        return cls.atms.get(atm_name)

# define User class to manage user details
class User:
    user = {}

    # constructor to intialize user details
    def __init__(self, user_name, bank, atm_name):
        self.user_name = user_name
        self.bank = bank
        self.atm_name = atm_name

        self.card = User.generate_card()
        self.pin = User.generate_pin()

        self.balance = 1000.0
        self.day_transaction_count = 0

        User.user[user_name] = self
        bank.insert_user(self)

    # define function to insert user object
    def insert_user(self):
        User.user[self.user_name] = self

    # define staticmethod to update user details
    @staticmethod
    def update_user(user_name, pin):
        if User.user_exist(user_name):
            User.user[user_name].pin = pin
        else:
            print("\nUser not Found.")

    # define staticmethod to delete user object
    @staticmethod
    def delete_user(user_name):
        if User.user_exist(user_name):
            user = User.user[user_name]
            
            if user.bank and user_name in user.bank.users:
                del user.bank.users[user_name]
            
            del User.user[user_name]
        else:
            print("\nUser not Found.")

    # define staticmethod to display user details
    @staticmethod
    def display_details(user_name):
        user = User.get_user(user_name)

        if user:
            print(f"\nUser Name: {user.user_name}")
            print(f"Card Number: {user.card}")
            print(f"Bank Name: {user.bank.bank_name}")
            print(f"ATM Name: {user.atm_name}")
            print(f"Balance: {user.balance}")
        else:
            print("\nUser not found.")

    # define staticmethod to generate card randomly
    @staticmethod
    def generate_card():
        return randint(10 ** 15, (10 ** 16 - 1))

    # define staticmethod to generate pin randomly
    @staticmethod
    def generate_pin():
        return randint(1000, 9999)

    # define classmethod to check if user exist or not
    @classmethod
    def user_exist(cls, user_name):
        return user_name in cls.user

    # define classmethod to get user details
    @classmethod
    def get_user(cls, user_name):
        return cls.user.get(user_name)

# define ATM_System class to manage ATM system
class ATM_System:
    day_transaction_limit = 50
    user_transaction_limit = 3
    single_transaction_limit = 10000
    transaction_count = 0

    # define staticmethod to deposite money 
    @staticmethod
    def deposite(user_name, atm_name, amount):
        if ATM_System.transaction_count >= ATM_System.day_transaction_limit:
            print("\nDaily transaction limit reached.")
            return

        user = User.get_user(user_name)
        atm = ATM.get_atm(atm_name)

        if not user:
            print("\nUser not found.")
            return

        if not atm:
            print("\nATM does not exist.")
            return

        if user.day_transaction_count >= ATM_System.user_transaction_limit:
            print("\nUser's daily transaction limit reached.")
            return

        if amount <= 0:
            print("\nInvalid Amount!")
            return

        if amount > ATM_System.single_transaction_limit:
            print("\nSingle transaction limit exceeded.")
            return

        if user.bank != atm.bank:
            print("\nDeposite not allowed from different Bank's ATM.")
            return

        user.balance += amount
        atm.atm_balance += amount
        user.bank.bank_balance += amount

        user.day_transaction_count += 1
        ATM_System.transaction_count += 1

        print(f"\n{amount} Rs. Deposited Successfully.")
        print(f"Current Balance: {user.balance}")

    # define staticmethod to withdraw money
    @staticmethod
    def withdraw(user_name, atm_name, amount):
        if ATM_System.transaction_count >= ATM_System.day_transaction_limit:
            print("\nDaily transaction limit reached.")
            return

        user = User.get_user(user_name)
        atm = ATM.get_atm(atm_name)

        if not user:
            print("\nUser not found.")
            return

        if not atm:
            print("\nATM does not exist.")
            return

        if user.day_transaction_count >= ATM_System.user_transaction_limit:
            print("\nUser's daily transaction limit reached.")
            return

        if amount <= 0:
            print("\nInvalid Amount!")
            return

        if amount > ATM_System.single_transaction_limit:
            print("\nSingle transaction limit exceeded.")
            return

        extra_charge = 0
        if user.bank != atm.bank:
            extra_charge = amount * 0.05

        total_amount = amount + extra_charge
        if user.balance < total_amount:
            print("\nInsufficient Balance !")
            return

        if atm.atm_balance < amount:
            print("\nATM has Insufficient Cash !")
            return

        user.balance -= total_amount
        atm.atm_balance -= amount
        user.bank.bank_balance -= amount

        user.day_transaction_count += 1
        ATM_System.transaction_count += 1

        if extra_charge > 0:
            print(f"\n{amount} Rs. withdrawn with 5% Extra Charge.")
            print(f"Current Balance: {user.balance}")
        else:
            print(f"\n{amount} Rs. withdrawn Successfully.")
            print(f"Current Balance: {user.balance}")

# define function to interact with user
def menu():
    # create object of Bank, ATM and ATM_System
    bank_object_1 = Bank("SBI", 500000)
    atm_object_1 = ATM(bank_object_1, "SBI-ATM", 250000)

    bank_object_2 = Bank("HDFC", 300000)
    atm_object_2 = ATM(bank_object_2, "HDFC-ATM", 150000)

    bank_object_3 = Bank("BOI", 400000)
    atm_object_3 = ATM(bank_object_3, "BOI-ATM", 200000)

    atm_system = ATM_System()

    print("\nWelcome to an ATM!")

    while True:
        print("\n1. Login")
        print("2. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                try:
                    user_name = input("\nEnter User name: ")

                    if not User.user_exist(user_name):
                        bank_name = input("\nEnter Bank name: ")

                        bank = Bank.get_bank(bank_name)
                        if not bank:
                            print("\nInvalid Bank Name !")
                            continue

                        atm_name = input("\nEnter ATM name (Bank-ATM): ")

                        atm = ATM.get_atm(atm_name)
                        if not atm or atm.bank != bank:
                            print("\nInvalid ATM name for selected Bank !")
                            continue

                        user_object = User(user_name, bank, atm_name)

                        print("\nUser Created Successfully.")
                        print("\nHere Your Credentials:")

                        print("\nCard:", user_object.card)
                        print("PIN:", user_object.pin)

                        print("\nPlease Login again.")
                        continue

                    card_number = int(input("\nEnter Card Number (16-digit): "))
                    pin_number = int(input("\nEnter PIN (4-digit): "))

                    user = User.get_user(user_name)

                    if user and user.card == card_number and user.pin == pin_number:
                        print(f"\nWelcome {user_name} !")

                        while True:
                            print("\n1. Deposit")
                            print("2. Withdraw")
                            print("3. Display Details")
                            print("4. Logout")

                            try:
                                user_choice = int(input("\nEnter choice: "))

                                if user_choice == 1:
                                    atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ")

                                    if atm_name == "Quit" or atm_name == "quit":
                                        continue

                                    amount = input("\nEnter amount or Quit to this operation: ")
                                    
                                    if amount == "Quit" or amount == "quit":
                                        continue

                                    atm_system.deposite(user_name, atm_name, float(amount))
                                elif user_choice == 2:
                                    atm_name = input("\nEnter ATM name (Bank-ATM) or Quit to this operation: ")

                                    if atm_name == "Quit" or atm_name == "quit":
                                        continue

                                    amount = input("\nEnter amount or Quit to this operation: ")
                                    
                                    if amount == "Quit" or amount == "quit":
                                        continue

                                    atm_system.withdraw(user_name, atm_name, float(amount))
                                elif user_choice == 3:
                                    User.display_details(user_name)
                                elif user_choice == 4:
                                    print("\nLogged out Successfully!")   
                                    break
                                else:
                                    print("\nPlease Enter valid choice (1-4).")
                            except ValueError:
                                print("\nValueError: Please Enter valid value of input.")
                            except Exception:
                                print("\nPlease Enter valid input only.")
                    else:
                        print("\nInvalid Credentials!")
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

# start ATM_System from here
menu()