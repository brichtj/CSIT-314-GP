class UserLogin:
    def __init__(self, UserProfile, Email, Password):
        self.UserProfile = UserProfile
        self.Email = Email
        self.Password = Password

    def is_valid(self):
        return self.UserProfile and self.Email and self.Password
