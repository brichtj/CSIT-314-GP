from entity.User import User


class HomeOwner(User):
    def __init__(self, userid, username, userprofile, email, phone, dob):
        super().__init__(userid, username, userprofile, email, phone, dob)

    def setAddress(self, address):
        self.address = address

    def to_dict(self):
        return {
            **super().to_dict(),
            "address": self.address
        }
