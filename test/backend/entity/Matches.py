
from Database import DB
from Classes.MatchesResponse import MatchesResponse
from utils.utils import log_exception

# ServiecID
# HomeOwnerID
# Price
# Date
# Rating


class Matches:
    def __init__(self):
        self.db = DB()
        self.Date = None
        self.SerivceID = None
        self.HomeOwnerID = None

    def searchByServiceID(self, ServiceID):
        try:
            self.SerivceID = ServiceID
            self.pullDetails
            if not self.Date or not hasattr(self, 'Date'):
                return MatchesResponse(False, 'Matches not found', None)
            return MatchesResponse(True, 'Matches found', self.to_dict)
        except Exception as e:
            log_exception(e)
            raise (e)

    def searchByHomeOwnerID(self, HomeOwnerID):
        try:
            self.HomeOwnerID = HomeOwnerID
            self.pullDetails()
            if not self.Date or not hasattr(self, 'Date'):
                return MatchesResponse(False, 'Matches not found', None)
            return MatchesResponse(True, 'Matches found', self.to_dict)
        except Exception as e:
            log_exception(e)
            raise (e)

    def pullDetails(self):
        query: str
        params: tuple

        if self.SerivceID or hasattr(self, 'ServiceID'):
            query = """
                    SELECT "ServiceID", "HomeOwnerID", "Price", "Date", "Rating"
                    FROM "Matches"
                    WHERE "ServiceID" = %s
                    """
            params = (self.SerivceID,)

        if self.HomeOwnerID or hasattr(self, 'HomeOwnerID'):
            query = """
                    SELECT "ServiceID", "HomeOwnerID", "Price", "Date", "Rating"
                    FROM "Matches"
                    WHERE "HomeOwnerID" = %s
                    """
            params = (self.HomeOwnerID,)

        if not query or not params:
            print(f"error: Nothing pass in while querying database")
            return

        result = self.db.execute_fetchone(query, params)

        if result:
            self.SerivceID = result[0]
            self.HomeOwnerID = result[1]
            self.Price = result[2]
            self.Date = result[3]
            self.Rating = result[4]
            print(f"Matches: Matches found")
            return

        print("Matches: Matches not found")

    def to_dict(self):
        return {
            'ServiecID': self.SerivceID,
            'HomeOwnerID': self.HomeOwnerID,
            'Price': self.Price,
            'Date': self.Date,
            'Rating': self.Rating
        }
