from app.entity.User import User, get_db_connection

# Admin::User
# int        AdminID


class UserAdmin(User):
    @classmethod
    def from_user(cls, user):
        print(f"{user.Email}: Downcasting User -> UserAdmin")
        return cls(user.Email, user.Password)

    def to_dict(self):
        return {
            "AdminID": self.UserID,
            **super().to_dict()
        }
