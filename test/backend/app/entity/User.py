from app.db import DB
import bcrypt


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
        query = """
            SELECT "Email", "Password"
            FROM "User"
            WHERE "UserProfile" = %s
            AND "Email" = %s"""

        params = (UserProfile, Email,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"{Email}: User found")
            return User(result[0], result[1])

        print(f"{Email}: User not found")
        raise Exception('User not found')

    def check_password(self, input_password) -> bool:
        input_password_bytes = input_password.encode('utf-8')
        hash_password_bytes = self.Password.encode('utf-8')
        print(f"{self.Email}: Authenticating")
        return bcrypt.checkpw(input_password_bytes, hash_password_bytes)

    def pullDetails(self):
        query = """
                SELECT "UserID", "Username", "UserProfile", "Email", "Phone", "IsActive"
                FROM "User"
                WHERE "Email" = %s"""
        params = (self.Email,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.UserID = result[0]
            self.Username = result[1]
            self.UserProfile = result[2]
            self.Email = result[3]
            self.Phone = result[4]
            self.IsActive = result[5]
            print(f"{self.Email}: Details pulled")
            return

        print(f"{self.Email}: Failed to pull details")
        raise Exception("Failed to pull details")

    def to_dict(self) -> dict:
        return {
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive
        }

    def getIsActive(self) -> bool:
        return self.IsActive
