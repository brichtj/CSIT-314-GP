from DatabaseConnection import DB
import bcrypt

db = DB()
conn = db.getConn()
cur = conn.cursor()

cur.execute("""
            SELECT "UserID"
            FROM "user"
            """)

rows = cur.fetchall()

for row in rows:
    password = b"user123"
    hash = bcrypt.hashpw(password,bcrypt.gensalt())
    hash = hash.decode('utf-8')
    cur.execute("""
                UPDATE "user"
                SET "Password" = %s
                WHERE "UserID" = %s
                """,
                (hash, row[0]))
    conn.commit