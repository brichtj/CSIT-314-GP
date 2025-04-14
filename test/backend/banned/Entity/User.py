

import os
import json


base_dir = os.path.dirname(os.path.abspath(
    __file__))       # locate project path
# locate Data Folder
folder_path = os.path.join(base_dir, 'Data')
data_path = os.path.join(folder_path, 'data.json')          # locate data.json
login_detail_db_path = os.path.join(
    folder_path, 'mock_login_detail_db')       # a JSON use to mock db

# allow python to makedir if path not exist
os.makedirs(folder_path, exist_ok=True)

# loading json for static value(e.g UserID)
try:
    with open(data_path, 'r') as f:
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
    with open(data_path, 'w') as f:         # set to write mode
        json.dump(data, f, indent=4)


# executed once to make user JSON always created(delete JSON to reset all data)
saveJSON()


def readFile(file):
    try:
        with open(file, 'r') as f:
            db = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: The file {file} contains invalid JSON.")
        db = []
    except FileNotFoundError:
        db = []

    return db


def writeFile(file, dataIn):
    try:
        with open(file, 'w') as f:
            json.dump(dataIn, f, indent=4)
    except IOError as e:
        print(f"Error writing to file {file}: {e}")


# User class
##### Private Variables#####
# for security purposes, password wont be store in User object
# string username
# string userID
# string email
# string phone
# bool status
# bool valid
# bool modifiable_flag
class User:
    valid = False
    modifiable_flag = False

    # constructor
    def __init__(self, email: str):
        self.email = email

    # Used for login
    def authenticate(self, password: str):
        # if self.email in mock_user_db:
        #     if password == mock_user_db[self.email]:
        #         self.valid = True
        #         return
        #     raise Exception("Incorrect password!")

        raise Exception("Incorrect Username!")

    # User object shouldn't have any details before logging in(authenticate)
    def pullDetail(self):
        if not self.valid:
            raise Exception("Invalid User! User authenticate() bypassed!")

        # need to be change after database is complete
        self.userID = "001"
        self.email = "XXX@yahoo.com"
        self.phone = "88888888"
        self.status = True  # True for active, False for suspended

    def login(self, password: str):
        self.authenticate(password)
        self.pullDetail()

    def setModifiable(self):
        self.modifiable_flag = True  # need to call this funtion before changing any details

    def setUnmodifiable(self):
        self.modifiable_flag = False  # set the object to unmodifiale after editing

    def setUsername(self, username: str):
        if not self.modifiable_flag:
            raise Exception("Unauthorize access to modify user details")

        self.username = username

    def setPassword(self, password):
        if not self.modifiable_flag:
            raise Exception("Unauthorize access to modify user details")

        row = {
            "email": self.email,
            "password": password
        }

        db = readFile(login_detail_db_path)
        db.append(row)
        writeFile(login_detail_db_path, db)

    def setEmail(self, email: str):
        if not self.modifiable_flag:
            raise Exception("Unauthorize access to modify user details")

        self.email = email

    def setPhone(self, phone: str):
        if not self.modifiable_flag:
            raise Exception("Unauthorize access to modify user details")

        self.phone = phone

    def setStatus(self, status=False):
        if not self.modifiable_flag:
            raise Exception("Unauthorize access to modify user details")

        self.status = status

    # For Creating User(Not User_Admin Create User)
    def create_User(self, username, email, phone, password):
        self.setModifiable()
        self.setUsername(username)
        self.setEmail(email)
        self.setPhone(phone)
        self.setStatus(True)
        self.setPassword(password)
        # need to add a funtion that directly deal with database to store password


def debug():
    user = User("test")
    user.setModifiable()
    user.setPassword("test123")


if __name__ == "__main__":
    debug()
