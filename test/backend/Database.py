import psycopg2

DATABASE = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
    'port': '5432',
    'database': 'csit314db'
}

try:
    connection = psycopg2.connect(
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port'],
        database=DATABASE['database']
    )

    connection.set_client_encoding('UTF8')
    cursor = connection.cursor()

    print("Database: Connection established successfully!")
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Database: PostgreSQL version: {db_version}")

except Exception as e:
    print(f"Error connecting to the database: {e}")


class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            user=DATABASE['user'],
            password=DATABASE['password'],
            host=DATABASE['host'],
            port=DATABASE['port'],
            database=DATABASE['database']
        )
        self.cur = self.conn.cursor()

    def execute_fetchone(self, query, params) -> tuple:
        try:
            self.cur.execute(query, params)
            row = self.cur.fetchone()
            return row
        except Exception as e:
            print(f"Database error: {e}")
            return ()

    def execute_update(self, query, params) -> bool:
        try:
            self.cur.execute(query, params)

            if self.cur.rowcount == 1:
                self.conn.commit()
                print(f'Database: Data updated')
                return True

            if self.cur.rowcount > 1:
                raise Exception(
                    "Update affected more than 1 row. Rolling back.")

            raise Exception("No rows were updated. Rolling back.")

        except Exception as e:
            self.conn.rollback()
            print(f"Database error: {e}")
            return False

    def execute_bulk_update(self, query, params) -> int:
        try:
            self.cur.execute(query, params)

            count = self.cur.rowcount

            if count > 0:
                self.conn.commit()
                print(f'Database: Data updated')
                return count

            raise Exception("No rows were updated. Rolling back.")

        except Exception as e:
            self.conn.rollback()
            print(f"Database error: {e}")
            return 0

    def __del__(self):
        self.conn.close()
