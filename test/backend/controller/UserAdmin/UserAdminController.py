from entity.UserAdmin import UserAdmin

class UserCreationController:

    def UserCreationController(self,username, email,phone,  experience, address, userType):
        
        return UserAdmin().createUser(username, email,phone,  experience, address, userType)


class UserProfileCreateController:

    def createUserProfile(self,name,privilege):
        
        return UserAdmin().createUserProfile(name,privilege)
    

class AdminSearchUserController:

    def adminSearchUserController(self,searchTerm):
        
        return UserAdmin().searchByUserName(searchTerm)


class SuspendUserController:

    def suspendUserController(self,username):
        
        return UserAdmin().suspendUser(username)
class UpdateUserProfileController:

    def updateUserProfileController(self,name:str,privilege:str,is_active:bool,userprofileID:int):
        
        return UserAdmin().updateUserProfile(name,privilege,is_active,userprofileID)


class ViewUserController:

    def viewUserController(self,username):
        
        return UserAdmin().viewUser(username)


class ViewUserProfileController:

    def viewUserProfileController(self,name):
        
        return UserAdmin().viewUserProfile(name)

class SuspendUserProfileController:

    def suspendUserProfileController(self,name):
        
        return UserAdmin().suspendUserProfile(name)
    
class SearchUserProfileController:

    def searchUserProfileController(self,name):
        
        return UserAdmin().searchUserProfile(name)
    