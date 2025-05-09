from entity.UserProfile import UserProfile

class ViewUserProfileController():
    def viewUserProfileController(self,UserProfileID:int):
        return UserProfile.viewUserProfile(UserProfileID)
class UpdateUserProfileController:

    def updateUserProfileController(self,name:str,privilege:str,is_active:bool,userprofileID:int):
        
        return UserProfile.updateUserProfile(name,privilege,is_active,userprofileID)


class SuspendUserProfileController:

    def suspendUserProfileController(self,userProfileID:int):
        
        return UserProfile.suspendUserProfile(userProfileID)
    
class SearchUserProfileController:

    def searchUserProfileController(self,name)->list[UserProfile]:
        
        return UserProfile.searchUserProfile(name)