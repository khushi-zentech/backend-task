from random import randint
from model.bank import Bank
from model.atm import ATM
from model.database import DatabaseConnection

class User:
    '''This model manages user details'''

    INSERT_USER = "INSERT INTO users (user_name, bank_name, atm_name, card, pin, balance, day_transaction_count) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    UPDATE_USER_NAME = "UPDATE users SET user_name = %s WHERE card = %s"
    UPDATE_PIN = "UPDATE users SET pin = %s WHERE card = %s"
    UPDATE_BALANCE = "UPDATE users SET balance = %s WHERE card = %s"
    DELETE_USER = "DELETE FROM users WHERE card = %s"
    GET_USER = "SELECT * FROM users WHERE card = %s"

    def __init__(self, user_name: str, bank_name: str, atm_name: str, db_instance: DatabaseConnection):
        '''constructor to intialize user details'''
        self.user_name = user_name
        self.db = db_instance

        self.bank = Bank(bank_name, 0.0, db_instance)
        self.atm = ATM(atm_name, self.bank, 0.0, db_instance)

        self.card = User.generate_card_number()
        self.pin = User.generate_pin()

        self.balance = 1000.0
        self.day_transaction_count = 0
        
    def insert(self):
        try:
            bank_exist = self.bank.exists(self.bank.bank_name)
            if not bank_exist.get("success"):
                return bank_exist

            atm_exist = self.atm.exists(self.atm.atm_name)
            if not atm_exist.get("success"):
                return atm_exist

            self.db.cursor.execute(User.INSERT_USER, (
                self.user_name,
                self.bank.bank_name,
                self.atm.atm_name,
                self.card,
                self.pin,
                self.balance,
                self.day_transaction_count
            ))

            self.db.connection.commit()

            return {
                "success": True,
                "message": f"\nUser created Successfully.\nCard: {self.card}\nPIN: {self.pin}"
            }
        except Exception as e:
            return {"success": False, "message": str(e)}

    def display_details(self, user_name: str):
        try:
            self.db.cursor.execute(User.GET_USER, (user_name,))
            user = self.db.cursor.fetchone()

            if not user:
                return {"success": False, "message": "\nUser not found!"}

            return {
                "success": True,
                "user_name": user.get("user_name"),
                "bank_name": user.get("bank_name"),
                "card": user.get("card"),
                "balance": user.get("balance")
            }
        except Exception as e:
            return {"success": False, "message": str(e)}

    def update_pin(self, card: str, new_pin: str):
        try:
            user_exists = self.exists(card)

            if not user_exists.get("success"):
                return user_exists

            self.db.cursor.execute(User.UPDATE_PIN, (new_pin, card))
            self.db.connection.commit()

            return {"success": True, "message": "\nPIN updated Successfully."}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def deposit(self, card: str, amount: float):
        try:
            self.db.cursor.execute(User.GET_USER, (card,))
            user = self.db.cursor.fetchone()

            current_balance = user.get("balance")

            new_balance = current_balance + amount

            self.db.cursor.execute(User.UPDATE_BALANCE, (new_balance, card))
            self.bank.update_bank_balance(self.bank.bank_name, amount)

            self.db.connection.commit()

            return {
                "success": True,
                "message": f"\n{amount} deposited Successfully.\nCurrent Balance: {new_balance}"
            }
        except Exception as e:
            return {"success": False, "message": str(e)}

    def withdraw(self, card: str, amount: float):
        try:
            self.db.cursor.execute(User.GET_USER, (card,))
            user = self.db.cursor.fetchone()

            current_balance = user.get("balance")

            if amount > current_balance:
                return {"success": False, "message": "\nInsufficient Balance!"}

            new_balance = current_balance - amount

            self.db.cursor.execute(User.UPDATE_BALANCE, (new_balance, card))

            self.bank.update_bank_balance(self.bank.bank_name, -amount)
            self.atm.update_atm_balance(self.atm.atm_name, -amount)

            self.db.connection.commit()

            return {
                "success": True,
                "message": f"\n{amount} withdraw Successfully.\nCurrent Balance: {new_balance}"
            }
        except Exception as e:
            return {"success": False, "message": str(e)}

    def exists(self, card: str):
        try:
            self.db.cursor.execute(User.GET_USER, (card,))
            user = self.db.cursor.fetchone()

            if user:
                return {"success": True}

            return {"success": False, "message": "\nUser not Found!"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    @staticmethod
    def generate_card_number():
        return str(randint(10**15, (10**16 - 1)))

    @staticmethod
    def generate_pin():
        return str(randint(1000, 9999))