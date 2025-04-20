from app.db import DB


class MatchesRepository:
    def findByServiceID(ServiceID):
        query = """
                SELECT "ServiceID", "HomeOwnerID", "Price", "Date", "Rating"
                FROM "Matches"
                WHERE "ServiceID" = %s
                """
        params = (ServiceID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"Matches: Matches found")
            return {
                'SerivceID': result[0],
                'HomeOwnerID': result[1],
                'Price': result[2],
                'Date': result[3],
                'Rating': result[4]
            }

        print("Matches: Matches not found")
        raise Exception("Matches not found")

    def findByHomeOwnerID(HomeOwnerID):
        query = """
                SELECT "ServiceID", "HomeOwnerID", "Price", "Date", "Rating"
                FROM "Matches"
                WHERE "ServiceID" = %s
                """
        params = (HomeOwnerID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"Matches: Matches found")
            return {
                'SerivceID': result[0],
                'HomeOwnerID': result[1],
                'Price': result[2],
                'Date': result[3],
                'Rating': result[4]
            }

        print("Matches: Matches not found")
        raise Exception("Matches not found")
