
from entity.User import User

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

    def viewUserController(self,UserID:int)->User:
        
        return User.viewUser(UserID)


    