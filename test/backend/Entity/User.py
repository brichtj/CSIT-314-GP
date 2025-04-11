

from .mockdb import mock_user_db        # using a mock database
import os
import json

base_dir = os.path.dirname(os.path.abspath(
    __file__))       # locate project path
# locate Data Folder
folder_path = os.path.join(base_dir, 'Data')
file_path = os.path.join(folder_path, 'data.json')          # locate data.json

# allow python to makedir if path not exist
os.makedirs(folder_path, exist_ok=True)

# loading json for static value(e.g UserID)
try:
    with open(file_path, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

# get user IDs
data['AdminID'] = data.get('AdminID', 0)
data['CleanerID'] = data.get('CleanerID', 0)
data['HomeOwnerID'] = data.get('HomeOwnerID', 0)
data['PlatformManagementID'] = data.get('PlatformManagementID', 0)

# funtion to save JSON


def saveJSON():
    with open(file_path, 'w') as f:         # set to write mode
        json.dump(data, f, indent=4)


# executed once to make user JSON always created(delete JSON to reset all data)
saveJSON()

# User class


class User:
    valid = False

    # constructor
    def __init__(self, username):
        self.username = username

    # Used for login
    def authenticate(self, password):
        if self.username in mock_user_db:
            if password == mock_user_db[self.username]:
                self.valid = True
                return
            raise Exception("Incorrect password!")

        raise Exception("Incorrect Username!")

    # User object shouldn't have any details before logging in(authenticate)
    def pullDetail(self):
        if not self.valid:
            raise Exception("Invalid User! User authenticate() bypassed!")

        # need to be change after database is complete
        self.userID = "001"
        self.name = ":D"
        self.email = "XXX@yahoo.com"
        self.phone = "88888888"
        self.status = True  # True for active, False for suspended

    # For Creating User(Not User_Admin Create User)
    def create_User(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.status = True
