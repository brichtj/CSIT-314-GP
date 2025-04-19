from app.entity.User import User, get_db_connection

# HomeOwner::UUser
# int        HomeOwnerID
# varchar    Address


class HomeOwner(User):
    @classmethod
    def from_user(cls, user):
        print(f"{user.Email}: Downcasting User -> HomeOwner")
        return cls(user.Email, user.Password)

    def pullDetails(self):
        super().pullDetails()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT "Address"
                    FROM "HomeOwner"
                    WHERE "HomeOwnerID" = %s""",
                    (self.UserID,)
                    )
        row = cur.fetchone()
        conn.close()

        if row:
            self.Address = row[0]
            print(f"{self.Email}: HomeOwner Address pulled")
        else:
            print(f"{self.Email}: Failed to pull HomeOwner Address")

    def to_dict(self):
        return {
            "HomeOwnerID": self.UserID,
            **super().to_dict(),
            "Address": self.Address
        }