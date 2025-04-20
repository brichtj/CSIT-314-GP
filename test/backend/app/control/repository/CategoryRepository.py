from app.db import DB


class CategoryRepository:
    def findByCategoryID(CategoryID) -> dict:
        query = """
                SELECT "CategoryID", "Title", "Description"
                FROM "Category"
                WHERE "CategoryID" = %s
                """
        params = (CategoryID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            print(f"{CategoryID}: Details pulled")
            return {
                "CategoryID": result[0],
                "Title": result[1],
                "Description": result[2]
            }

        print(f"{CategoryID}: Category not found")
        raise Exception("Category not found")
