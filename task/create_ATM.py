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

# define Bank class to manage bank details
class Bank:
    banks = {'SBI': 500000, 'HDFC': 300000}
    
    # constructor to initialize bank name and bank balance
    def __init__(self, bank_name, bank_balance):
        self.bank_name = bank_name
        self.bank_balance = bank_balance

    # define function to insert bank details
    def insert_bank(self):
        Bank.banks[self.bank_name] = self.bank_balance

    # define function to update bank details
    def update_bank(self):
        if self.bank_name in Bank.banks:
            Bank.banks[self.bank_name] = self.bank_balance
        else:
            print(f"\nBank '{self.bank_name}' does not exist.\nPlease insert it first.")

    # define function to delete bank details
    def delete_bank(self):
        if self.bank_name in Bank.banks:
            del Bank.banks[self.bank_name]
        else:
            print(f"\nBank '{self.bank_name}' does not exist.")

# define ATM class to manage ATM details
class ATM:
    atms = {'SBI-ATM': 200000, 'HDFC-ATM': 100000}

    # constructor to initialize ATM name and ATM balance
    def __init__(self, atm_name, atm_balance):
        self.atm_name = atm_name
        self.atm_balance = atm_balance

    # define function to insert ATM details
    def insert_atm(self):
        ATM.atms[self.atm_name] = self.atm_balance

    # define function to update ATM details
    def update_atm(self):
        if self.atm_name in ATM.atms:
            ATM.atms[self.atm_name] = self.atm_balance
        else:
            print(f"\nATM '{self.atm_name}' does not exist.\nPlease insert it first.")

    # define function to delete ATM details
    def delete_atm(self):
        if self.atm_name in ATM.atms:
            del ATM.atms[self.atm_name]
        else:
            print(f"\nATM '{self.atm_name}' does not exist.")

# define User class to manage user details
class User:
    user = {'Khushi': {'card': 1234567890101112, 'pin': 1234, 'bank_name': 'SBI', 'atm_name': 'SBI-ATM', 'balance': 25000.0, 'day_transaction_count': 0}}

    def __init__(self):
        pass
        
    # define function to insert user details
    def insert_user(self, user_name, bank_name, atm_name):
        card_number = randint(10 ** 15, (10 ** 16) - 1)
        pin_number = randint(1000, 9999)

        User.user[user_name] = {'card': card_number, 'pin': pin_number, 'bank_name': bank_name, 'atm_name': atm_name, 'balance': 1000.0, 'day_transaction_count': 0}

    # define function to update user details
    def update_user(self, user_name, bank_name, atm_name):
        if user_name in User.user:
            User.user[user_name]['bank_name'] = bank_name
            User.user[user_name]['atm_name'] = atm_name
        else:
            print("\nUser not Found.")

    # define function to delete user details
    def delete_user(self, user_name):
        if user_name in User.user:
            del User.user[user_name]
        else:
            print("\nUser not Found.")

