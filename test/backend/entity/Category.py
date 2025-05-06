
from Database import DB
from Classes.CategoryResponse import CategoryResponse
from utils.utils import log_exception

# CategoryID
# Title
# Description


class Category:
    def __init__(self):
        self.db = DB()

    def ViewByCategoryID(self, CategoryID):
        try:
            query = """
                    SELECT *
                    FROM "Category"
                    WHERE "CategoryID" = %s
                    """
            params = (CategoryID,)

            result = self.db.fetch_one_by_key(query, params)

            return result

        except Exception as e:
            log_exception(e)
            raise (e)
