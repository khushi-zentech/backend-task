import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseConnection:
    '''This model manages database connection'''

    def __init__(self):
        '''constructor to initialize database connection'''
        
        try:
            self.connection = psycopg2.connect(
                dbname="atm_system",
                user="postgres",
                password="LJIET",
                host="localhost",
                port="5432"
            )
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        except psycopg2.Error as e:
            raise Exception(f"Database connection Failed: {e}")

    def close_connection(self):
        try:
            self.cursor.close()
            self.connection.close()

            return {
                "success": True,
                "message": "\nDatabase connection closed Successfully."
            }
        except Exception as e:
            return {"success": False, "message": str(e)}