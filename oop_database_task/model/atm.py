from model.bank import Bank
from model.database import DatabaseConnection

class ATM:
    '''This model manages ATM details'''

    INSERT_ATM = "INSERT INTO atms (atm_name, bank_name, atm_balance) VALUES (%s, %s, %s)"
    UPDATE_ATM_BALANCE = "UPDATE atms SET atm_balance = %s WHERE atm_name = %s"
    DELETE_ATM = "DELETE FROM atms WHERE atm_name = %s"
    GET_ATM = "SELECT * FROM atms WHERE atm_name = %s"

    def __init__(self, atm_name: str, bank: Bank, atm_balance: float, db_instance: DatabaseConnection):
        '''constructor to initialize ATM details'''

        self.atm_name = atm_name
        self.bank = bank            
        self.atm_balance = atm_balance
        self.db = db_instance

    def insert(self):
        try:
            atm_exists = self.exists(self.atm_name)
            if atm_exists.get("success"):
                return atm_exists

            bank_exist = self.bank.exists(self.bank.bank_name)
            if not bank_exist.get("success"):
                return bank_exist
            
            self.db.cursor.execute(ATM.INSERT_ATM, (self.atm_name, self.bank.bank_name, self.atm_balance))
            self.db.connection.commit()

            return {"success": True, "message": "\nATM created Successfully."}
        except Exception as e:
            return {"success": False, "message": e}

    def update_atm_balance(self, atm_name, new_balance):
        try:
            atm_exists = self.exists(atm_name)
            
            if not atm_exists.get("success"):
                return atm_exists

            self.db.cursor.execute(ATM.UPDATE_ATM_BALANCE, (new_balance, atm_name))
            self.db.connection.commit()

            return {"success": True, "message": "\nATM balance updated Successfully."}
        except Exception as e:
            return {"success": False, "message": e}

    def delete(self, atm_name):
        try:
            atm_exists = self.exists(atm_name)
            
            if not atm_exists.get("success"):
                return atm_exists

            self.db.cursor.execute(ATM.DELETE_ATM, (atm_name,))
            self.db.connection.commit()

            return {"success": True, "message": "\nATM deleted Successfully."}
        except Exception as e:
            return {"success": False, "message": e}

    def exists(self, atm_name):
        try:
            self.db.cursor.execute(ATM.GET_ATM, (atm_name,))
            atm = self.db.cursor.fetchone()

            if atm:
                return {"success": True, "message": "\nATM already exists!"}
            
            return {"success": False, "message": "\nATM not Found!"}
        except Exception as e:
            return {"success": False, "message": e}