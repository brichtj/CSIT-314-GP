
from Database import DB
from Classes.MatchesResponse import MatchesResponse
from utils.utils import log_exception

# ServiecID
# HomeOwnerID
# Price
# Date
# Rating


class Matches:
    def __init__(self,ServiceID:int,HomeOwnerID:int):
        self.db = DB()
        self.ServiceID = ServiceID
        self.HomeOwnerID = HomeOwnerID

    def SearchByServiceID(self, ServiceID):
        try:
            query = """
                    SELECT *
                    FROM "Matches"
                    WHERE "ServiceID" = %s
                    """
            params = (ServiceID,)

            result = self.db.fetch_one_by_key(query, params)

            return result

        except Exception as e:
            log_exception(e)
            raise (e)

    def SearchByHomeOwnerID(self, HomeOwnerID):
        try:
            query = """
                    SELECT *
                    FROM "Matches"
                    WHERE "HomeOwnerID" = %s
                    """
            params = (self.HomeOwnerID,)

            result = self.db.fetch_one_by_key(query, params)

            return result

        except Exception as e:
            log_exception(e)
            raise (e)


##################################################################################
# Req5.1 Req6.1 View History
##################################################################################


    def ViewCleanerHistory(self, CleanerID):
        try:
            query = """
                    SELECT *
                    FROM "Matches"
                    WHERE "ServiceID" IN(
                        SELECT "ServiceID"
                        FROM "Service"
                        WHERE "CleanerID" = %s
                    )
                    """
            params = (CleanerID,)
            result = self.db.execute_fetchall(query, params)
            return result
        except Exception as e:
            log_exception(e)
            raise e
        
    def ViewHomeOwnerHistory(self, HomeOwnerID):
        try:
            query = """
                    SELECT *
                    FROM "Matches"
                    WHERE "HomeOwnerID" = %s
                    """
            params = (HomeOwnerID,)
            result = self.db.execute_fetchall(query, params)
            return result
        except Exception as e:
            log_exception(e)
            raise e

##################################################################################
# Req5.2 Req.6.2 Search History
##################################################################################

    def SearchCleanerHistoryByServiceID(self, CleanerID, ServiceID):
        try:
            query = """
                    SELECT m.*
                    FROM "Matches" m
                    JOIN "Service" s ON m."ServiceID" = s."ServiceID"
                    WHERE s."CleanerID" = %s
                    AND m."ServiceID" = %s
                    """
            params = (CleanerID, ServiceID)
            result = self.db.execute_fetchall(query, params)
            return result
        except Exception as e:
            log_exception(e)
            raise e

    def SearchHomeOwnerHistoryByServiceID(self, HomeOwnerID, ServiceID):
        try:
            query = """
                    SELECT *
                    FROM "Matches"
                    WHERE "HomeOwnerID" = %s
                    AND "ServiceID" = %s
                    """
            params = (HomeOwnerID, ServiceID)
            result = self.db.execute_fetchall(query, params)
            return result
        except Exception as e:
            log_exception(e)
            raise e
# req 3 extra create
    def CreateMatch(self, HomeOwnerID:int, ServiceID:int, Price:float,)->bool:
        try:
            query = """
                    INSERT INTO "Matches" ("ServiceID","HomeOwnerID", "Price")
                    VALUES (%s, %s, %s)
                    """
            UpdateMatch = """
                    UPDATE "Service"
                    SET "MatchCount" = "MatchCount" + 1
                    WHERE "ServiceID" = %s

                """
            params = (ServiceID,HomeOwnerID, Price,)
            param2  = (ServiceID,)
            result = DB().update_two_tables(query,params,UpdateMatch,param2)
            return result
        except Exception as e:
            log_exception(e)
            raise e