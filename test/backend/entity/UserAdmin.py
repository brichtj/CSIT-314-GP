import bcrypt
from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
import psycopg2
#make cleaner class, inherits from user.py
class UserAdmin():
    def __init__(self):
        self.db = DB()
    
    def createUser(self,username,email,phone,experience,address,userType):
        try:
            hashed_password = bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt())
            #insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive") values (%s, %s, %s,%s,%s,true) RETURNING "UserID"
                """
            params = (username,userType,email,phone,hashed_password,)
            result =self.db.execute_update(Userstatement, params)
            id = result[0]#SQL statement returns a userID, which is the first argument in a tuple returned by psycopg2
            #insert into cleaner table
        
            #swithch case based on userType to change userstatement
            if userType == "Cleaner":
                Userstatement = """
                    Insert into "Cleaner" ("CleanerID","Experience") values (%s, %s)
                    """
                params = (id, experience)
            elif userType == "HomeOwner":
                Userstatement = """
                    Insert into "HomeOwner" ("HomeOwnerID","Address") values (%s, %s)
                    """
                params = (id, address)
            elif userType == "UserAdmin":
                Userstatement = """
                    Insert into "UserAdmin" ("AdminID") values (%s)
                    """
                params = (id,)
            elif userType == "PlatformManagement":
                Userstatement = """
                    Insert into "PlatformManagement" ("ManagerID") values (%s)
                    """
                params = (id,)
            else:
                raise ValueError("Invalid user type")

            result =self.db.execute_update(Userstatement, params)
            
            return True


        except Exception as e:
            log_exception(e)
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
