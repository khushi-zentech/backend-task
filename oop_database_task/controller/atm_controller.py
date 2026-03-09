from model.bank import Bank
from model.atm import ATM
from model.user import User
from model.database import DatabaseConnection

class ATMController:
    '''This controller manages ATM system operations'''

    def __init__(self, db_instance: DatabaseConnection):
        self.db = db_instance

    def insert_bank(self, bank_name):
        try:
            bank = Bank(bank_name, 0.0, self.db)
            return bank.insert()
        except Exception as e:
            return {"success": False, "message": str(e)}

    def insert_atm(self, atm_name, bank_name):
        try:
            bank = Bank(bank_name, 0.0, self.db)

            atm = ATM(atm_name, bank, 500000, self.db)

            return atm.insert()
        except Exception as e:
            return {"success": False, "message": str(e)}

    def insert_user(self, user_name, bank_name, atm_name):
        try:
            user = User(user_name, bank_name, atm_name, self.db)
            return user.insert()
        except Exception as e:
            return {"success": False, "message": str(e)}