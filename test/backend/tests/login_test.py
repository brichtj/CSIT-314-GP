import json
import unittest

from Boundary.User.UserBoundary import login

#IMPORTANT NOTE, to run this, make sure your working directory is backend, then run python -m tests.login_test
#because you need to run this unittest file as a module, you need an empty __init__.py file in tests folder, 
# otherwise python thinks tests folder is the only working directory and cannot import from boundary folder

class DummyRequest:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class TestLoginFunction(unittest.TestCase):
    def test_valid_credentials_Cleaner(self):
        # Arrange
        username = 'sjordan'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message']['UserProfile'],1)
    def test_valid_credentials_HomeOwner(self):
        # Arrange
        username = 'jeffrey86'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message']['UserProfile'],2)
    def test_valid_credentials_UserAdmin(self):
        # Arrange
        username = 'wadecolleen'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message']['UserProfile'],3)
    def test_valid_credentials_PlatformManagement(self):
        # Arrange
        username = 'agraham'
        password = '123'
        expected_result = True
        #make dictionary object
        data = DummyRequest(username=username, password=password)

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message']['UserProfile'],4)
        

    def test_suspended_user(self):
        # Arrange
        username = 'suspendedUsername'
        password = '123'
        data = DummyRequest(username=username, password=password)
        expected_result = False
        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message'], 'User suspended')
        
        
    def test_non_existent_user(self):
        # Arrange
        username = 'ThisUsernameIsNotReal'
        password = 'wrong_password'
        data = DummyRequest(username=username, password=password)
        expected_result = False

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message'], "User does not exist")

    def test_invalid_credentials(self):
        # Arrange
        username = 'sjordan'
        password = 'wrong_password'
        data = DummyRequest(username=username, password=password)
        expected_result = False

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message'], "Password false")

    def test_user_profile_suspended(self):
        # Arrange
        username = 'SuspendedUserProfile'
        password = '123'
        data = DummyRequest(username=username, password=password)
        expected_result = False

        # Act
        response = login(data)
        response_body = json.loads(response.body.decode())
        # Assert
        self.assertEqual(response_body['success'], expected_result)
        self.assertEqual(response_body['message'], "User profile suspended")

if __name__ == '__main__':
    unittest.main(verbosity=2)