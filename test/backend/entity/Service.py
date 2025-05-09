
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
    def SearchService(self, mode, data):
        if (mode == 1):
            result = self.SearchServiceByCategoryName(data)
        if (mode == 2):
            result = self.SearchServiceByCategoryID(data)
        if (mode == 3):
            result = self.SearchServiceByCleanerID(data)

        result = self.SearchServiceByTitle(data)

        return result

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

        return result