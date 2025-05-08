from entity.UserProfile import UserProfile

class ViewUserProfileController():
    def viewUserProfileController(self,name:str):
        return UserProfile.viewUserProfile(name)