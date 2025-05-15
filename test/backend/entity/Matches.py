
from Database import DB
from Classes.MatchesResponse import MatchesResponse
from Classes.CustomMatch import CustomMatch
from Classes.CustomService import customService
from Classes.SimpleMatch import SimpleMatch
from utils.utils import log_exception

# ServiecID
# HomeOwnerID
# Price
# Date
# Rating


class Matches:
    def __init__(self,ServiceID:int,HomeOwnerID:int,MatchID:int):
        self.ServiceID = ServiceID
        self.HomeOwnerID = HomeOwnerID
        self.matchID = MatchID


# req 3 extra create
    @staticmethod
    def CreateMatch(HomeOwnerID:int, ServiceID:int, Price:float)->bool:
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
        
##################################################################################
# Req5.1 Req6.1 View History
##################################################################################

    @staticmethod
    def ViewMatch( matchID: int)->CustomMatch:
        try:
            # query = """
            #         SELECT 
            #             "ServiceID",
            #             "Service"."CategoryID",
            #             "Service"."Title",
            #             "Service"."Description",
            #             "DatePosted",
            #             "CleanerID",
            #             "LikeCount",
            #             "ViewCount",
            #             "MatchCount",
            #             "price",
            #             "ImageLink",
			# 			"Category"."Title" as "CatTitle",
			# 			"Category"."Description" as "CatDesc",
			# 			"Category"."Is_Active" as "CatActive",
			# 			"user"."Username",
			# 			"user"."Email",
			# 			"user"."Phone",
			# 			"user"."IsActive" as "UActive",
			# 			"user"."Experience",
            #             "Matches"."Price" as "DealPrice",
            #             "Matches"."DateCreated" as "DealDate"
            #         FROM "Service"
			# 		left join "Category" on "Category"."CategoryID" = "Service"."CategoryID"
            #         left join "user" on "user"."UserID" = "Service"."CleanerID"
            #         left join "Matches" on "Matches"."ServiceID" = "Service"."ServiceID"
			# 		WHERE "Matches"."ServiceID" = %s and "Service"."CleanerID" = %s
            #     """
            query = """
                    SELECT 
                        "Service"."ServiceID",
                        "Service"."CategoryID",
                        "Service"."Title",
                        "Service"."Description",
                        "DatePosted",
                        "CleanerID",
                        "LikeCount",
                        "ViewCount",
                        "MatchCount",
                        "price",
                        "ImageLink",
                        "Category"."Title" as "CatTitle",
                        "Category"."Description" as "CatDesc",
                        "Category"."Is_Active" as "CatActive",
                        "user"."Username" as "CleanerName",
                        "user"."Email",
                        "user"."Phone",
                        "user"."IsActive" as "UActive",
                        "user"."Experience",
                        "HomeOwner"."Address",
                        "HomeOwner"."Username" as "HomeOwnerName",
                        "Matches"."Price" as "DealPrice",
                        "Matches"."Date" as "DealDate"
                    FROM "Service"
                    left join "Category" on "Category"."CategoryID" = "Service"."CategoryID"
                    left join "user" on "user"."UserID" = "Service"."CleanerID"
                    left join "Matches" on "Matches"."ServiceID" = "Service"."ServiceID"
                    left join "user" as "HomeOwner" on "HomeOwner"."UserID" = "Matches"."HomeOwnerID"
					WHERE "Matches"."MatchID" = %s 
                """
            params = (matchID,)
            result = DB().fetch_one_by_key(query, params)
            print(result)
            if result:
                return CustomMatch(**result)
            else:
                return None
        except Exception as e:
            log_exception(e)
            raise e
        
#req 5.2
    def SearchMatchCleaner(searchTerm:str,CleanerID:int)->list[SimpleMatch]:

        try:
            query =''
            params = ()
            if searchTerm.rstrip() == '':
                query = """
                    SELECT 
                        "Service"."ServiceID",
                        "Service"."Title",
                        "price" as "Price",
                        "ImageLink",
                        "Matches"."Price" as "DealPrice",
                        "Matches"."Date" as "DealDate",
                        "Matches"."MatchID"
                    FROM "Service"
                    left join "Category" on "Category"."CategoryID" = "Service"."CategoryID"
                    left join "user" on "user"."UserID" = "Service"."CleanerID"
                    INNER join "Matches" on "Matches"."ServiceID" = "Service"."ServiceID"
                    WHERE "Service"."CleanerID" = %s
                    LIMIT 10;
                """
                params = (CleanerID,)
            else:
                query = """
                Select
                        "Service"."ServiceID",
                        "Service"."Title",
                        "price" as "Price",
                        "ImageLink",
                        "Matches"."Price" as "DealPrice",
                        "Matches"."Date" as "DealDate",
                        "Matches"."MatchID"
                    FROM "Service"
                    left join "Category" on "Category"."CategoryID" = "Service"."CategoryID"
                    left join "user" on "user"."UserID" = "Service"."CleanerID"
                    INNER join "Matches" on "Matches"."ServiceID" = "Service"."ServiceID"
                    WHERE "Service"."Title" LIKE %s and "Service"."CleanerID" = %s
                """
                params = (f"%{searchTerm}%", CleanerID,)
            result = DB().execute_fetchall(query, params)
            if result:  
                return [SimpleMatch(**match) for match in result]
            else:
                return []
        except Exception as e:
            log_exception(e)
            raise e
        
#req 6.2
    def SearchMatchHomeOwner(searchTerm:str,HomeOwnerID:int)->list[SimpleMatch]:
        
        try:
            query =''
            params = ()
            if searchTerm.rstrip() == '':
                query = """
                    SELECT 
                        "Service"."ServiceID",
                        "Service"."Title",
                        "price" as "Price",
                        "ImageLink",
                        "Matches"."Price" as "DealPrice",
                        "Matches"."Date" as "DealDate",
                        "Matches"."MatchID"
                    FROM "Service"
                    left join "Category" on "Category"."CategoryID" = "Service"."CategoryID"
                    left join "user" on "user"."UserID" = "Service"."CleanerID"
                    INNER join "Matches" on "Matches"."ServiceID" = "Service"."ServiceID"
                    WHERE "Matches"."HomeOwnerID" = %s
                    LIMIT 10;
                """
                params = (HomeOwnerID,)
            else:
                query = """
                SELECT
                        "Service"."ServiceID",
                        "Service"."Title",
                        "price" as "Price",
                        "ImageLink",
                        "Matches"."Price" as "DealPrice",
                        "Matches"."Date" as "DealDate",
                        "Matches"."MatchID"
                    FROM "Service"
                    left join "Category" on "Category"."CategoryID" = "Service"."CategoryID"
                    left join "user" on "user"."UserID" = "Service"."CleanerID"
                    INNER join "Matches" on "Matches"."ServiceID" = "Service"."ServiceID"
                    WHERE "Service"."Title" LIKE %s and "Matches"."HomeOwnerID" = %s
                """
                params = (f"%{searchTerm}%", HomeOwnerID,)
            result = DB().execute_fetchall(query, params)
            if result:  
                return [SimpleMatch(**match) for match in result]
            else:
                return []
        except Exception as e:
            log_exception(e)
            raise e