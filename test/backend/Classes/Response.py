

class Response():
    def __init__(self, succcess,  message):
        self.success = succcess
        self.message = message

    def __rper__(self):
        return f'Response(success = {self.success}, message = {self.message})'

    def __str__(self):
        return f'success = {self.success}, message = {self.message}'
