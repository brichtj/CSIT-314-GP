from Classes.LoginResponse import LoginResponse
from Database import DB
import bcrypt


class User:
    # Password =  input_Password
    def __init__(self, Username, Password):
        self.Username = Username
        self.input_Password = Password

    def login(self):
        try:
            self.pullDetails()
            passwordCorrect = self.checkPassword()
            if self.UserID is None:
                return LoginResponse(False, "User does not exist", None)
            if self.IsActive == False:
                return LoginResponse(False, "User suspended", None)
            if not self.checkPassword():
                return LoginResponse(False, "Password false", None)
            return LoginResponse(True, "welcome", self.to_dict())

        except Exception as e:
            return LoginResponse(False, "Technical error", None)
            pass

    def pullDetails(self):
        query = """
                    SELECT "UserID", "Username", "UserProfile", "Email", "Phone", "Password", "IsActive"
                    FROM "User"
                    WHERE "Email" = %s"""
        params = (self.Username,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.UserID = result[0]
            self.Username = result[1]
            self.UserProfile = result[2]
            self.Email = result[3]
            self.Phone = result[4]
            self.Password = result[5]
            self.IsActive = result[6]
            print(f"{self.Email}: Details pulled")
        else:
            print(f'{self.Email}: Failed to pull details')

    def checkPassword(self) -> bool:
        input_password_bytes = self.input_Password.encode('utf-8')
        hash_password_bytes = self.Password.encode('utf-8')

        print(f"{self.Email}: Authenticating")
        return bcrypt.checkpw(input_password_bytes, hash_password_bytes)

    def to_dict(self) -> dict:
        return {
            "UserID": self.UserID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone
        }
