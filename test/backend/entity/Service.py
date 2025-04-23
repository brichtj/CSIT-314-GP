
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
        self.ServiceID = None
        self.db = DB()
        self.Title = None

    def searchByServiceID(self, ServiceID) -> ServiceResponse:
        try:
            self.ServiceID = ServiceID
            self.pullDetails()
            if not hasattr(self, 'Title') or not self.Title:
                return ServiceResponse(False, "Service not found", None)

            self.update_LikeCount()
            self.update_MatchCount()
            self.update_ViewCount()

            return ServiceResponse(True, "Service found", self.to_dict())

        except Exception as e:
            log_exception(e)
            raise (e)

    def pullDetails(self):
        query = """
                SELECT "ServiceID", "CategoryID", "Title", "Description", "DatePosted", "CleanerID", "LikeCount", "ViewCount", "MatchCount", "Price"
                FROM "Service"
                WHERE "ServiceID" = %s"""
        params = (self.ServiceID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            self.ServiceID = result[0]
            self.CategoryID = result[1]
            self.Title = result[2]
            self.Description = result[3]
            self.DatePosted = result[4]
            self.CleanerID = result[5]
            self.LikeCount = result[6]
            self.ViewCount = result[7]
            self.MatchCount = result[8]
            self.Price = result[9]
            print(f"{self.ServiceID}: Details pulled")
            return

        print(f"{self.ServiceID}: Failed to pull datails")

    def get_total_ServiceLikes(self) -> int:
        query = """
                SELECT COUNT(DISTINCT "HomeOwnerID")
                FROM "ServiceLikes"
                WHERE "ServiceID" = %s
                GROUP BY "ServiceID"
                """
        params = (self.ServiceID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            print(f'{self.ServiceID}: total ServiceLikes calculated successfully')
            return result[0]

        print(f'{self.ServiceID}: Failed to calculate total ServiceLikes. Returning 0')
        return 0

    def update_LikeCount(self):
        data = self.get_total_ServiceLikes()

        query = """
                UPDATE "Service"
                SET "LikeCount" = %s
                WHERE "ServiceID" = %s
                """
        params = (data, self.ServiceID)

        result = self.db.execute_update(query, params)

        if result:
            self.LikeCount = data
            print(f'{self.ServiceID}: LikeCount updated')
            return

        print(f"Failed to update LikeCount")

    def get_total_Views(self) -> int:
        query = """
                SELECT COUNT(DISTINCT "HomeOwnerID")
                FROM "Views"
                WHERE "ServiceID" = %s
                GROUP BY "ServiceID"
                """
        params = (self.ServiceID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            print(f'{self.ServiceID}: total Views calculated successfully')
            return result[0]

        print(f'{self.ServiceID}: Failed to calculate total Views. Returning 0')
        return 0

    def update_ViewCount(self):
        data = self.get_total_Views()

        query = """
                UPDATE "Service"
                SET "ViewCount" = %s
                WHERE "ServiceID" = %s
                """
        params = (data, self.ServiceID)

        result = self.db.execute_update(query, params)

        if result:
            self.ViewCount = data
            print(f'{self.ServiceID}: ViewCount upated')
            return

        print(f"Failed to update ViewCount")

    def get_total_Matches(self) -> int:
        query = """
                SELECT COUNT(*)
                FROM "Matches"
                WHERE "ServiceID" = %s
                GROUP BY "ServiceID"
                """
        params = (self.ServiceID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            print(f'{self.ServiceID}: total Matches calculated successfully')
            return result[0]

        print(f'{self.ServiceID}: Failed to calculate total Matches. Returning 0')
        return 0

    def update_MatchCount(self):
        data = self.get_total_Matches()

        query = """
                UPDATE "Service"
                SET "MatchCount" = %s
                WHERE "ServiceID" = %s
                """
        params = (data, self.ServiceID)

        result = self.db.execute_update(query, params)

        if result:
            self.MatchCount = data
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