# define ATM_System class to manage ATM system
class ATM_System:
    day_transaction_limit = 50
    user_transaction_limit = 3
    single_transaction_limit = 10000
    transaction_count = 0

    def __init__(self):
        pass
    
    # define function to deposite money into ATM
    def deposite(self, user_name, amount):
        if ATM_System.transaction_count >= ATM_System.day_transaction_limit:
            print("\nDaily transaction limit reached.\nPlease try again tomorrow.")
            return
        else:
            if user_name in User.user:
                if User.user[user_name]['day_transaction_count'] >= ATM_System.user_transaction_limit:
                    print(f"\nUser '{user_name}' has exceeded daily transaction limit.")
                    return
                else:
                    if amount > ATM_System.single_transaction_limit:
                        print(f"\nSingle transaction limit is {ATM_System.single_transaction_limit} Rs.")
                        return
                    
                    if amount <= 0:
                        print("\nAmount must be greater than zero.")
                        return
                    
                    User.user[user_name]['balance'] += amount
                    ATM.atms[User.user[user_name]['atm_name']] += amount
                    Bank.banks[User.user[user_name]['bank_name']] += amount

                    User.user[user_name]['day_transaction_count'] += 1
                    ATM_System.transaction_count += 1
                    
                    print(f"\n{amount} Rs. deposited successfully.")
            else:
                print("\nUser not Found.")

    # define function to withdraw money from ATM
    def withdraw(self, user_name, amount, atm_name):
        if ATM_System.transaction_count >= ATM_System.day_transaction_limit:
            print("\nDaily transaction limit reached.\nPlease try again tomorrow.")
            return
        else:
            if user_name in User.user:
                if User.user[user_name]['day_transaction_count'] >= ATM_System.user_transaction_limit:
                    print(f"\nUser '{user_name}' has exceeded daily transaction limit.")
                    return
                else:
                    if amount > ATM_System.single_transaction_limit:
                        print(f"\nSingle transaction limit is {ATM_System.single_transaction_limit} Rs.")
                        return
                    
                    if amount <= 0:
                        print("\nAmount must be greater than zero.")
                        return
                    
                    if atm_name not in ATM.atms:
                        print(f"\n'{atm_name}' ATM does not exist.")
                        return
                    else:
                        if User.user[user_name]['atm_name'] != atm_name:
                            amount -= amount * 0.05
                        
                            if ATM.atms[atm_name] >= amount and User.user[user_name]['balance'] >= amount:
                                User.user[user_name]['balance'] -= amount
                                ATM.atms[atm_name] -= amount
                                Bank.banks[User.user[user_name]['bank_name']] -= amount
                                
                                User.user[user_name]['day_transaction_count'] += 1
                                ATM_System.transaction_count += 1
                                
                                print(f"\n{amount} Rs. withdrawn successfully. (5% cut applied for using other Bank's ATM)")
                            else:
                                print("\nInsufficient balance or ATM does not have enough funds.")
                                return
                        else:
                            if ATM.atms[atm_name] >= amount and User.user[user_name]['balance'] >= amount:
                                User.user[user_name]['balance'] -= amount
                                ATM.atms[atm_name] -= amount
                                Bank.banks[User.user[user_name]['bank_name']] -= amount
                                
                                User.user[user_name]['day_transaction_count'] += 1
                                ATM_System.transaction_count += 1
                                
                                print(f"\n{amount} Rs. withdrawn successfully.")
                            else:
                                print("\nInsufficient balance or ATM does not have enough funds.")
                                return
            else:
                print("\nUser not Found.")

    # define function to display user details
    def display_details(self, user_name):
        if user_name in User.user:
            print(f"User Name: {user_name}")
            print(f"Card Number: {User.user[user_name]['card']}")
            print(f"Pin Number: {User.user[user_name]['pin']}")
            print(f"Bank Name: {User.user[user_name]['bank_name']}")
            print(f"ATM Name: {User.user[user_name]['atm_name']}")
            print(f"Balance: {User.user[user_name]['balance']}")
        else:
            print("\nUser not Found.")

# define menu function to interact with user
def menu():
    # example data for Bank and ATM
    bank_object = Bank('BOI', 400000)
    bank_object.insert_bank()

    atm_object = ATM('BOI-ATM', 150000)
    atm_object.insert_atm()

    # start the menu from here
    print("\nWelcome to an ATM !!!")
    
    while True:
        try:
            print("\n1. Login")
            print("2. Exit")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                user_object = User()
                atm_system = ATM_System()

                try:
                    user_name = input("\nEnter your name: ")

                    if user_name not in User.user:
                        try:
                            bank_name = input("Enter your Bank name: ")
                            atm_name = input("Enter your ATM name (Bank-ATM): ")
                            
                            if bank_name not in Bank.banks:
                                print("Invalid bank name.")
                                continue

                            if atm_name not in ATM.atms:
                                print("Invalid ATM name.")
                                continue
                        except Exception:
                            print("\nPlease Enter valid input only.")
                            continue

                        user_object.insert_user(user_name, bank_name, atm_name)
                        
                        print(f"\nUser '{user_name}' inserted successfully.")
                        print("\nHere are your credentials:")
                        
                        atm_system.display_details(user_name)
                        print("\nPlease login with your credentials.")

                        continue

                    card_number = int(input("Enter your card number: "))
                    pin_number = int(input("Enter your pin number: "))
                except Exception:
                    print("\nPlease Enter valid credentials.")
                    
                    continue

                if user_name in User.user and User.user[user_name]['card'] == card_number and User.user[user_name]['pin'] == pin_number:
                    print(f"\nWelcome {user_name}!")
                    
                    while True:
                        try:
                            print("\n1. Deposite Money")
                            print("2. Withdraw Money")
                            print("3. Display Account Details")
                            print("4. Logout")

                            user_choice = int(input("\nEnter your choice: "))

                            if user_choice == 1:
                                amount = float(input("\nEnter amount to deposite: "))
                                atm_system.deposite(user_name, amount)
                            elif user_choice == 2:
                                amount = float(input("\nEnter amount to withdraw: "))
                                atm_name = input("Enter ATM name (Bank-ATM): ")
                                
                                atm_system.withdraw(user_name, amount, atm_name)
                            elif user_choice == 3:
                                atm_system.display_details(user_name)
                            elif user_choice == 4:
                                print(f"\nYou have logged out successfully!\nThank You!")
                                break
                            else:
                                print("\nPlease Enter valid choice (1-4).")
                        except Exception:
                            print("\nPlease Enter valid input only.")
                else:
                    print("\nInvalid credentials.\nPlease try again.")
            elif choice == 2:
                print("\nYou selected Exit.\nThank You!")
                break
            else:
                print("\nPlease Enter valid choice (1-2).")
        except Exception:
            print("\nPlease Enter valid integer input only.")

# start the ATM system
menu()