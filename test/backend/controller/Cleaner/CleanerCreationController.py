from entity.Cleaner import Cleaner

class CleanerCreationController:

    def CleanerCreationController(self,username,email,phone,experience):
        cleaner = Cleaner(username, email,phone,experience)
        return cleaner.createUser()
    