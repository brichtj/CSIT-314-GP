
from typing import Self
from Database import DB
from Classes.ServiceResponse import ServiceResponse
from utils.utils import log_exception

# ServiceID
# CategoryID
# Title
# Description
# DatePosted
# CleanerID
# LikeCount
# ViewCount
# MatchCount
# Price


class Service:

    #convert all to capital first
    def __init__(self, ServiceID=None, CategoryID=None, Title=None, Description=None,
                DatePosted=None, CleanerID=None, LikeCount=None, ViewCount=None,
                MatchCount=None, price=None, ImageLink=None):
        self.db = DB()
        self.ServiceID = ServiceID
        self.CategoryID = CategoryID
        self.Title = Title
        self.Description = Description
        self.DatePosted = DatePosted
        self.CleanerID = CleanerID
        self.LikeCount = LikeCount
        self.ViewCount = ViewCount
        self.MatchCount = MatchCount
        self.price = price
        self.ImageLink = ImageLink


    #to json method
    def to_json(self) -> dict:
        return {
            "ServiceID": self.ServiceID,
            "CategoryID": self.CategoryID,
            "Title": self.Title,
            "Description": self.Description,
            "DatePosted": self.DatePosted,
            "CleanerID": self.CleanerID,
            "LikeCount": self.LikeCount,
            "ViewCount": self.ViewCount,
            "MatchCount": self.MatchCount,
            "Price": self.price,
            "ImageLink": self.ImageLink
        }

##################################################################################
# Req3.1 Search Service
##################################################################################
    @staticmethod
    def SearchService(mode: int, searchTerm: str)->Self:
        try:

            query = ''
            if mode == 1:#by title
                query = """
                        SELECT 
                        "ServiceID",
                        "CategoryID",
                        "Title",
                        "Description",
                        "DatePosted",
                        "CleanerID",
                        "LikeCount",
                        "ViewCount",
                        "MatchCount",
                        "price",
                        "ImageLink"
                        FROM "Service"
                        WHERE "Title" ILIKE %s
                        """
            elif mode == 2:#by category name
                query = """
                        SELECT 
                        "ServiceID",
                        "CategoryID",
                        "Title",
                        "Description",
                        "DatePosted",
                        "CleanerID",
                        "LikeCount",
                        "ViewCount",
                        "MatchCount",
                        "price",
                        "ImageLink"
                        FROM "Service"
                        WHERE "CategoryID" IN(
                            SELECT "CategoryID"
                            FROM "Category"
                            WHERE "Title" ILIKE %s
                        )
                        """
            params = (f"%{searchTerm}%",)

            result = DB().execute_fetchall(query, params)

            return [Service(**row) for row in result]

        except Exception as e:
            log_exception(e)
            raise e

##################################################################################
# Req4.1 View Total Views of Services
##################################################################################
    @staticmethod
    def ViewTotalViewbyID(ServiceID:int)->int:
        try:
            query = """
                    SELECT "ViewCount"
                    FROM "Service"
                    WHERE "ServiceID" = %s
                    """
            params = (ServiceID,)

            result = DB().fetch_one_by_key(query, params)
            if result is not None:
                return result["ViewCount"]
            else:
                return None
            
        except Exception as e:
            log_exception(e)
            raise e


##################################################################################
# Req4.2 View Total Shortlisted Count of Services
##################################################################################
    @staticmethod
    def ViewTotalShortlistedCountByID(ServiceID:int)->int:
        try:
            query = """
                    SELECT "LikeCount"
                    FROM "Service"
                    WHERE "ServiceID" = %s
                    """
            params = (ServiceID,)

            result = DB().fetch_one_by_key(query, params)
            if result is not None:
                return result["LikeCount"]
            else:
                return None

            return result
        except Exception as e:
            log_exception(e)
            raise e

    #req 2 create service
    def createService(self,CategoryID:int ,Title:str ,Description:str ,CleanerID:int ,Price:float ,ImageLink:str)->bool:
        try:
            query = """
                    INSERT INTO "Service" ("CategoryID", "Title", "Description", "CleanerID", "price", "ImageLink")
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING "ServiceID"
                    """
            values = (CategoryID, Title, Description, CleanerID, Price, ImageLink)

            res = self.db.insertFreeStyle(query, values)

            return True

        except Exception as e:
            print(e)
            log_exception(e)
            raise (e)
        
#req 2, req 3.2,req 3.3 view service by serviceID
    def viewService(self,ServiceID:int,updateViewCount:bool)->Self:
        try:
            query = """
                    SELECT 
                        "ServiceID",
                        "CategoryID",
                        "Title",
                        "Description",
                        "DatePosted",
                        "CleanerID",
                        "LikeCount",
                        "ViewCount",
                        "MatchCount",
                        "price",
                        "ImageLink"
                    FROM "Service"
                    WHERE "ServiceID" = %s;
                """
            params = (ServiceID,)

            result = self.db.fetch_one_by_key(query, params)
            if updateViewCount == True:
                updateServiceViewCount = """
                        UPDATE "Service"
                        SET "ViewCount" = "ViewCount" + 1
                        WHERE "ServiceID" = %s;
                    """
                
                self.db.execute_update(updateServiceViewCount, params)

            if result:
                return Service(**result) 
            else:
                return None
        
        except Exception as e:
            log_exception(e)
            raise e
        
#req 2 update service by serviceID
    def updateService(self,CategoryID:int,Title:str,Description:str,price:float,ImageLink:str, ServiceID:int,CleanerID:int)->bool:
        try:
            #only cleaner can update his own service, thats why required cleanerID
            query = """
                    UPDATE "Service"
                    SET "CategoryID" = %s,
                        "Title" = %s,
                        "Description" = %s,
                        "price" = %s,
                        "ImageLink" = %s
                    WHERE "ServiceID" = %s and "CleanerID" = %s;
                """
            params = (CategoryID,Title,Description,price,ImageLink,ServiceID,CleanerID)

            result = self.db.execute_update(query, params)
            return result


        except Exception as e:
            log_exception(e)
            raise e
        
    #req 2 delete service by serviceID
    def deleteService(self,ServiceID:int,CleanerID:int)->bool:
        try:
            query = """
                    DELETE FROM "Service"
                    WHERE "ServiceID" = %s and "CleanerID" = %s;
                """
            params = (ServiceID,CleanerID,)

            result = self.db.execute_delete(query, params)
            return result

        except Exception as e:
            log_exception(e)
            raise e
        
    #req 2 search Service by title and cleanerID(so that cleaner can search his own services)
    def searchServiceByCleanerID(self,Title:str,CleanerID:int)->list[Self]:
        try:
            query = """
                    SELECT 
                        "ServiceID",
                        "CategoryID",
                        "Title",
                        "Description",
                        "DatePosted",
                        "CleanerID",
                        "LikeCount",
                        "ViewCount",
                        "MatchCount",
                        "price",
                        "ImageLink"
                    FROM "Service"
                    WHERE "Title" ILIKE %s and "CleanerID" = %s;
                """
            params = ('%'+Title+'%',CleanerID,)

            result = self.db.execute_fetchall(query, params)
            if result is None or len(result) == 0:
                return []
            else:
                return [Service(**row)for row in result]
        except Exception as e:
            log_exception(e)
            raise e