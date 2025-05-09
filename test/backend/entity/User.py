from Classes.LoginResponse import LoginResponse
from Database import DB
import bcrypt
from utils.utils import log_exception


class User():
    # Password =  input_Password
    def __init__(self):
        self.db = DB()

    def login(self, Username, input_Password):
        try:
            query = """
                    SELECT "Password"
                    FROM "user"
                    WHERE "Username" = %s
                    """
            params = (Username,)
            result = self.db.execute_fetchone(query, params)

            if not self.checkPassword(input_Password, result[0]):
               return LoginResponse(False, "Password false", None)
                        
            query = """
                    SELECT "IsActive"
                    FROM "user"
                    WHERE "Username" = %s
                    """
            params = (Username,)
            result = self.db.execute_fetchone(query, params)

            if not result[0]:
                return LoginResponse(False, "User suspended", None)
            
            query = """
                    SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "Password"
                    FROM "user"
                    WHERE "Username" = %s
                    """
            params = (Username,)
            result = self.db.execute_fetchall(query, params)

            return LoginResponse(True, "welcome", result)

        except Exception as e:
            log_exception(e)
            raise (e)
        
    def checkPassword(self, input_Password, Password) -> bool:
        input_password_bytes = input_Password.encode('utf-8')
        hash_password_bytes = Password.encode('utf-8')

        is_match = bcrypt.checkpw(input_password_bytes, Password)
        print(f"{self.Username}: Password match = {is_match}")
        return is_match
    
    def searchByUserID(self, searchTerm):
        try:
            query = """
                SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive"
                FROM "user"
                WHERE "Username" ILIKE %s AND ("UserProfileID" =1 OR "UserProfileID" =2 )
            """

            params = (f"{searchTerm}%",)
            print("Full SQL:", query % params)
            result = self.db.execute_fetchall(query, params)
            print(result)
            return result

        except Exception as e:
            log_exception(e)
            raise (e)