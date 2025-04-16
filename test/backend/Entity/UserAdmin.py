from entity.User import User

# Admin::User
# int        AdminID


class UserAdmin(User):
    def __init__(self, row):
        super().__init__(row)
        self.AdminID = self.UserID

    def to_dict(self):
        return {
            "AdminID": self.AdminID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive
        }