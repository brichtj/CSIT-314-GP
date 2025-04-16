# login_module.py (you can name this file anything)

# Mock DB access function
def get_user_by_email(username):
    # Simulate a DB lookup
    mock_db = {
        "adm": {
            "username": "adm",
            "email": "alice@example.com",
            "password": "123"
        }
    }
    return mock_db.get(username)


# ENTITY + CONTROLLER in one file

#entity
class UserLogin:
    #define structure that will be returned from postgres here in the __init__
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password = password

    @classmethod
    def from_db(cls, username):
        data = get_user_by_email(username)
        if data:
            return cls(data["username"], data["email"], data["password"])
        return None

    def check_password(self, input_password):
        return self._password == input_password
    #to convert to a json format
    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email
            # Don't return password in response for security reasons
        }


#controller
def login_controller(username, password):
    print('hello')
    user = UserLogin.from_db(username)
    if not user or not user.check_password(password):
        return {"error": "Invalid login"}
    return user.to_dict()
