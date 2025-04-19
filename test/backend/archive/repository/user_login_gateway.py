class UserLoginGateway:
    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def authenticate(self, UserProfile, Email, Password):
        try:
            self.cursor.execute("""
                                SELECT "UserProfile", "Email"
                                FROM "User"
                                WHERE "Email" = %s
                                AND "Password" = %s""",
                                (Email, Password)
                                )
            row = self.cursor.fetchone()
            if row:
               return row
            return None
        except Exception as e:
            print(f"Database error: {e}")
            return None
