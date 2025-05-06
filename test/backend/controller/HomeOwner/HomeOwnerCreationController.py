from entity.HomeOwner import HomeOwner

class HomeOwnerCreationController:

    def HomeOwnerCreationController(self,username,email,phone,address):
        homeOwner = HomeOwner(username, email,phone,address)
        return homeOwner.createUser()
    