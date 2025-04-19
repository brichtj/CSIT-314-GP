from app.entity.User import User, get_db_connection

# Cleaner::User
# int        CleanerID
# float      Experience
# bool       IsActive


class Cleaner(User):
    @classmethod
    def from_user(cls, user):
        print(f"{user.Email}: Downcasting User -> Cleaner:")
        return cls(user.Email, user.Password)

    def pullDetails(self):
        super().pullDetails()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    SELECT "Experience"
                    FROM "Cleaner"
                    WHERE "CleanerID" = %s""",
                    (self.UserID,)
                    )
        row = cur.fetchone()
        conn.close()

        if row:
            self.Experience = row[0]
            print(f"{self.Email}: Cleaner Experience pulled")
        else:
            print(f"{self.Email}: Failed to pull Cleaner Experience")

    def to_dict(self):
        return {
            "CleanerID": self.UserID,
            **super().to_dict(),
            "Experience": self.Experience
        }