from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
from entity.User import User
import bcrypt
import psycopg2
#make cleaner class, inherits from user.py
class Cleaner(User):
    def __init__(self, username=None, email=None, phone=None, is_active=True, Experience=None, input_password=None):
        super().__init__(username, None, email, phone, "Cleaner", is_active)
        self.Experience = Experience
        self.input_Password = input_password 
        self.db = DB()

    
    def createUser(self):
        try:

            #insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive") values (%s, 'Cleaner', %s,%s,'123',true) RETURNING "UserID"
                """
            params = (self.Username,self.Email,self.Phone,)
            result =self.db.execute_update(Userstatement, params)
            id = result[0]#SQL statement returns a userID, which is the first argument in a tuple returned by psycopg2
            #insert into cleaner table
            Userstatement = """
                Insert into "Cleaner" ("CleanerID","Experience") values (%s, %s)
                """
            params = (id,self.Experience)
            result =self.db.execute_update(Userstatement, params)
            
            return True


        except Exception as e:
            raise e
        
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
                "Cleaner",
                self.IsActive
            )

            user_result = self.db.execute_update(user_query, user_params)

            if user_result:
                user_id = user_result[0]
                print(f"{self.Username}: User created with ID {user_id}")

                cleaner_query = """
                    INSERT INTO "Cleaner" ("CleanerID", "Experience")
                    VALUES (%s, %s)
                """
                cleaner_params = (user_id, self.Experience)
                self.db.execute_update(cleaner_query, cleaner_params)

                return Response(True, "Cleaner account created").to_json()
            else:
                return Response(False, "Failed to create user").to_json()

        except Exception as e:
            log_exception(e)
            return Response(False, "Internal server error").to_json()



    def pullExperience(self):
        query = """
                SELECT "Experience"
                FROM "Cleaner"
                WHERE "CleanerID" = %s
                """
        params = (self.UserID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            self.Experience = result[0]
            print(f'{self.Username}: Experience pulled')
        else:
            print(f'{self.Username}: Failed to pull Experience')
