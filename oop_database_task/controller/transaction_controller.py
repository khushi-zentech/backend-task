from model.bank import Bank
from model.atm import ATM
from model.user import User
from model.database import DatabaseConnection

class TransactionController:
    '''This controller manages transactions'''
    
    SINGLE_TRANSACTION_LIMIT = 20000
    DAILY_TRANSACTION_LIMIT = 50
    USER_TRANSACTIONS_LIMIT = 3

    GET_USER = "SELECT * FROM users WHERE user_name=%s"
    GET_USER_BY_CARD = "SELECT * FROM users WHERE card=%s AND pin=%s"
    GET_ATM = "SELECT * FROM atms WHERE atm_name=%s"

    def __init__(self, db_instance: DatabaseConnection):
        '''constructor to intialize transaction count'''
        self.db = db_instance
        self.transaction_count = 0

    def authenticate_user(self, card: str, pin: str):
        try:
            self.db.cursor.execute(TransactionController.GET_USER, (card, pin))
            user = self.db.cursor.fetchone()

            if not user:
                return {"success": False, "message": "\nInvalid Credentials!"}

            return {"success": True, "user": user}

        except Exception as e:
            return {"success": False, "message": str(e)}
        
    def authenticate_transaction(self, user_name: str, atm_name: str, amount: float):
        try:
            if self.transaction_count >= TransactionController.DAILY_TRANSACTION_LIMIT:
                return {"success": False, "message": "\nDaily transaction limit reached."}

            self.db.cursor.execute(TransactionController.GET_USER, (user_name,))
            user = self.db.cursor.fetchone()

            if not user:
                return {"success": False, "message": "\nUser not Found!"}

            self.db.cursor.execute(self.GET_ATM, (atm_name,))
            atm = self.db.cursor.fetchone()

            if not atm:
                return {"success": False, "message": "\nATM not Found!"}

            if user.get("day_transaction_count") >= TransactionController.USER_TRANSACTIONS_LIMIT:
                return {"success": False, "message": "\nUser's daily transaction limit reached."}

            if amount <= 0:
                return {"success": False, "message": "\nInvalid amount!"}

            if amount > TransactionController.SINGLE_TRANSACTION_LIMIT:
                return {"success": False, "message": "\nSingle transaction limit exceeded."}

            return {"success": True, "user": user, "atm": atm}
        except Exception as e:
            return {"success": False, "message": str(e)}
        
    def deposit(self, user_name: str, card: str, pin: str, atm_name: str, amount: float):
        result = self.authenticate_transaction(user_name, atm_name, amount)

        if not result.get("success"):
            return result

        user_data: dict = result.get("user")
        atm_data: dict = result.get("atm")

        if user_data.get("bank_name") != atm_data.get("bank_name"):
            return {"success": False, "message": "\nDeposit allowed only in Your Bank's ATM."}

        try:
            user_model = User(user_name, user_data.get("bank_name"), atm_name, self.db)
            deposit_result = user_model.deposit(card, amount)

            if not deposit_result.get("success"):
                return deposit_result

            new_count = user_data.get("day_transaction_count") + 1

            self.db.cursor.execute("UPDATE users SET day_transaction_count=%s WHERE user_name=%s", (new_count, user_name))
            self.db.connection.commit()

            self.transaction_count += 1

            return deposit_result
        except Exception as e:
            return {"success": False, "message": str(e)}

    def withdraw(self, user_name: str, card: str, pin: str, atm_name: str, amount: float):
        result: dict = self.authenticate_transaction(user_name, atm_name, amount)

        if not result.get("success"):
            return result

        user_data: dict = result.get("user")
        atm_data: dict = result.get("atm")

        extra_charge = 0
        if user_data.get("bank_name") != atm_data.get("bank_name"):
            extra_charge = amount * 0.05

        total_amount = amount + extra_charge

        try:
            if atm_data.get("atm_balance") < amount:
                return {"success": False, "message": "\nATM has Insufficient Cash!"}

            user_model = User(user_name, user_data.get("bank_name"), atm_name, self.db)

            withdraw_result = user_model.withdraw(card, total_amount)

            if not withdraw_result.get("success"):
                return withdraw_result

            new_count = user_data.get("day_transaction_count") + 1

            self.db.cursor.execute("UPDATE users SET day_transaction_count=%s WHERE user_name=%s", (new_count, user_name))
            self.db.connection.commit()

            self.transaction_count += 1

            if extra_charge > 0:
                result: str = withdraw_result.get("message")
                result += f"\nExtra Charge (5%): {extra_charge}"
                return result
            return withdraw_result
        except Exception as e:
            return {"success": False, "message": str(e)}
   
    @staticmethod
    def display_details(user_name):
        return User.display_details(user_name)
    
    @staticmethod
    def update_pin(card, new_pin):
        return User.update_pin(card, new_pin)    