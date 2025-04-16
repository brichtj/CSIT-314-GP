from entity.User import User

# HomeOwner::UUser
# int        HomeOwnerID
# varchar    Address


class HomeOwner(User):
    def __init__(self, row):
        super().__init__(row)
        self.Address = row[6]
        self.HomeOwnerID = self.UserID

    def setAddress(self, Address):
        self.Address = Address

    def to_dict(self):
        return {
            "HomeOwnerID": self.HomeOwnerID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive,
            "address": self.Address
        }
