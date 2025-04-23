# db_singleton.py

import psycopg2

DATABASE = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
    'port': '5432',
    'database': 'csit314db'
}


class DB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
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
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def execute_fetchone(self, query, params=()) -> tuple:
        try:
            self.cur.execute(query, params)
            return self.cur.fetchone()
        except Exception as e:
            print(f"Database error: {e}")
            return ()

    def execute_update(self, query, params=()) -> bool:
        try:
            self.cur.execute(query, params)
            if self.cur.rowcount == 1:
                self.conn.commit()
                return True
            elif self.cur.rowcount > 1:
                raise Exception("Update affected more than 1 row. Rolling back.")
            raise Exception("No rows were updated. Rolling back.")
        except Exception as e:
            self.conn.rollback()
            print(f"Database error: {e}")
            return False

    def execute_bulk_update(self, query, params=()) -> int:
        try:
            self.cur.execute(query, params)
            count = self.cur.rowcount
            if count > 0:
                self.conn.commit()
                return count
            raise Exception("No rows were updated. Rolling back.")
        except Exception as e:
            self.conn.rollback()
            print(f"Database error: {e}")
            return 0

    def __del__(self):
        if hasattr(self, 'conn') and self.conn:
            self.cur.close()
            self.conn.close()
