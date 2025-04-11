

from .User import User, data


class HomeOwner(User):
    IDPrefix = "HO"

    def __init__(self, username):
        super().__init__(username)

    def authenticate(self):
        try:
            super().authenticate()
            return self
        except Exception as e:
            raise Exception(e)

    def pullDetail(self):
        super.pullDetail()
        self.address = "SUN"

    def create_User(self, name, email, phone, add):
        super().create_User(name, email, phone)
        data['HomeOwnerID'] += 1
        ID = data['HomeOwnerID']
        ID = str(ID).zfill(9)
        self.userID = self.IDPrefix + ID
        self.address = add
