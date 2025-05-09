from entity.User import User


class UserLoginController:
    def login(self,Username, Password):
        return User().login(Username, Password)
