

from Classes.Response import Response


class CategoryResponse(Response):
    def __init__(self, success, message, category):
        super().__init__(success, message)
        self.category = category

    def to_json(self):
        # Call the base class's to_json and add the user attribute
        base_json = super().to_json()  # Get the base Response JSON
        base_json["category"] = self.category  # Add user to the JSON
        return base_json
