

DATABASE = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
    'port': '5432',
    'database': 'csit314db'
}

import psycopg2
import bcrypt

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


conn = psycopg2.connect(
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port'],
        database=DATABASE['database']
    )
cur = conn.cursor()

cur.execute("""
            SELECT "UserID"
            FROM "User"
            """)

rows = cur.fetchall()

for row in rows:
    password = b"user123"
    hash = bcrypt.hashpw(password,bcrypt.gensalt())
    hash = hash.decode('utf-8')
    cur.execute("""
                UPDATE "User"
                SET "Password" = %s
                WHERE "UserID" = %s
                """,
                (hash, row[0]))
    
conn.commit()
cur.close()
conn.close()