from entity.User import User

# Cleaner::User
# int        CleanerID
# float      Experience
# bool       IsActive


class Cleaner(User):
    def __init__(self, row):
        super().__init__(row)
        self.Experience = row[6]
        self.CleanerID = self.UserID

    def to_dict(self):
        return {
            "CleanerID": self.CleanerID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive,
            "Experience": self.Experience
        }