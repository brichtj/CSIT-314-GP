

from .User import User, data


class UserAdmin(User):
    IDPrefix = "UA"  # UserAdmin userID Prefix

    def __init__(self, username):
        super().__init__(username)  # calling constructor from parent class

    def authenticate(self):
        try:
            super().authenticate()  # calling authenticate() form parent class
            return self
        except Exception as e:
            raise Exception(e)

    def pullDetail(self):
        super.pullDetail()  # calling pullDetail() from parent class

    def create_User(self, name, email, phone):
        # calling createUser() from parent class
        super().create_User(name, email, phone)
        data['AdminID'] += 1  # creating ID for new user
        ID = data['AdminID']
        ID = str(ID).zfill(9)
        self.userID = self.IDPrefix + ID  # at this layer ID will looks like UA000000001
