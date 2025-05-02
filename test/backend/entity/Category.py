
from Database import DB
from Classes.CategoryResponse import CategoryResponse
from utils.utils import log_exception

# CategoryID
# Title
# Description


class Category:
    def __init__(self):
        self.db = DB()
        self.Title = None

    def searchByCategoryID(self, CategoryID) -> CategoryResponse:
        try:
            self.CategoryID = CategoryID
            self.pullDetails()
            if not hasattr(self, 'Title') or not self.Title:
                return CategoryResponse(False, "Category not found", None)

            return CategoryResponse(True, "Category found", self.to_dict())
        except Exception as e:
            log_exception(e)
            raise (e)

    def pullDetails(self):
        query = """
                SELECT "CategoryID", "Title", "Description"
                FROM "Category"
                WHERE "CategoryID" = %s
                """
        params = (self.CategoryID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            self.CategoryID = result[0]
            self.Title = result[1]
            self.Description = result[2]
            print(f"{self.CategoryID}: Details pulled")
            return

        print(f"{self.CategoryID}: Category not found")

    def to_dict(self) -> dict:
        return {
            "CategoryID": self.CategoryID,
            "Title": self.Title,
            "Description": self.Description
        }
