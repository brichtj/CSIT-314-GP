from app.entity.User import User

# Cleaner::User
# int        CleanerID
# float      Experience
# bool       IsActive


class Cleaner(User):
    def setExperience(self, Experience):
        self.Experience = Experience

    def to_dict(self) -> dict:
        return {
            "CleanerID": self.UserID,
            **super().to_dict(),
            "Experience": self.Experience
        }
