from entity.UserAdmin import UserAdmin

class UserCreationController:

    def UserCreationController(self,username, email,phone,  experience, address, userType):
        
        return UserAdmin().createUser(username, email,phone,  experience, address, userType)
    