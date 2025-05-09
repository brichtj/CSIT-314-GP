from typing import Self
from Classes.LoginResponse import LoginResponse
from Database import DB
import bcrypt
from utils.utils import log_exception


class User():
    # Password =  input_Password
    def __init__(self, user_id,username=None, email=None, phone=None,is_active=True,userProfileID=None,Address=None,Experience=None):
        self.UserID = user_id
        self.Username = username
        self.Email = email
        self.Phone = phone
        self.IsActive = is_active
        self.UserProfile = userProfileID
        self.Address = Address
        self.Experience = Experience
        self.db = DB()

    #to json method
    def to_json(self):
        print(self.Experience)
        return {
            "UserID": self.UserID,
            "Username": self.Username,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive,
            "UserProfile": self.UserProfile,
            "Address": self.Address,
            "Experience": float(self.Experience) if self.Experience is not None else self.Experience
        }

    def login(self):
        try:
            self.pullDetails()
            if not hasattr(self, 'UserID') or self.UserID is None:
                return LoginResponse(False, "User does not exist", None)
            if not self.IsActive:
                return LoginResponse(False, "User suspended", None)
            if not self.checkPassword():
                return LoginResponse(False, "Password false", None)

            if self.UserProfile == "Cleaner":
                pass
                #self.pullExperience()
            if self.UserProfile == "HomeOwner":
                self.pullAddress()

            return LoginResponse(True, "welcome", self.to_dict())

        except Exception as e:
            log_exception(e)
            raise (e)
  #req 1.1 create
    @staticmethod
    def createUser(username:str,email:str,phone:str,experience:float,address:str,UserprofileID:int)->bool:
        try:
            hashed_password = bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt())
            #insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive","Address","Experience") values (%s, %s, %s,%s,%s,true,%s,%s) RETURNING "UserID"
                """
            params = (username,UserprofileID,email,phone,hashed_password,address,experience,)
            result =DB().execute_update(Userstatement, params)
            id = result[0]#SQL statement returns a userID, which is the first argument in a tuple returned by psycopg2
            #insert into cleaner table
            
            return True


        except Exception as e:
            log_exception(e)
            raise e
    #req 1.1 view
    @staticmethod
    def viewUser(UserID:int)->Self:
        try:
            query = """
                        SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive", "Address", "Experience"
                        FROM "user"
                        WHERE "UserID" = %s
                    """
            params = (UserID,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = DB().execute_fetchone(query, params)
            #create json object based on query results
           

            if result is not None:
                user = User(result[0],result[1],result[3],result[4],result[5],result[2],result[6],result[7])
                return user
            else:               
                return None
        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.1 suspend
    @staticmethod
    def suspendUser(UserID:int)->bool:
        try:
            query = """
                        UPDATE "user"
                        SET "IsActive" = false
                        WHERE "UserID" = %s
                    """
            params = (UserID,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = DB().execute_update(query, params)
            #create json object based on query results
            print(result)

            if result:
                return True
            else:               
                return False
        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.1 search
    @staticmethod
    def searchByUserName( searchTerm)->list[Self]:#overwrite User.searchByUserID 
        try:

            query = """
                SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive"
                FROM "user"
                WHERE "Username" ILIKE %s 
            """

            params = (f"{searchTerm}%",)
            #print("Full SQL:", query % params)
            result = DB().execute_fetchall(query, params)
            print(result)
            if len(result) == 0:
                return []
            else:
                return [User(row['UserID'],row['Username'],row['Email'],row['Phone'],row['IsActive'],row['UserProfileID'],row['IsActive'])for row in result]

        except Exception as e:
            log_exception(e)
            raise (e)
    # put into homeowner class
    # def pullAddress(self):
    #     query = """
    #             SELECT "Address"
    #             FROM "HomeOwner"
    #             WHERE "HomeOwnerID" = %s
    #             """
    #     params = (self.UserID,)

    #     result = self.db.execute_fetchone(query, params)

    #     if result:
    #         self.Address = result[0]
    #         print(f'{self.Username}: Address pulled')
    #     else:
    #         print(f'{self.Username}: Failed to pull Address')
    """
    def checkPassword(self) -> bool:
        input_password_bytes = self.input_Password.encode('utf-8')
        hash_password_bytes = self.Password.encode('utf-8')

        print(f"{self.Username}: Authenticating")
        return bcrypt.checkpw(input_password_bytes, hash_password_bytes)
    """

    def checkPassword(self) -> bool:
        input_password_bytes = self.input_Password.encode('utf-8')
        hash_password_bytes = self.Password.encode('utf-8')

        is_match = bcrypt.checkpw(input_password_bytes, hash_password_bytes)
        print(f"{self.Username}: Password match = {is_match}")
        return is_match
    """
    def to_dict(self) -> dict:
        dict = {
            "UserID": self.UserID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone
        }
    """
    def to_dict(self) -> dict:
        return {
            "id": self.UserID,
            "name": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone
        }

