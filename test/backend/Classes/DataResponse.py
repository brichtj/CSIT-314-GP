from Classes.Response import Response


class DataResponse(Response):
    def __init__(self, success, message, data):
        super().__init__(success, message)
        self.data = data

    def to_json(self):
        # Call the base class's to_json and add the user attribute
        base_json = super().to_json()  # Get the base Response JSON
        base_json["data"] = self.data  # Add user to the JSON
        return base_json
