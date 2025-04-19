

from .User import User, data


#####Private Variables#####
# string username
# string userID
# string email
# string phone
# bool status
# bool valid
# bool modifiable_flag
class Cleaner(User):
    IDPrefix = "C"

    def pullDetail(self):
        super.pullDetail()

    def create_User(self):
        super().create_User()
        data['CleanerID'] += 1
        ID = data['CleanerID']
        ID = str(ID).zfill(9)
        self.userID = self.IDPrefix + ID

        super.setUnmodifiable()
