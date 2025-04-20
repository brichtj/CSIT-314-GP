
# ServiecID
# HomeOwnerID
# Price
# Date
# Rating


class Matches:
    def __init__(self, ServiceID, HomeOwnerID, Price, Date, Rating):
        self.ServiceID = ServiceID
        self.HomeOwnerID = HomeOwnerID
        self.Price = Price
        self.Date = Date
        self.Rating = Rating

    def to_dict(self) -> dict:
        return {
            'ServiecID': self.ServiceID,
            'HomeOwnerID': self.HomeOwnerID,
            'Price': self.Price,
            'Date': self.Date,
            'Rating': self.Rating
        }
