import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        dbname="csit314db",
        user="rooter",
        password="rooter",
        host="localhost",
        cursor_factory=RealDictCursor
    )
    return conn
