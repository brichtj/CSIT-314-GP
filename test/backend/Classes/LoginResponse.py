

from Classes.Response import Response


class LoginResponse(Response):
    def __init__(self, success, message, user):
        super().__init__(success, message)
        self.user = user

    def to_json(self):
        # Call the base class's to_json and add the user attribute
        base_json = super().to_json()  # Get the base Response JSON
        base_json["user"] = self.user  # Add user to the JSON
        return base_json
