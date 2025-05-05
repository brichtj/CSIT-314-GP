from entity.UserAdmin import UserAdmin

class ViewUserProfileController:

    def viewUserProfileController(self,name):
        
        return UserAdmin().viewUserProfile(name)
    