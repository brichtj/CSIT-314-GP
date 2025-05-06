from entity.UserAdmin import UserAdmin

class ViewUserController:

    def viewUserController(self,username):
        
        return UserAdmin().viewUser(username)
    