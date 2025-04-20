from app.entity.User import User

# Admin::User
# int        AdminID


class UserAdmin(User):
    def to_dict(self) -> dict:
        return {
            "AdminID": self.UserID,
            **super().to_dict()
        }
