from entity.User import User


class Cleaner(User):
    def __init__(self, userid, username, userprofile, email, phone, dob):
        super().__init__(userid, username, userprofile, email, phone, dob)