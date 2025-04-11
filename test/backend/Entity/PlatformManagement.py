

from .User import User, data


class PlatformManagement(User):
    IDPrefix = "PM"

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

    def create_User(self, name, email, phone):
        super().create_User(name, email, phone)
        data['PlatformManagementID'] += 1
        ID = data['PlatformManagementID']
        ID = str(ID).zfill(9)
        self.userID = self.IDPrefix + ID
