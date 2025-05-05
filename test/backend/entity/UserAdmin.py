import bcrypt
from Classes.Response import Response
from Database import DB
from entity.User import User
from utils.utils import log_exception
import psycopg2
#make cleaner class, inherits from user.py
class UserAdmin(User):
    def __init__(self):
        self.db = DB()
    #req 1.1 create
    def createUser(self,username,email,phone,experience,address,userType):
        try:
            hashed_password = bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt())
            UserprofileID = 1
                 #swithch case based on userType to change userstatement
            if userType == "Cleaner":
                UserprofileID = 1
            elif userType == "HomeOwner":
                UserprofileID = 2
            elif userType == "UserAdmin":
                UserprofileID = 3
            elif userType == "PlatformManagement":
                UserprofileID = 4
            else:
                raise ValueError("Invalid user type")
            #insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive","Address","Experience") values (%s, %s, %s,%s,%s,true,%s,%s) RETURNING "UserID"
                """
            params = (username,UserprofileID,email,phone,hashed_password,address,experience,)
            result =self.db.execute_update(Userstatement, params)
            id = result[0]#SQL statement returns a userID, which is the first argument in a tuple returned by psycopg2
            #insert into cleaner table
            
            return True


        except Exception as e:
            log_exception(e)
            raise e
    #req 1.1 view
    def viewUser(self,username):
        try:
            query = """
                        SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive", "Address", "Experience"
                        FROM "user"
                        WHERE LOWER("Username") = LOWER(%s)
                    """
            params = (username,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = self.db.execute_fetchone(query, params)
            #create json object based on query results
           

            if result is not None:
                data = {
                    "UserID": result[0],
                    "Username": result[1],
                    "UserProfileID": result[2],
                    "Email": result[3],
                    "Phone": result[4],
                    "IsActive": result[5],
                    "Address": result[6],
                    "Experience": result[7]
                }
                return data
            else:               
                return None
        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.1 suspend
    def suspendUser(self,username):
        try:
            query = """
                        UPDATE "user"
                        SET "IsActive" = false
                        WHERE LOWER("Username") = LOWER(%s)
                    """
            params = (username,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = self.db.execute_update(query, params)
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
    def searchByUserID(self, searchTerm):#overwrite User.searchByUserID 
        try:

            query = """
                SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive"
                FROM "user"
                WHERE "Username" ILIKE %s 
            """

            params = (f"{searchTerm}%",)
            #print("Full SQL:", query % params)
            result = self.db.execute_fetchall(query, params)
            #print(result)
            return result

        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.2 Create
    def createUserProfile(self,name,privilege):
        try:
            #insert into user table
            Userstatement = """
                Insert into "UserProfile" ("Name","Privilege") values (%s, %s) 
                """
            params = (name,privilege)
            result =self.db.execute_update(Userstatement, params)
            
            return True


        except Exception as e:
            log_exception(e)
            raise e
    #req 1.2 view
    def viewUserProfile(self,userProfileName):
        try:
            query = """
                        SELECT *
                        FROM "UserProfile"
                        WHERE LOWER("Name") = LOWER(%s)
                    """
            params = (userProfileName,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = self.db.fetch_one_by_key(query, params)
            #create json object based on query results
           

            return result
        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.1 suspendUserprofile
    def suspendUserProfile(self,name):
        try:
            query = """
                        UPDATE "UserProfile"
                        SET "Is_Active" = false
                        WHERE LOWER("Name") = LOWER(%s)
                    """
            params = (name,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = self.db.execute_update(query, params)
            #create json object based on query results
            #print(result)

            if result:
                return True
            else:               
                return False
        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.2 search user profile
    def searchUserProfile(self, searchTerm):#overwrite User.searchByUserID 
        try:

            query = """
                SELECT *
                FROM "UserProfile"
                WHERE "Name" ILIKE %s 
            """

            params = (f"{searchTerm}%",)
            #print("Full SQL:", query % params)
            result = self.db.execute_fetchall(query, params)
            #print(result)
            return result

        except Exception as e:
            log_exception(e)
            raise (e)
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
