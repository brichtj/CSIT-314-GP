from app.db import DB


class UserRepository:
    def findByEmail(UserProfile, Email) -> tuple:
        query = """
            SELECT "Email", "Password"
            FROM "User"
            WHERE "UserProfile" = %s
            AND "Email" = %s"""

        params = (UserProfile, Email,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"{Email}: User found")
            return result

        print(f"{Email}: User not found")
        raise Exception('User not found')
    
    def pullDetails(Email) -> dict:
        query = """
                SELECT "UserID", "Username", "UserProfile", "Email", "Phone", "IsActive"
                FROM "User"
                WHERE "Email" = %s"""
        params = (Email,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"{Email}: Details pulled")
            return {
                "UserID": result[0],
                "Username": result[1],
                "UserProfile": result[2],
                "Email": result[3],
                "Phone": result[4],
                "IsActive": result[5]
            }

        print(f"{Email}: Failed to pull details")
        raise Exception("Failed to pull details")

    def pullExperience(UserID) -> dict:
        query = """
                SELECT "Experience"
                FROM "Cleaner"
                WHERE "CleanerID" = %s"""
        params = (UserID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"{UserID}: Cleaner Experience pulled")
            return {'Experience': result[0]}

        print(f"{UserID}: Failed to pull Cleaner Experience")
        raise Exception("Failed to pull Cleaner Expreience")

    def pullAddress(UserID) -> dict:
        query = """
                SELECT "Address"
                FROM "HomeOwner"
                WHERE "HomeOwnerID" = %s"""
        params = (UserID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"{UserID}: HomeOwner Address pulled")
            return {'Address': result[0]}

        print(f"{UserID}: Failed to pull HomeOwner Address")
        raise Exception("Failed to pull HomeOwner Address")
