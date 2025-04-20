class Response:
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message

    def __repr__(self):
        return f"Response(success={self.success}, message={self.message!r})"

    def __str__(self):
        return f"Success: {self.success}, Message: {self.message}"
