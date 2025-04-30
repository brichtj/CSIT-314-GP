from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
from entity.User import User
import psycopg2
#make cleaner class, inherits from user.py
class Cleaner(User):
    def __init__(self,  username=None, email=None, phone=None,  is_active=True,Experience = None):
        super().__init__(username, None, email, phone, "Cleaner", is_active)   
        self.Experience = Experience
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
