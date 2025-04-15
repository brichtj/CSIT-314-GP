class UserGateway:
    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def getAddress(self, userid):
        try:
            self.cursor.execute("""
                                SELECT *
                                FROM "homeowner"
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
