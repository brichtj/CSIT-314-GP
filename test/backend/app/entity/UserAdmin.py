from app.entity.User import User

# Admin::User
# int        AdminID


class UserAdmin(User):
    @classmethod
    def from_user(cls, user) -> User:
        print(f"{user.Email}: Downcasting User -> UserAdmin")
        try:
            return cls(user.Email, user.Password)
        except Exception as e:
            print(f"{user.Email}: failed to Downcast User")
            return user

    def to_dict(self) -> dict:
        return {
            "AdminID": self.UserID,
            **super().to_dict()
        }
