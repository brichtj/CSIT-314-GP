import bcrypt
from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
import psycopg2
from typing import Self
#make cleaner class, inherits from user.py
class UserProfile():
    def __init__(self,UserProfileID,Name,Privilege,Is_Active):
        self.UserProfileID = UserProfileID
        self.Name = Name
        self.Privilege = Privilege
        self.Is_Active = Is_Active
    def __str__(self):
        return f"UserProfileID: {self.UserProfileID}, Name: {self.Name}, Privilege: {self.Privilege}, Is_Active: {self.Is_Active}"
    def to_json(self) -> dict:
        return {
            "UserProfileID": self.UserProfileID,
            "Name": self.Name,
            "Privilege": self.Privilege,
            "Is_Active": self.Is_Active
        }
    #req 1.2 Create
    @staticmethod
    def createUserProfile(name,privilege)->bool:
        try:
            #insert into user table
            Userstatement = """
                Insert into "UserProfile" ("Name","Privilege") values (%s, %s) 
                """
            params = (name,privilege)
            result =DB().execute_update(Userstatement, params)
            if result is None:
                return False
            else:
                return True


        except Exception as e:
            log_exception(e)
            raise e
    #req 1.2 view
    @staticmethod
    def viewUserProfile(userProfileID:int)->Self:
        try:
            query = """
                        SELECT *
                        FROM "UserProfile"
                        WHERE "UserProfileID" = %s
                    """
            params = (userProfileID,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = DB().fetch_one_by_key(query, params)
            if result is not None:
                #create json object based on query results
                user = UserProfile(result['UserProfileID'],result['Name'],result['Privilege'],result['Is_Active'])
                return user
            else:
                return None
        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.1 suspendUserprofile
    @staticmethod
    def suspendUserProfile(userProfileID:int)->bool:
        try:
            query = """
                        UPDATE "UserProfile"
                        SET "Is_Active" = false
                        WHERE "UserProfileID" = %s
                    """
            params = (userProfileID,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = DB().execute_update(query, params)
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
    @staticmethod
    def searchUserProfile( searchTerm:str)->list[Self]:#overwrite User.searchByUserID 
        try:

            query = """
                SELECT *
                FROM "UserProfile"
                WHERE "Name" ILIKE %s 
            """
            #if empty string is passed in, its equivalent to retrieving all user profiles
            params = (f"{searchTerm.rstrip()}%",)
            #print("Full SQL:", query % params)
            result = DB().execute_fetchall(query, params)
            if result is None or len(result) == 0:
                return []
            else:
                return [UserProfile(**row)for row in result]

        except Exception as e:
            log_exception(e)
            raise (e)
    #req 1.2 update User Profile
    def updateUserProfile( name:str,privilege:str,is_active:bool,userprofileID:int)->bool:#overwrite User.searchByUserID 
        try:

            query = """
                update "UserProfile"
                set "Name" = %s,
                "Privilege" = %s,
                "Is_Active" = %s
                where "UserProfileID" = %s
            """

            params = (name,privilege,is_active,userprofileID,)
            #print("Full SQL:", query % params)
            result = DB().execute_update(query, params)
            #print(result)
            return result

        except Exception as e:
            log_exception(e)
            raise (e)
