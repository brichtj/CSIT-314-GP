

from .User import User, data


#####Private Variables#####
# string username
# string userID
# string email
# string phone
# bool status
# bool valid
# bool modifiable_flag
class UserAdmin(User):
    IDPrefix = "UA"  # UserAdmin userID Prefix

    def pullDetail(self):
        super.pullDetail()  # calling pullDetail() from parent class

    def create_User(self):
        # calling createUser() from parent class
        super().create_User()
        data['AdminID'] += 1  # creating ID for new user
        ID = data['AdminID']
        ID = str(ID).zfill(9)
        self.userID = self.IDPrefix + ID  # at this layer ID will looks like UA000000001

        super.setUnmodifiable()
