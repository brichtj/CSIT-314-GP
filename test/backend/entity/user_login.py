class UserLogin:
    def __init__(self, profile, email, password):
        self.profile = profile
        self.email = email
        self.password = password

    def is_valid(self):
        return self.profile and self.email and self.password
