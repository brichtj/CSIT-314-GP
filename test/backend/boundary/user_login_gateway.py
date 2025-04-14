class UserLoginGateway:
    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def authenticate(self, profile, email, password):
        try:
            self.cursor.execute("""
                                SELECT userprofile, email, password
                                FROM login_details
                                WHERE userprofile = %s
                                AND email = %s
                                and password = %s""",
                                (profile, email, password)
                                )
            row = self.cursor.fetchone()
            if row:
                self.cursor.execute("""
                                    SELECT userid, username, userprofile, email, phone, dob
                                    FROM "user"
                                    WHERE userprofile = %s
                                    AND email = %s """,
                                    (profile, email)
                                    )
                row = self.cursor.fetchone()

                return row
            return None
        except Exception as e:
            print(f"Database error: {e}")
            return None

    def getAddress(self, userid):
        try:
            self.cursor.execute("""
                                SELECT userprofile
                                FROM "user"
                                WHERE userid = %s""",
                                (userid,))

            row = self.cursor.fetchone()

            if row:
                self.cursor.execute("""
                                    SELECT address
                                    FROM homeowner
                                    WHERE userid = %s""",
                                    (userid,)
                                    )

                row = self.cursor.fetchone()

                if row:
                    return row

                print("error: No address found for {userid}")
                return None

            print("error: {userid} is not a HomeOwner")
            return None

        except Exception as e:
            print(f"Database error: {e}")
            return None
