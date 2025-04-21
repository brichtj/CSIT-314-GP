from app.entity.User import User
from app.db import DB

# Cleaner::User
# int        CleanerID
# float      Experience
# bool       IsActive


class Cleaner(User):
    @classmethod
    def from_user(cls, user) -> User:
        print(f"{user.Email}: Downcasting User -> Cleaner:")
        try:
            return cls(user.Email, user.Password)
        except Exception as e:
            print(f"{user.Email}: failed to Downcast User")
            return user

    def pullDetails(self):
        super().pullDetails()
        query = """
                SELECT "Experience"
                FROM "Cleaner"
                WHERE "CleanerID" = %s"""
        params = (self.UserID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.Experience = result[0]
            print(f"{self.Email}: Cleaner Experience pulled")
            return
        
        print(f"{self.Email}: Failed to pull Cleaner Experience")
        raise Exception("Failed to pull Cleaner Expreience")

    def to_dict(self) -> dict:
        return {
            "CleanerID": self.UserID,
            **super().to_dict(),
            "Experience": self.Experience
        }
