from Classes.Response import Response


class ServiceResponse(Response):
    def __init__(self, success, message, service):
        super().__init__(success, message)
        self.service = service

    def to_json(self):
        # Call the base class's to_json and add the user attribute
        base_json = super().to_json()  # Get the base Response JSON
        base_json["service"] = self.service  # Add user to the JSON
        return base_json
