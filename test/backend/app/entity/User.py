from app.db import get_db_connection


# User:
# int        UserID
# varchar    Username
# int        UserProfile
# varchar    Email
# number     Phone
# varchar    Password
# bool       IsActive


class User:
    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password

    @staticmethod
    def find_by_email(UserProfile, Email):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT "Email", "Password"
                    FROM "User"
                    WHERE "UserProfile" = %s
                    AND "Email" = %s
                    """,
                    (UserProfile, Email,))
        row = cur.fetchone()
        conn.close()
        if row:
            return User(row[0], row[1])
        return None

    def pullDetails(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT "UserID", "Username", "UserProfile", "Email", "Phone", "IsActive"
                    FROM "User"
                    WHERE "Email" = %s""",
                    (self.Email,)
                    )
        row = cur.fetchone()
        conn.close()

        if row:
            self.UserID = row[0]
            self.Username = row[1]
            self.UserProfile = row[2]
            self.Email = row[3]
            self.Phone = row[4]
            self.IsActive = row[5]
            print(f"Details pulled: {self.Email}")
        else:
            print(f"Failed to pull details: {self.Email}")

    def to_dict(self):
        return {
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive
        }
