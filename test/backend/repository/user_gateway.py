class UserGateway:
    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def getUserDetail(self, UserProfile, Email):
        try:
            if UserProfile == "UserAdmin":
                self.cursor.execute("""
                                    SELECT U."UserID", U."Username", U."UserProfile", U."Email", U."Phone", U."IsActive"
                                    FROM "User" U
                                    INNER JOIN "UserAdmin" UA
                                    ON U."UserID" = UA."AdminID"
                                    WHERE U."Email" = %s""",
                                    (Email,)
                                    )

                row = self.cursor.fetchone()
                return row

            if UserProfile == "Cleaner":
                self.cursor.execute("""
                                    SELECT U."UserID", U."Username", U."UserProfile", U."Email", U."Phone", U."IsActive", C."Experience"
                                    FROM "User" U
                                    INNER JOIN "Cleaner" C
                                    ON U."UserID" = C."CleanerID"
                                    WHERE U."Email" = %s""",
                                    (Email,)
                                    )

                row = self.cursor.fetchone()
                return row

            if UserProfile == "HomeOwner":
                self.cursor.execute("""
                                    SELECT U."UserID", U."Username", U."UserProfile", U."Email", U."Phone", U."IsActive", HO."Address"
                                    FROM "User" U
                                    INNER JOIN "HomeOwner" HO
                                    ON U."UserID" = HO."HomeOwnerID"
                                    WHERE U."Email" = %s""",
                                    (Email,)
                                    )

                row = self.cursor.fetchone()
                return row

            if UserProfile == "PlatformManagement":
                self.cursor.execute("""
                                    SELECT U."UserID", U."Username", U."UserProfile", U."Email", U."Phone", U."IsActive"
                                    FROM "User" U
                                    INNER JOIN "PlatformManagement" PM
                                    ON U."UserID" = PM."ManagerID"
                                    WHERE U."Email" = %s""",
                                    (Email,)
                                    )

                row = self.cursor.fetchone()
                return row

        except Exception as e:
            print(f"Database error: {e}")
            return None

    def userProfileInit(self, UserID, UserProfile):
        try:
            if UserProfile == "Cleaner":
                self.cursor.execute("""
                                    SELECT "Experience"
                                    FROM "Cleaner"
                                    WHERE "CleanerID" = %s""",
                                    (UserID,))

                row = self.cursor.fetchone()

                if row:
                    print("Cleaner Experience found")
                    return row

                print("error: No Experience found for {UserID}")
                return None

            if UserProfile == "HomeOwner":
                self.cursor.execute("""
                                    SELECT "Address"
                                    FROM "HomeOwner"
                                    WHERE "HomeOwnerID" = %s""",
                                    (UserID,))

                row = self.cursor.fetchone()

                if row:
                    print("HomeOwner Address found")
                    return row

                print("error: No Address found for {UserID}")
                return None

            print(
                "No extra details needed for UserAdmin and PlatformManagement currently")
            return None
        except Exception as e:
            print(f"Database error: {e}")
            return None
