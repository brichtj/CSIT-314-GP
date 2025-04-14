class User:
    def __init__(self, userid, username, userprofile, email, phone, dob):
        self.userid = userid
        self.username = username
        self.userprofile = userprofile
        self.email = email
        self.phone = phone
        self.dob = dob

    def getUserID(self):
        return self.userid