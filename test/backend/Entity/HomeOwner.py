from .User import User

class HomeOwner(User):
    def __init__(self, username, password, email, phone, address):
        super().__init__(username, password, email, phone, address)
        self.role = "homeowner"

    def __str__(self):
        return f"HomeOwner: {self.username}, Email: {self.email}"