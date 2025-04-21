from app.db import DB

# CategoryID
# Title
# Description


class Category:
    def __init__(self, CategoryID):
        self.CategoryID = CategoryID
        self.pullDetails()

    def pullDetails(self):
        query = """
                SELECT "CategoryID", "Title", "Description"
                FROM "Category"
                WHERE "CategoryID" = %s
                """
        params = (self.CategoryID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.CategoryID = result[0]
            self.Title = result[1]
            self.Description = result[2]
            print(f"{self.CategoryID}: Details pulled")
            return

        print(f"{self.CategoryID}: Category not found")
        raise Exception("Category not found")

    def to_dict(self) -> dict:
        return {
            "CategoryID": self.CategoryID,
            "Title": self.Title,
            "Description": self.Description
        }
