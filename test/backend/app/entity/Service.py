from app.db import DB

# ServiceID
# CategoryID
# Title
# Description
# DatePosted
# CleanerID
# LikeCount
# ViewCount
# MatchCount
# Price


class Service:
    def __init__(self, ServiceID, CategoryID, Title, Description, DatePosted, CleanerID, LikeCount, ViewCount, MatchCount, Price):
        self.ServiceID = ServiceID
        self.CategoryID = CategoryID
        self.Title = Title
        self.Description = Description
        self.DatePosted = DatePosted
        self.CleanerID = CleanerID
        self.LikeCount = LikeCount
        self.ViewCount = ViewCount
        self.MatchCount = MatchCount
        self.Price = Price

    def to_dict(self) -> dict:
        return {
            "ServiceID": self.ServiceID,
            "CategoryID": self.CategoryID,
            "Title": self.Title,
            "Description": self.Description,
            "DatePosted": self.DatePosted,
            "CleanerID": self.CleanerID,
            "LikeCount": self.LikeCount,
            "ViewCount": self.ViewCount,
            "MatchCount": self.MatchCount,
            "Price": self.Price
        }