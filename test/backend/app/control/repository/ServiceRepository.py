from app.db import DB


class ServiceRepository:
    def findByServiceID(ServiceID) -> dict:
        query = """
                SELECT "ServiceID", "CategoryID", "Title", "Description", "DatePosted", "CleanerID", "LikeCount", "ViewCount", "MatchCount", "Price"
                FROM "Service"
                WHERE "ServiceID" = %s"""
        params = (ServiceID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"{ServiceID}: Details pulled")
            return {
                'ServiceID':  result[0],
                'CategoryID': result[1],
                'Title': result[2],
                'Description': result[3],
                'DatePosted': result[4],
                'CleanerID': result[5],
                'LikeCount':  result[6],
                'ViewCount':  result[7],
                'MatchCount': result[8],
                'Price': result[9]
            }

        print(f"{ServiceID}: Service not found")
        raise Exception("Service not found")

    def getTotalServiceLikes(ServiceID) -> int:
        query = """
                SELECT COUNT(DISTINCT "HomeOwnerID")
                FROM "ServiceLikes"
                WHERE "ServiceID" = %s
                GROUP BY "ServiceID"
                """
        params = (ServiceID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f'{ServiceID}: total ServiceLikes calculated successfully')
            return result[0]

        print(f'{ServiceID}: Failed to calculate total ServiceLikes. Returning 0')
        return 0

    def updateLikeCount(ServiceID):
        data = ServiceRepository.getTotalServiceLikes(ServiceID)

        query = """
                UPDATE "Service"
                SET "LikeCount" = %s
                WHERE "ServiceID" = %s
                """
        params = (data, ServiceID)

        db = DB()
        result = db.execute_update(query, params)

        if result:
            print(f'{ServiceID}: LikeCount updated')
            return

        raise Exception("Failed to update LikeCount")

    def getTotalViews(ServiceID) -> int:
        query = """
                SELECT COUNT(DISTINCT "HomeOwnerID")
                FROM "Views"
                WHERE "ServiceID" = %s
                GROUP BY "ServiceID"
                """
        params = (ServiceID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f'{ServiceID}: total Views calculated successfully')
            return result[0]

        print(f'{ServiceID}: Failed to calculate total Views. Returning 0')
        return 0

    def updateViewCount(ServiceID):
        data = ServiceRepository.getTotalViews(ServiceID)

        query = """
                UPDATE "Service"
                SET "ViewCount" = %s
                WHERE "ServiceID" = %s
                """
        params = (data, ServiceID)

        db = DB()
        result = db.execute_update(query, params)

        if result:
            print(f'{ServiceID}: ViewCount upated')
            return

        raise Exception("Failed to update ViewCount")

    def getTotalMatches(ServiceID) -> int:
        query = """
                SELECT COUNT(*)
                FROM "Matches"
                WHERE "ServiceID" = %s
                GROUP BY "ServiceID"
                """
        params = (ServiceID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f'{ServiceID}: total Matches calculated successfully')
            return result[0]

        print(f'{ServiceID}: Failed to calculate total Matches. Returning 0')
        return 0

    def updateMatchCount(ServiceID):
        data = ServiceRepository.getTotalMatches()

        query = """
                UPDATE "Service"
                SET "MatchCount" = %s
                WHERE "ServiceID" = %s
                """
        params = (data, ServiceID)

        db = DB()
        result = db.execute_update(query, params)

        if result:
            print(f'{ServiceID}: MatchCount upated')
            return

        raise Exception("Failed to update MatchCount")
