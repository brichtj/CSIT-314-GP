from Classes.LoginResponse import LoginResponse
from Database import DB
import bcrypt


class User:
    # Password =  input_Password
    def __init__(self, Username, Password):
        # attributes in database
        self.UserID = None
        self.Username = Username
        self.UserProfile = None
        self.Email = None
        self.Phone = None
        self.Password = None
        self.IsActive = None
        self.Experience = None
        self.Address = None

        self.input_Password = Password

    def login(self):
        try:
            self.pullDetails()

            if not self.UserID:
                return LoginResponse(False, "User does not exist", None)
            if not self.IsActive:
                return LoginResponse(False, "User suspended", None)
            if not self.checkPassword():
                return LoginResponse(False, "Incorrect Password", None)

            if self.UserProfile == "Cleaner":
                self.pullExperience()
            if self.UserProfile == "HomeOwner":
                self.pullAddress()

            return LoginResponse(True, "welcome", self.to_dict())

        except Exception as e:
            print(f'{self.Username}: {str(e)}')
            return LoginResponse(False, "Technical error", None)

    def pullDetails(self):
        query = """
                    SELECT "UserID", "Username", "UserProfile", "Email", "Phone", "Password", "IsActive"
                    FROM "User"
                    WHERE "Username" = %s"""
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
            print(f"{self.Username}: Details pulled")
        else:
            print(f'{self.Username}: Failed to pull details')

    def checkPassword(self) -> bool:
        input_password_bytes = self.input_Password.encode('utf-8')
        hash_password_bytes = self.Password.encode('utf-8')

        print(f"{self.Username}: Authenticating")
        return bcrypt.checkpw(input_password_bytes, hash_password_bytes)

    def pullExperience(self):
        query = """
                SELECT "Experience"
                FROM "Cleaner"
                WHERE "CleanerID" = %s
                """
        params = (self.UserID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.Experience = result[0]
            print(f'{self.Username}: Experience pulled')
        else:
            print(f'{self.Username}: Failed to pull Experience')

    def pullAddress(self):
        query = """
                SELECT "Address"
                FROM "HomeOwner"
                WHERE "HomeOwnerID" = %s
                """
        params = (self.UserID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.Experience = result[0]
            print(f'{self.Username}: Address pulled')
        else:
            print(f'{self.Username}: Failed to pull Address')

    def to_dict(self) -> dict:
        dict = {
            "UserID": self.UserID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone
        }

        if self.Address:
            dict.update({'Address': self.Address})

        if self.Experience:
            dict.update({'Experience': self.Experience})

        return dict
