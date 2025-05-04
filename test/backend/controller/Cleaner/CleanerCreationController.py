from entity.Cleaner import Cleaner

class CleanerCreationController:
    def register(self, username, password, email, phone, experience):
        cleaner = Cleaner(
            username=username,
            email=email,
            phone=phone,
            Experience=experience,
            input_password=password
        )
        return cleaner.create_account()
