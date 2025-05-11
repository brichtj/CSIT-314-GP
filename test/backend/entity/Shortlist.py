#create shortlist entity
from Database import DB
from entity.Service import Service
from utils.utils import log_exception


class Shortlist:
    def __init__(self, userid, serviceid):
        self.userid = userid
        self.serviceid = serviceid

    #to_json method
    def to_json(self):
        return {
            "userid": self.userid,
            "serviceid": self.serviceid
        }

    #req 3.3
    @staticmethod
    def shortListService(serviceID:int,HomeOwnerID:int)->bool:
        try:
            Insertquery = """
                    INSERT INTO "Shortlist_Record" ("ServiceID", "HomeOwnerID")
                    VALUES (%s, %s);
                """
            UpdateLikeCountQuery = """
                    UPDATE "Service"
                    SET "LikeCount" = "LikeCount" + 1
                    WHERE "ServiceID" = %s;
                """
            param1 = (serviceID,HomeOwnerID,)
            param2 = (serviceID,)
            result = DB().update_two_tables(Insertquery,param1,UpdateLikeCountQuery,param2)


            return result

        except Exception as e:
            log_exception(e)
            raise e
        
    #req 3.4(custom return object, check usecase description)
    def searchShortlistForHomeOwner(self,HomeOwnerID:int,Title:str)->list[Service]:
        try:
            query = """

            SELECT "Service"."ServiceID",
                        "CategoryID",
                        "Title",
                        "Description",
                        "DatePosted",
                        "CleanerID",
                        "LikeCount",
                        "ViewCount",
                        "MatchCount",
                        "price",
                        "ImageLink" FROM public."Shortlist_Record"
LEFT join "Service" ON "Service"."ServiceID" = "Service"."ServiceID"
where "HomeOwnerID" = %s and "Service"."Title" = ILIKE %s
                """
            params = (HomeOwnerID,f"%{Title}%",)

            result = DB().execute_fetchall(query,params)

            return [Service(**row)for row in result]

        except Exception as e:
            log_exception(e)
            raise e