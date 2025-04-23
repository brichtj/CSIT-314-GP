from Classes.LoginResponse import LoginResponse
from Database import DB
import bcrypt
from utils.utils import log_exception


class User:
    # Password =  input_Password
    def __init__(self, username=None, input_password=None, email=None, phone=None, user_profile=None, is_active=True,homeOwnerAddress = None, CleanerExperience = None, db=None):
        self.UserID = None
        self.Username = username
        self.Email = email
        self.Phone = phone
        self.Password = None # Will store hashed password for comparison
        self.UserProfile = user_profile
        self.IsActive = is_active
        self.input_Password = input_password # Plain text for login/creation hashing
        self.db = db or DB()

    def login(self):
        try:
            self.pullDetails()
            if not hasattr(self, 'UserID') or self.UserID is None:
                return LoginResponse(False, "User does not exist", None)
            if self.IsActive == False:
                return LoginResponse(False, "User suspended", None)
            if not self.checkPassword():
                return LoginResponse(False, "Password false", None)
            return LoginResponse(True, "welcome", self.to_dict())

        except Exception as e:
            log_exception(e)
            raise(e)
        

    def pullDetails(self):
        query = """
                    SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "Password", "IsActive"
                    FROM "user"
                    WHERE "Username" = %s
                """
        params = (self.Username,)
        # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
        # print(f"Formatted query: {formatted_query}")

        db = DB()
        result = db.execute_fetchone(query, params)
        if result is not None:
            self.UserID = result[0] or None
            self.Username = result[1] or None
            self.UserProfile = result[2] or None
            self.Email = result[3] or None
            self.Phone = result[4] or None
            self.Password = result[5] or None
            self.IsActive = result[6] or None
            print(f"{self.Email}: Details pulled")
        else:
            print(f'{self.Username}: Failed to pull details')

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