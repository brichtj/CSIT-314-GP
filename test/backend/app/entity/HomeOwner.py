from app.entity.User import User, get_db_connection

# HomeOwner::UUser
# int        HomeOwnerID
# varchar    Address


class HomeOwner(User):
    @classmethod
    def from_user(cls, user):
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
            print(f"HomeOwner Address pulled: {self.Email}")
        else:
            print(f"Failed to pull HomeOwner Address: {self.Email}")

    def to_dict(self):
        return {
            "HomeOwnerID": self.UserID,
            **super().to_dict(),
            "Address": self.Address
        }