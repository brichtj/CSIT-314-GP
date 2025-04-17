import psycopg2
from config import DATABASE

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


def get_db_connection():
    return psycopg2.connect(
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port'],
        database=DATABASE['database']
    )
