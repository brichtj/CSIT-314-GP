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

    #insert bulk for batch insert rows to a SINGLE table
    # Example insert_bulk
# columns = ['name', 'email']
# values_list = [
#     ['John Doe', 'john.doe@example.com'],
#     ['Jane Smith', 'jane.smith@example.com'],
#     ['Alice Johnson', 'alice.johnson@example.com']
# ]
    def insert_bulk(self, table, columns, values_list) -> bool:
        """
        Insert multiple rows of data into the specified table.

        :param table: The table to insert data into.
        :param columns: List of column names.
        :param values_list: List of objects (rows) where each object is a list of values for each row.
        :return: True if the insert is successful, False otherwise.
        """
        try:
            # Create the query dynamically using columns
            query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

            # Execute the query for each set of values
            self.cur.executemany(query, values_list)

            # Commit the transaction if insertion is successful
            self.conn.commit()

            print(f"Successfully inserted {len(values_list)} rows.")
            return True
        except Exception as e:
            # Rollback in case of an error
            self.conn.rollback()
            print(f"Error inserting data: {e}")
            return False
        
    #insert single row to a SINGLE table
    def insert(self, table, columns, values) -> bool:
        """
        Insert data into the specified table.

        :param table: The table to insert data into.
        :param columns: List of column names.
        :param values: List of values corresponding to the columns.
        :return: True if the insert is successful, False otherwise.
        """
        try:
            # Create the query dynamically using columns and values
            query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
            self.cur.execute(query, values)

            # Commit the transaction if insertion is successful
            self.conn.commit()

            print("Insert successful")
            return True
        except Exception as e:
            # Rollback in case of an error
            self.conn.rollback()
            print(f"Error inserting data: {e}")
            return False
