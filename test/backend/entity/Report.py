
from typing import Self
from Database import DB
from utils.utils import log_exception

# CategoryID
# Title
# Description

class Report:
      

    #req 7 suspend category
    @staticmethod
    def getReport(mode:str)->list[dict]:
        try:
            #insert into user table
            statement =''
            if (mode == 'daily'):
                statement = """
                SELECT "Service"."DatePosted"::date AS "date", COUNT(*) AS PostCount
                FROM "Service"
                GROUP BY "date"
                ORDER BY "date";
                """
            elif (mode == 'weekly'):
                statement = """
                SELECT DATE_TRUNC('week', "Service"."DatePosted")::date AS "date", COUNT(*) AS PostCount
                FROM "Service"
                GROUP BY "date"
                ORDER BY "date";
                """
            elif(mode == 'monthly'):
                statement = """
                SELECT DATE_TRUNC('month', "Service"."DatePosted")::date AS "date", COUNT(*) AS PostCount
                FROM "Service"
                GROUP BY "date"
                ORDER BY "date";
                """
            params = ()
            result =DB().execute_fetchall(statement,params)
          
            return result


        except Exception as e:
            raise e
   