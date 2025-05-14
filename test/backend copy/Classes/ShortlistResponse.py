from Classes.Response import Response


class ShortlistResponse(Response):
    def __init__(self, success, message, shortlist):
        super().__init__(success, message)
        self.shortlist = shortlist

    def to_json(self):
        # Call the base class's to_json and add the user attribute
        base_json = super().to_json()  # Get the base Response JSON
        base_json["shortlist"] = self.shortlist  # Add user to the JSON
        return base_json
