from app.entity.User import User
from app.db import DB

# HomeOwner::UUser
# int        HomeOwnerID
# varchar    Address


class HomeOwner(User):
    @classmethod
    def from_user(cls, user) -> User:
        print(f"{user.Email}: Downcasting User -> HomeOwner")
        try:
            return cls(user.Email, user.Password)
        except Exception as e:
            print(f"{user.Email}: failed to Downcast User")
            return user

    def pullDetails(self):
        super().pullDetails()
        query = """
                SELECT "Address"
                FROM "HomeOwner"
                WHERE "HomeOwnerID" = %s"""
        params = (self.UserID,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.Address = result[0]
            print(f"{self.Email}: HomeOwner Address pulled")
            return

        print(f"{self.Email}: Failed to pull HomeOwner Address")
        raise Exception("Failed to pull HomeOwner Address")

    def to_dict(self) -> dict:
        return {
            "HomeOwnerID": self.UserID,
            **super().to_dict(),
            "Address": self.Address
        }
