

from Classes.Response import Response
class LoginResponse(Response):
    def __init__(self, success, message, user):
        super().__init__(success, message)
        self.user = user
