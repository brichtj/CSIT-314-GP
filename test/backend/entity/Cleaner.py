import bcrypt
from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
from entity.User import User
import bcrypt
import psycopg2
#make cleaner class, inherits from user.py
class Cleaner(User):
    def __init__(self,  username=None, email=None, phone=None,Experience = None,  is_active=True):
        super().__init__(username, None, email, phone, "Cleaner", is_active)   

        self.Experience = Experience
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
                Insert into "Cleaner" ("CleanerID","Experience") values (%s, %s)
                """
            params = (id,self.Experience)
            result =self.db.execute_update(Userstatement, params)
            
            return True
        except Exception as e:
            log_exception(e)
            raise e
        
    def viewMyService(self,cleanerID):
        try:
            #insert into user table
            query = """
                    select * from "Service" where "CleanerID" = %s
                """
            params = (cleanerID,)
            result =self.db.execute_fetchall(query, params)
            return result
        
        except Exception as e:
            log_exception(e)
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

    def deleteMyService(self,cleanerID, serviceID)->bool:
        try:
            #insert into user table
            query = """
                    delete  from "Service" where "CleanerID" = %s and "ServiceID" = %s
                """
            params = (cleanerID,serviceID)
            result =self.db.execute_delete(query,params)
            return True
        
        except Exception as e:
            #log_exception(e)
            raise e
    def searchMyService(self,cleanerID:int,serviceTitle:str)->list:
        try:
            print(len(serviceTitle.strip()))
            query ='' 
            params = ()
            if len(serviceTitle.strip()) == 0:
            #empty serviceTitle, means want to query all by cleanerID
                query = """
                    select * from "Service" where "CleanerID" = %s
                """
                params = (cleanerID,)
            else:
                query = """
                    select * from "Service" where "CleanerID" = %s and "Title" ILIKE %s
                """
                params = (cleanerID,f"{serviceTitle}%",)
            result =self.db.execute_fetchall(query,params)
            return result
        
        except Exception as e:
            #log_exception(e)
            raise e
    
    def updateService(self,categoryID:int,title:str,description:str,cleanerID:int,price:float,ImageLink:str,serviceID:int)->bool:
        
        try:
            update_query = """
            UPDATE "Service"
            SET "CategoryID" = %s,
                "Title" = %s,
                "Description" = %s,
                "CleanerID" = %s,
                "price" = %s,
                "ImageLink" = %s
            WHERE "ServiceID" = %s
            """
            params = (categoryID,title,description,cleanerID,price,ImageLink,serviceID)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = self.db.execute_update(update_query,params)
            #create json object based on query results
            

            return result
        except Exception as e:
            log_exception(e)
            raise (e)
