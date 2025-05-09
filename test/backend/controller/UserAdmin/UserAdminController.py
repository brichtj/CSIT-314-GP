from entity.UserAdmin import UserAdmin

class UserCreationController:

    def UserCreationController(self,username, email,phone,  experience, address, userType):
        
        return UserAdmin().createUser(username, email,phone,  experience, address, userType)

    

class AdminSearchUserController:

    def adminSearchUserController(self,searchTerm):
        
        return UserAdmin().searchByUserName(searchTerm)


class SuspendUserController:

    def suspendUserController(self,username):
        
        return UserAdmin().suspendUser(username)

class ViewUserController:

    def viewUserController(self,username):
        
        return UserAdmin().viewUser(username)


    