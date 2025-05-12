
from typing import Self
from Database import DB
from Classes.CategoryResponse import CategoryResponse
from utils.utils import log_exception

# CategoryID
# Title
# Description


class Category:
    def __init__(self,CategoryID:int,Title:str,Description:str,IsActive:bool=True):
      
        self.CategoryID = CategoryID
        self.Title = Title
        self.Description = Description
        self.IsActive = IsActive

    #to json method
    def to_json(self):
        return {
            "CategoryID": self.CategoryID,
            "Title": self.Title,
            "Description": self.Description,
            "IsActive": self.IsActive
        }
        
    #req 7 create
    @staticmethod
    def createCategory(Title:str,Description:str)->bool:
        try:
            #insert into user table
            statement = """
                Insert into "Category" 
                ("Title","Description") 
                values (%s, %s)
                """
            params = (Title,Description,)
            result =DB().execute_update(statement, params)
            
            return result


        except Exception as e:
            log_exception(e)
            raise e
    
    #req 7 view
    @staticmethod
    def viewCategory(categoryID:int)->Self:
        try:
            query = """
                    SELECT "CategoryID","Title","Description","Is_Active"
                    FROM "Category"
                    WHERE "CategoryID" = %s
                    """
            params = (categoryID,)

            result = DB().fetch_one_by_key(query, params)
            if result:
                return Category(result["CategoryID"],result["Title"],result["Description"],result["Is_Active"])
            else:
                return None

        except Exception as e:
            log_exception(e)
            raise (e)

    @staticmethod
    def updateCategory(categoryID:int,Title:str,Description:str,Is_Active:bool)->bool:
        try:
            #insert into user table
            statement = """
                update "Category" 
                set "Title" = %s,
                "Description" = %s,
                "Is_Active" = %s
                where "CategoryID" = %s
                """
            params = (Title,Description,Is_Active,categoryID,)
            result =DB().execute_update(statement, params)
            
            return result


        except Exception as e:
            log_exception(e)
            raise e

    #req 7 suspend category
    @staticmethod
    def suspendCategory(categoryID:int)->bool:
        try:
            #insert into user table
            statement = """
                update "Category" 
                set "Is_Active" = false
                where "CategoryID" = %s
                """
            params = (categoryID,)
            result =DB().execute_update(statement, params)
            
            return result


        except Exception as e:
            log_exception(e)
            raise e
    
    #req 7 search category
    @staticmethod
    def searchCategory(keyword:str)->list[Self]:
        try:
            query = """
                    SELECT *
                    FROM "Category"
                    WHERE "Title" ILIKE %s
                    """
            params = ('%'+keyword.rstrip().lstrip()+'%',)

            result = DB().execute_fetchall(query, params)
            if result is None or len(result) == 0:
                return []
            else:
                return [Category(result['CategoryID'],result['Title'],result['Description'],result['Is_Active'])for result in result]

        except Exception as e:
            log_exception(e)
            raise (e)