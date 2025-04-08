from mockdb import mock_user_db

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        if self.username in mock_user_db and self.password == mock_user_db[self.username]:
            return
        
        raise Exception("Authentication Failed")
    
    def pullDetail(self):
        #need to be change after database is complete
        userID = "001" #most likely PK
        name = ":D"
        email = "@yahoo.com"
        phone = "88888888"
        status = True     #True for active, False for suspended


class UserAdmin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def authenticate(self):
        try:
            super().authenticate()
            self.pullDetail()
            return self
        except Exception as e:
            raise Exception(e)

    def pullDetail(self):
        #need to be change after database is complete
        #super.pullDetail() #can use super class method to pull common detail
        userID = "Admin001" #most likely PK
        name = "Admin:D"
        email = "admin001@yahoo.com"
        phone = "88888888"
        status = True     #True for active, False for suspended

class Cleaner(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def authenticate(self):
        try:
            super().authenticate()
            self.pullDetail()
            return self
        except Exception as e:
            raise Exception(e)
        
    def pullDetail(self):
        #need to be change after database is complete
        #super.pullDetail() #can use super class method to pull common detail
        userID = "Cleaner001" #most likely PK
        name = "Cleaner:D"
        email = "clenaer001@yahoo.com"
        phone = "88888887"
        status = True     #True for active, False for suspended
        history_record = "cleaner_history001" #may be a separated table to store history indentify with RecordID
        #Or maybe this approach:
        # CREATE TABLE user_history (
        #     history_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique history record ID
        #     user_id INT,  -- Foreign key to the user table
        #     action_type VARCHAR(100),  -- Type of action (e.g., 'cleaning booked', 'payment made')
        #     description TEXT,  -- A detailed description of the action
        #     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- When the action occurred
        #     FOREIGN KEY (user_id) REFERENCES user(user_id)  -- Link to the user table
        # );

class HomeOwner(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def authenticate(self):
        try:
            super().authenticate()
            self.pullDetail()
            return self
        except Exception as e:
            raise Exception(e)
        
    def pullDetail(self):
        #need to be change after database is complete
        #super.pullDetail() #can use super class method to pull common detail
        userID = "Cleaner001" #most likely PK
        name = "Cleaner:D"
        email = "clenaer001@yahoo.com"
        phone = "88888887"
        status = True     #True for active, False for suspended
        address = "SUN"
        history_record = "homeowner_history001"
        shortlist = "shortlist001"

class PlatfromManagement(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def authenticate(self):
        try:
            super().authenticate()
            self.pullDetail()
            return self
        except Exception as e:
            raise Exception(e)
        
    def pullDetail(self):
        #need to be change after database is complete
        #super.pullDetail() #can use super class method to pull common detail
        userID = "Cleaner001" #most likely PK
        name = "Cleaner:D"
        email = "clenaer001@yahoo.com"
        phone = "88888887"
        status = True     #True for active, False for suspended