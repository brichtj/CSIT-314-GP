
from datetime import datetime


class SimpleMatch():#to return the full service object with all joined values
    def __init__(self,ServiceID:int,Title:str,Price:float,ImageLink:str,MatchID:int,DealPrice:float,DealDate:datetime) -> None:
        self.ServiceID = ServiceID
        self.Title = Title
        self.Price = Price
        self.ImageLink = ImageLink
        self.MatchID = MatchID
        self.DealPrice = DealPrice
        self.DealDate = DealDate
    def to_json(self):
        return {
            "ServiceID": self.ServiceID,
            "Title": self.Title,
            "Price": float(self.Price),
            "ImageLink": self.ImageLink,
            "MatchID": self.MatchID,
            "DealPrice": float(self.DealPrice),
            "DealDate": self.DealDate
        }