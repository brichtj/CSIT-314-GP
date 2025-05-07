
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
    def __init__(self):
        self.db = DB()

##################################################################################
# Req3.1 Search Service
##################################################################################

    def SearchServiceByTitle(self, Title: str):
        try:
            query = """
                    SELECT *
                    FROM "Service"
                    WHERE "Title" ILIKE %s
                    """
            params = (f"%{Title}%",)

            result = self.db.execute_fetchall(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise e

    def SearchServiceByCategoryName(self, CategoryName: str):
        try:
            query = """
                    SELECT * 
                    FROM "Service"
                    WHERE "CategoryID" IN(
                        SELECT "CategoryID"
                        FROM "Category"
                        WHERE "Title" ILIKE %s
                    )
                    """
            params = (CategoryName,)

            result = self.db.execute_fetchall(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise e

    def SearchServiceByCategoryID(self, CategoryID: str):
        try:
            query = """
                    SELECT *
                    FROM "Service"
                    WHERE "CategoryID" = %s
                    """
            params = (CategoryID,)

            result = self.db.execute_fetchall(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise e

    def SearchServiceByCleanerID(self, CleanerID: str):
        try:
            query = """
                    SELECT *
                    FROM "Service"
                    WHERE "CleanerID" = %s
                    """
            params = (CleanerID,)

            result = self.db.execute_fetchall(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise e


##################################################################################
# Req3.2 Req3.5 View Service
##################################################################################

    def ViewServiceByID(self, ServiceID: str):
        try:
            query = """
                    SELECT *
                    FROM "Service"
                    WHERE "ServiceID" = %s
                    """
            params = (ServiceID,)

            result = self.db.fetch_one_by_key(query, params)

            return result

        except Exception as e:
            log_exception(e)
            raise (e)

##################################################################################
# Req4.1 View Total Views of Services
##################################################################################

    def ViewTotalViewbyID(self, ServiceID):
        try:
            query = """
                    SELECT "ViewCount"
                    FROM "Service"
                    WHERE "ServiceID" = %s
                    """
            params = (ServiceID,)

            result = self.db.fetch_one_by_key(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise e


##################################################################################
# Update Total Views of Services
##################################################################################

    def UpdateTotalViewByID(self, ServiceID):
        query = """
                UPDATE "Service"
                SET "ViewCount" = (
                    SELECT COUNT(*)
                    FROM "Views"
                    WHERE "ServiceID" = %s
                )
                WHERE "ServiceID" = %s
                """
        params = (ServiceID, ServiceID)

        result = self.db.execute_update(query, params)

        return result

##################################################################################
# Req4.2 View Total Shortlisted Count of Services
##################################################################################

    def ViewTotalShortlistedCountByID(self, ServiceID):
        try:
            query = """
                    SELECT "LikeCount"
                    FROM "Service"
                    WHERE "ServiceID" = %s
                    """
            params = (ServiceID,)

            result = self.db.fetch_one_by_key(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise e

##################################################################################
# Update Total Shortlisted Count of Services
##################################################################################

    def UpdateTotalShortlistedCountViewByID(self, ServiceID):
        query = """
                UPDATE "Service"
                SET "LikeCount" = (
                    SELECT COUNT(*)
                    FROM "ServiceLikes"
                    WHERE "ServiceID" = %s
                )
                WHERE "ServiceID" = %s
                """
        params = (ServiceID, ServiceID)

        result = self.db.execute_update(query, params)

        return result

##################################################################################
# View Total Matches Count of Services
##################################################################################

    def ViewTotalShortlistedCount(self, ServiceID):
        try:
            query = """
                    SELECT "MatchCount"
                    FROM "Service"
                    WHERE "ServiceID" = %s
                    """
            params = (ServiceID,)

            result = self.db.fetch_one_by_key(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise e

##################################################################################
# Update Total Matches Count of Services
##################################################################################

    def UpdateTotalShortlistedCountViewByID(self, ServiceID):
        query = """
                UPDATE "Service"
                SET "MatchCount" = (
                    SELECT COUNT(*)
                    FROM "Matches"
                    WHERE "ServiceID" = %s
                )
                WHERE "ServiceID" = %s
                """
        params = (ServiceID, ServiceID)

        result = self.db.execute_update(query, params)

        if result:
            #self.MatchCount = data
            print(f'{self.ServiceID}: MatchCount upated')
            return

        print("Failed to update MatchCount")

    def to_dict(self) -> dict:
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
            "Price": self.Price
        }
    
    def createService(self,CategoryID,Title,Description,CleanerID,Price,ImageLink)->bool:
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
