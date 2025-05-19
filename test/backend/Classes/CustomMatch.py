
from datetime import datetime


class CustomMatch():#to return the full service object with all joined values
    def __init__(self,ServiceID:int,CategoryID:int,Title:str,Description:str,DatePosted:datetime,CleanerID:int,LikeCount:int,ViewCount:int,MatchCount:int,price:float,ImageLink:str,CatTitle:str,CatDesc:str,CatActive:bool,CleanerName:str,Email:str,Phone:str,UActive:str,Experience:float,Address:str,HomeOwnerName:str,DealPrice:float,DealDate:datetime) -> None:
        self.ServiceID = ServiceID
        self.CategoryID = CategoryID
        self.Title = Title
        self.Description = Description
        self.DatePosted = DatePosted
        self.CleanerID = CleanerID
        self.LikeCount = LikeCount
        self.ViewCount = ViewCount
        self.MatchCount = MatchCount
        self.price = price
        self.ImageLink = ImageLink
        self.CatTitle = CatTitle
        self.CatDesc = CatDesc
        self.CatActive = CatActive
        self.CleanerName = CleanerName
        self.Email = Email
        self.Phone = Phone
        self.UActive = UActive
        self.Experience = Experience
        self.Address = Address
        self.HomeOwnerName = HomeOwnerName
        self.DealPrice = DealPrice
        self.DealDate = DealDate
        
    def to_json(self):
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
            "Price": float(self.price),
            "ImageLink": self.ImageLink,
            "CatTitle": self.CatTitle,
            "CatDesc": self.CatDesc,
            "CatActive": self.CatActive,
            "CleanerName": self.CleanerName,
            "Email": self.Email,
            "Phone": self.Phone,
            "UActive": self.UActive,
            "Experience": float(self.Experience),
            "Address": self.Address,
            "HomeOwnerName": self.HomeOwnerName,
            "DealPrice": float(self.DealPrice),
            "DealDate": self.DealDate
        }