import psycopg2

DATABASE = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
    'port': '5432',
    'database': 'csit314'
}


class DB:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                user=DATABASE['user'],
                password=DATABASE['password'],
                host=DATABASE['host'],
                port=DATABASE['port'],
                database=DATABASE['database']
            )
            self.cur = self.conn.cursor()

            print("Database: Connection established successfully!")
            self.cur.execute("SELECT version();")
            db_version = self.cur.fetchone()
            print(f"Database: PostgreSQL version: {db_version}")

        except Exception as e:
            print(f"Error connecting to the database: {e}")
        
    def getCursor(self):
        return self.cur
    
    def getConn(self):
        return self.conn
    
    def __del__(self):
        if hasattr(self, 'conn') and self.conn:
            self.cur.close()
            self.conn.close()
