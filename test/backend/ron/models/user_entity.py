class UserEntity:
    def __init__(self, conn):
        self.conn = conn

    def get_user_by_username(self, username: str):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM \"user\" WHERE Username = %s", (username,))
            return cur.fetchone()
