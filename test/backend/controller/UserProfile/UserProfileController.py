from entity.UserProfile import UserProfile

class ViewUserProfileController():
    def viewUserProfileController(self,UserProfileID:int):
        return UserProfile.viewUserProfile(UserProfileID)