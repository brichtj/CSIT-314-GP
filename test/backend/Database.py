# db_singleton.py

import psycopg2
from datetime import datetime

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
            self.conn.autocommit = False
            print("Database: Connection established successfully!")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def execute_fetchone(self, query, params=()) -> tuple:
        try:
            
            self.cur.execute(query, params)
            return self.cur.fetchone()
        except Exception as e:
            print(f"Database error: {e}")
            return (e)
        
    #fetch an array of results
    def execute_fetchall(self, query: str, params) -> list[dict]:
        """
        Returns all results as a list of dictionaries with column names as keys.
        """
        try:
            if self.cur.closed:
                self.cur = self.conn.cursor()
            self.cur.execute(query, params)
            #print(query%params)
            rows = self.cur.fetchall()

            if not rows:
                return None

            colnames = [desc[0] for desc in self.cur.description]

            result = []
            for row in rows:
                row_dict = dict(zip(colnames, row))
                
                for key, value in row_dict.items():
                    if isinstance(value, datetime):
                        row_dict[key] = value.isoformat()
                
                result.append(row_dict)

            return result
        except Exception as e:
            print(f"Database error: {e}")
            return []
        
    def fetch_one_by_key(self, query: str, params) -> dict:
        try:
            if self.cur.closed:
                self.cur = self.conn.cursor()
            self.cur.execute(query, (params,))
            row = self.cur.fetchone()

            if row is None:
                return None

            colnames = [desc[0] for desc in self.cur.description]
            result = dict(zip(colnames, row))

            for key, value in result.items():
                if isinstance(value, datetime):
                    result[key] = value.isoformat()

            return result
        except Exception as e:
            self.cur.close()
            
            print(f"Database error: {e}")
            return None
        
    def execute_update(self, query, params=()) -> bool:
        try:
            if self.cur.closed:
                self.cur = self.conn.cursor()
            self.cur.execute(query, params)
            
            # If the query is returning something, fetch the first row
            if self.cur.description:  # Check if there's a returning column
                self.conn.commit()
                result = self.cur.fetchone()  # Only one row should be returned, note this is a TUPLE depending on what you want returned, e.g (1,"other stuff")
                return result  # You could return the whole row if needed (result[0], etc.)
            elif self.cur.rowcount > 1:
                raise Exception("Update affected more than 1 row. Rolling back.")
            elif self.cur.rowcount == 1:
                self.conn.commit()
                return True
            #in case no updates happened, e.g no rows were updated because username didnt exist, dont have to show error.
            self.conn.rollback()
            return False
        except Exception as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            raise(e)
    #update with error incase no rows returned(e.g the row requested to update does not exist)
    def execute_update_with_error(self, query, params=()) -> bool:
        try:
            if self.cur.closed:
                self.cur = self.conn.cursor()
            self.cur.execute(query, params)
            
            # If the query is returning something, fetch the first row
            if self.cur.description:  # Check if there's a returning column
                self.conn.commit()
                result = self.cur.fetchone()  # Only one row should be returned, note this is a TUPLE depending on what you want returned, e.g (1,"other stuff")
                return result  # You could return the whole row if needed (result[0], etc.)
            elif self.cur.rowcount > 1:
                raise Exception("Update affected more than 1 row. Rolling back.")
            elif self.cur.rowcount == 0:
                raise Exception("Update affected no rows. Rolling back.")
            elif self.cur.rowcount == 1:
                self.conn.commit()
                return True
            return True
        except Exception as e:
            self.conn.rollback()
            #print(f"Database error: {e}")
            raise(e)
            
    def update_two_tables(
            self,
        update1_query, update1_params,
        update2_query, update2_params,
        require_rows=True  # If True, require at least one row to be updated
    ):
        try:
            if self.cur.closed:
                self.cur = self.conn.cursor()
            cur = self.conn.cursor()

            cur.execute(update1_query, update1_params)
            if require_rows and cur.rowcount == 0:
                raise Exception("First update matched no rows.")

            cur.execute(update2_query, update2_params)
            if require_rows and cur.rowcount == 0:
                raise Exception("Second update matched no rows.")

            self.conn.commit()
            return True

        except Exception as e:
            print("Transaction failed:", e)
            if self.conn:
                self.conn.rollback()
            raise e

        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                self.conn.close()

    def execute_delete(self, query, params=()) -> bool:
        try:
            self.cur.execute(query, params)
            deleted = self.cur.rowcount
            if deleted == 0:
                raise psycopg2.DatabaseError("No rows were deleted. Rolling back.")
            else:
                self.conn.commit()
                return True
        except Exception as e:
            self.conn.rollback()
            #print(f"Database error: {e}")
            raise(e)
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

            #print("Insert successful")
            return True
        except Exception as e:
            # Rollback in case of an error
            self.conn.rollback()
            print(f"Error inserting data: {e}")
            return False
        #insert single row to a SINGLE table
    def insertFreeStyle(self, query, values) -> bool:
        try:
            self.cur.execute(query, values)

            # Commit the transaction if insertion is successful
            self.conn.commit()

            #print("Insert successful")
            return True
        except Exception as e:
            # Rollback in case of an error
            self.conn.rollback()
            #print(f"Error inserting data: {e}")
            raise(e)

