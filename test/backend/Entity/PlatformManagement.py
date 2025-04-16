from entity.User import User

# PlatformManagement::User
# int        ManagerID


class PlatformManagement(User):
    def __init__(self, row):
        super().__init__(row)
        self.ManagerID = self.UserID

    def to_dict(self):
        return {
            "ManagerID": self.ManagerID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive
        }