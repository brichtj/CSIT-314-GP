from entity.UserAdmin import UserAdmin

class SuspendUserController:

    def suspendUserController(self,username):
        
        return UserAdmin().suspendUser(username)
    