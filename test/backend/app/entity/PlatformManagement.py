from app.entity.User import User

# PlatformManagement::User
# int        ManagerID


class PlatformManagement(User):
    @classmethod
    def from_user(cls, user):
        return cls(user.Email, user.Password)

    def to_dict(self):
        return {
            "ManagerID": self.UserID,
            **super().to_dict()
        }
