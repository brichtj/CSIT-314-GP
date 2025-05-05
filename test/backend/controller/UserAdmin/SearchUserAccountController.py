from entity.UserAdmin import UserAdmin

class AdminSearchUserController:

    def adminSearchUserController(self,searchTerm):
        
        return UserAdmin().searchByUserID(searchTerm)
    