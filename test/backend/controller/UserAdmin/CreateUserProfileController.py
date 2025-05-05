from entity.UserAdmin import UserAdmin

class UserProfileCreateController:

    def createUserProfile(self,name,privilege):
        
        return UserAdmin().createUserProfile(name,privilege)
    