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
            print(self.Address)

            #insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive") values (%s, 'Cleaner', %s,%s,'123',true) RETURNING "UserID"
                """
            params = (self.Username,self.Email,self.Phone,)
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
            raise e

