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

class ViewUserController:

    def viewUserController(self,username):
        
        return UserAdmin().viewUser(username)


    