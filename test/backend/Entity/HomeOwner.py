

from .User import User, data


#####Private Variables#####
# string username
# string userID
# string email
# string phone
# bool status
# string address
# bool valid
# bool modifiable_flag
class HomeOwner(User):
    IDPrefix = "HO"

    def pullDetail(self):
        super.pullDetail()
        self.address = "SUN"

    def setAddress(self, add:str):
        if not self.modifiable_flag:
            raise Exception ("Unauthorize access to modify user details")
        
        if not add or add is None:
            raise Exception("missing address data when setting address")
        
        self.address = add

    def create_User(self):
        super().create_User()
        data['HomeOwnerID'] += 1
        ID = data['HomeOwnerID']
        ID = str(ID).zfill(9)
        self.userID = self.IDPrefix + ID

        super.setUnmodifiable()
