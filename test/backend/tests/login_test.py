import json
import unittest

from Boundary.User.UserBoundary import login

#IMPORTANT NOTE, to run this, make sure your working directory is backend, then run python -m tests.login_test
#because you need to run this as a module, you need an empty __init__.py file in tests folder, otherwise python thinks tests folder is the only working directory and cannot import from boundary folder

class DummyRequest:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class TestLoginFunction(unittest.TestCase):
    def test_valid_credentials_Cleaner(self):
        # Arrange
        username = 'cleaner'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
    def test_valid_credentials_HomeOwner(self):
        # Arrange
        username = 'homeowner'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
    def test_valid_credentials_UserAdmin(self):
        # Arrange
        username = 'homeowner'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
    def test_valid_credentials_PlatformManagement(self):
        # Arrange
        username = 'homeowner'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        

    def test_invalid_credentials(self):
        # Arrange
        username = 'test_user'
        password = 'wrong_password'
        data = DummyRequest(username=username, password=password)
        expected_result = False

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())

        # Assert
        self.assertEqual(response_body['success'], expected_result)

if __name__ == '__main__':
    unittest.main()