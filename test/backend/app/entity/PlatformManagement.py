from app.entity.User import User

# PlatformManagement::User
# int        ManagerID


class PlatformManagement(User):
    def to_dict(self) -> dict:
        return {
            "ManagerID": self.UserID,
            **super().to_dict()
        }
