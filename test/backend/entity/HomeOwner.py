from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
from entity.User import User
import bcrypt

class HomeOwner(User):
    def __init__(self, username=None, email=None, phone=None, address=None, is_active=True, input_password=None):
        super().__init__(username, input_password, email, phone, "HomeOwner", is_active)
        self.Address = address
        self.db = DB()


    def pullAddress(self):
        try:
            query = """
                SELECT "Address"
                FROM "HomeOwner"
                WHERE "HomeOwnerID" = %s
            """
            params = (self.UserID,)
            result = self.db.execute_fetchone(query, params)

            if result:
                self.Address = result[0]
                print(f"{self.Username}: Address pulled")
            else:
                print(f"{self.Username}: Failed to pull Address")
        except Exception as e:
            log_exception(e)
            raise

    def create_account(self):
        try:
            hashed_password = bcrypt.hashpw(self.input_Password.encode(), bcrypt.gensalt()).decode()

            user_query = """
                INSERT INTO "user" ("Username", "Password", "Email", "Phone", "UserProfileID", "IsActive")
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING "UserID"
            """
            user_params = (
                self.Username,
                hashed_password,
                self.Email,
                self.Phone,
                "HomeOwner",
                self.IsActive
            )

            print("Attempting to insert user:", self.Username)
            user_result = self.db.execute_update(user_query, user_params)
            print("Result from DB:", user_result)

            if user_result:
                user_id = user_result[0]
                print(f"{self.Username}: User created with ID {user_id}")

                homeowner_query = """
                    INSERT INTO "HomeOwner" ("HomeOwnerID", "Address")
                    VALUES (%s, %s)
                """
                homeowner_params = (user_id, self.Address)
                self.db.execute_update(homeowner_query, homeowner_params)
                return Response(True, "User created", data=user_result).__dict__

                #return Response(True, "Homeowner account created").to_json()
            else:
                return Response(False, "Failed to create user").to_json()

        except Exception as e:
            log_exception(e)
            return Response(False, "Internal server error").to_json()
