from model.database import DatabaseConnection

class Bank:
    '''This model manages bank details'''
    
    INSERT_BANK = "INSERT INTO banks (bank_name, bank_balance) VALUES (%s, %s)"
    UPDATE_BANK = "UPDATE banks SET bank_balance = %s WHERE bank_name = %s"
    DELETE_BANK = "DELETE FROM banks WHERE bank_name = %s"
    GET_BANK = "SELECT * FROM banks WHERE bank_name = %s"

    def __init__(self, bank_name: str, bank_balance: float, db_instance: DatabaseConnection):
        '''constructor to initialize bank details'''
        
        self.bank_name = bank_name
        self.bank_balance = bank_balance
        self.db = db_instance

    def insert(self):
        try:
            bank_exists = self.exists(self.bank_name)

            if bank_exists.get("success"):
                return bank_exists
            
            self.db.cursor.execute(Bank.INSERT_BANK, (self.bank_name, self.bank_balance))
            self.db.connection.commit()
            
            return {"success": True, "message": "\nBank created Successfully."}
        except Exception as e:
            return {"success": False, "message": e}

    def update_bank_balance(self, bank_name, new_balance):
        try:
            bank_exists = self.exists(bank_name)

            if not bank_exists.get("success"):
                return bank_exists
            
            self.db.cursor.execute(Bank.UPDATE_BANK, (new_balance, bank_name))
            self.db.connection.commit()
            
            return {"success": True, "message": "\nBank balance updated Successfully."}
        except Exception as e:
            return {"success": False, "message": e}

    def delete(self, bank_name):
        try:
            bank_exists = self.exists(bank_name)

            if not bank_exists.get("success"):
                return bank_exists
            
            self.db.cursor.execute(Bank.DELETE_BANK, (bank_name,))
            self.db.connection.commit()
            
            return {"success": True, "message": "\nBank deleted Successfully."}
        except Exception as e:
            return {"success": False, "message": e}
        
    def exists(self, bank_name):
        try:
            self.db.cursor.execute(Bank.GET_BANK, (bank_name,))
            bank = self.db.cursor.fetchone()

            if bank:
                return {"success": True, "message": "\nBank already exists."}
            
            return {"success": False, "message": "\nBank not Found!"}
        except Exception as e:
            return {"success": False, "message": e}