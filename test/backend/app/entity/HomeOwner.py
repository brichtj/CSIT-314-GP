from app.entity.User import User

# HomeOwner::UUser
# int        HomeOwnerID
# varchar    Address


class HomeOwner(User):
    def setAddress(self, Address):
        self.Address = Address

    def to_dict(self) -> dict:
        return {
            "HomeOwnerID": self.UserID,
            **super().to_dict(),
            "Address": self.Address
        }
