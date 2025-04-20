from app.entity.User import User

# PlatformManagement::User
# int        ManagerID


class PlatformManagement(User):
    @classmethod
    def from_user(cls, user) -> User:
        print(f"{user.Email}: Downcasting User -> PlatformManagement")
        try:
            return cls(user.Email, user.Password)
        except Exception as e:
            print(f"{user.Email}: failed to Downcast User")
            return user

    def to_dict(self) -> dict:
        return {
            "ManagerID": self.UserID,
            **super().to_dict()
        }
