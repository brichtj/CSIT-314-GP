from .User import User

class PlatformManager(User):
    def __init__(self, username, password, email, phone, address):
        super().__init__(username, password, email, phone, address)
        self.role = "platform_manager"

    def __str__(self):
        return f"Platform Manager: {self.username}, Email: {self.email}"