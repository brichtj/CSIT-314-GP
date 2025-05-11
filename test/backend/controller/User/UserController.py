
from entity.User import User


class UserLoginController:
    def login(self,Username, Password):
        user = User(Username, Password)
        return user.login()

class CreateUserController:

    def CreateUserController(self,username:str,email:str,phone:str,experience:float,address:str,UserprofileID:int)->bool:
        
        return User.createUser(username, email,phone,  experience, address, UserprofileID)

    

class SearchUserController:

    def SearchUserController(self,searchTerm:str)->list[User]:
        
        return User.searchByUserName(searchTerm)


class SuspendUserController:

    def suspendUserController(self,UserID:int)->bool:
        
        return User.suspendUser(UserID)

class ViewUserController:

    def ViewUserController(self,UserID:int)->User:
        
        return User.viewUser(UserID)
class UpdateUserController:

    def updateUserController(self,username:str,email:str,phone:str,IsActive:bool,UserProfileID:int,address:str,experience:float,UserID:int)->bool:
        
        return User.updateUser(username,email,phone,IsActive,UserProfileID,address,experience,UserID)


    