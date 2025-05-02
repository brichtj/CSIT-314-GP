

from Classes.Response import Response


class MatchesResponse(Response):
    def __init__(self, success, message, matches):
        super().__init__(success, message)
        self.matches = matches

    def to_json(self):
        # Call the base class's to_json and add the user attribute
        base_json = super().to_json()  # Get the base Response JSON
        base_json["matches"] = self.matches  # Add user to the JSON
        return base_json
