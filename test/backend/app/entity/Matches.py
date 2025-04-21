from app.db import DB

# ServiecID
# HomeOwnerID
# Price
# Date
# Rating


class Matches:
    def __init__(self, ServiceID, HomeOwnerID, Date):
        self.SerivceID = ServiceID
        self.HomeOwnerID = HomeOwnerID
        self.Date = Date
        self.pullDetails()

    def pullDetails(self):
        query = """
                SELECT "ServiceID", "HomeOwnerID", "Price", "Date", "Rating"
                FROM "Matches"
                WHERE "ServiceID" = %s
                AND "HomeOwnerID" = %s
                AND "Date" = %s
                """
        params = (self.SerivceID, self.HomeOwnerID, self.Date)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.SerivceID = result[0]
            self.HomeOwnerID = result[1]
            self.Price = result[2]
            self.Date = result[3]
            self.Rating = result[4]
            print(f"Matches: Matches found")
            return

        print("Matches: Matches not found")
        raise Exception("Matches not found")

    def to_dict(self):
        return {
            'ServiecID': self.SerivceID,
            'HomeOwnerID': self.HomeOwnerID,
            'Price': self.Price,
            'Date': self.Date,
            'Rating': self.Rating
        }
