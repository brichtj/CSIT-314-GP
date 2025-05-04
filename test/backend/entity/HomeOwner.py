
import bcrypt
from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
from entity.User import User
#make cleaner class, inherits from user.py
class HomeOwner(User):
    def __init__(self,  username=None, email=None, phone=None,Address = None,  is_active=True):
        super().__init__(username, None, email, phone, "HomeOwner", is_active)   
        self.Address = Address
        self.db = DB()
    
    def createUser(self):
        try:
            hashed_password = bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt())
            #insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive") values (%s, 'Cleaner', %s,%s,%s,true) RETURNING "UserID"
                """
            params = (self.Username,self.Email,self.Phone,hashed_password,)
            result =self.db.execute_update(Userstatement, params)
            id = result[0]#SQL statement returns a userID, which is the first argument in a tuple returned by psycopg2
            #insert into cleaner table
            Userstatement = """
                Insert into "HomeOwner" ("HomeOwnerID","Address") values (%s, %s)
                """
            params = (id,self.Address)
            result =self.db.execute_update(Userstatement, params)
            
            return True


        except Exception as e:
            log_exception(e)
            raise e

