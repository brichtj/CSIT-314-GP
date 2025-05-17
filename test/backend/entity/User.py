from typing import Self
from Classes.LoginResponse import LoginResponse
from .UserProfile import UserProfile
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
        self.UserProfileID = userProfileID
        self.Address = Address
        self.Experience = Experience

    #to json method
    def to_json(self):
        return {
            "UserID": self.UserID,
            "Username": self.Username,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive,
            "UserProfile": self.UserProfileID,
            "Address": self.Address,
            "Experience": float(self.Experience) if self.Experience is not None else self.Experience,
        }
    @staticmethod
    def login(username:str,password:str)->LoginResponse:
        try:
            query = """
                SELECT "UserID", "Username",  "Email", "Phone", "IsActive","user"."UserProfileID", "Address", "Experience","Password"
                ,"Name","Privilege","Is_Active" as "UPActive"
                FROM "user"
                Left join "UserProfile" on "UserProfile"."UserProfileID" = "user"."UserProfileID"    
                            
                WHERE "Username" = %s
            """
            params = (username,)
            result = DB().fetch_one_by_key(query, params)
            if result is None:
                return LoginResponse(False, "User does not exist", None)
            input_password_bytes = password.encode('utf-8')
            hash_password_bytes = result["Password"].encode('utf-8')
            if not bcrypt.checkpw(input_password_bytes, hash_password_bytes):
                return LoginResponse(False, "Password false", None)
            elif result["IsActive"] == False:
                return LoginResponse(False, "User suspended", None)
            elif result["UPActive"] == False:   
                return LoginResponse(False, "User profile suspended", None)
            else:
                #userProfile = UserProfile(result["UserProfileID"],result["Name"],result["Privilege"],result["IsActive"])
                #user = User(,userProfile)
                use = CustomUser(result["UserID"],result["Username"],result["Email"],result["Phone"],result["IsActive"],result["UserProfileID"],result["Address"],result["Experience"],result["Name"],result["Privilege"],result["IsActive"])
                return LoginResponse(True, "welcome", use)

        except Exception as e:
            log_exception(e)
            raise (e)
  #req 1.1 create
    @staticmethod
    def createUser(username:str,email:str,phone:str,experience:float,address:str,UserprofileID:int)->bool:
        try:
            hashed_password = bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
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
                        
                SELECT "UserID", "Username",  "Email", "Phone", "IsActive","user"."UserProfileID", "Address", "Experience","Password"
                ,"Name","Privilege","IsActive"
                FROM "user"
                Left join "UserProfile" on "UserProfile"."UserProfileID" = "user"."UserProfileID"    
                        WHERE "UserID" = %s
                           
                    """
            params = (UserID,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = DB().fetch_one_by_key(query, params)
            #create json object based on query results
           

            if result is not None:     
                userProfile = UserProfile(result["UserProfileID"],result["Name"],result["Privilege"],result["IsActive"])
                user = User(result["UserID"],result["Username"],result["Email"],result["Phone"],result["IsActive"],result["UserProfileID"],result["Address"],result["Experience"],userProfile)
           
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
            if result is None or len(result) == 0:
                return []
            else:
                return [User(row['UserID'],row['Username'],row['Email'],row['Phone'],row['IsActive'],row['UserProfileID'],row['IsActive'])for row in result]

        except Exception as e:
            log_exception(e)
            raise (e)
        
    #req 1.1 update User 
    def updateUser(username:str,email:str,phone:str,IsActive:bool,UserProfileID:int,address:str,experience:float,UserID:int)->bool:#overwrite User.searchByUserID 
        try:

            query = """
                UPDATE "user"
                SET
                    "Username" = %s,
                    "Email" = %s,
                    "Phone" = %s,
                    "IsActive" = %s,
                    "UserProfileID" = %s,
                    "Address" = %s,
                    "Experience" = %s
                WHERE "UserID" = %s;
            """

            params = (username,email,phone,IsActive,UserProfileID,address,experience,UserID)
            #print("Full SQL:", query % params)
            result = DB().execute_update(query, params)
            #print(result)
        
            return result

        except Exception as e:
            log_exception(e)
            raise (e)

class CustomUser(User):
    def __init__(self,user_id,username=None, email=None, phone=None,is_active=True,userProfileID=None,Address=None,Experience=None,userprofileName = None,Privilege = None,UPActive = None):
        super().__init__(user_id, username, email, phone, is_active,userProfileID,Address,Experience)
        self.userProfileName = userprofileName
        self.Privilege = Privilege
        self.UPActive = UPActive
    def to_json(self):
        parentJson = super().to_json()
        json = {
            "UserProfileName":self.userProfileName,
            "Privilege":self.Privilege,
            "UPActive":self.UPActive
            }
        parentJson.update(json)

        return parentJson