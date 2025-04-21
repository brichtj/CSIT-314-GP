from entity.User import User


class UserLoginController:
    def login(Username, Password):
        user = User(Username, Password)
        return user.login()
