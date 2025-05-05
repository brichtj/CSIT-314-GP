from entity.User import User

class AdminSearchUserController:

    def adminSearchUserController(self,searchTerm):
        
        return User().searchByUserID(searchTerm,'admin')
    