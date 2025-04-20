
# CategoryID
# Title
# Description


class Category:
    def __init__(self, CategoryID, Title, Description):
        self.CategoryID = CategoryID
        self.Title = Title
        self.Description = Description

    def to_dict(self) -> dict:
        return {
            "CategoryID": self.CategoryID,
            "Title": self.Title,
            "Description": self.Description
        }
