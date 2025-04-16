
# User:
# int        UserID
# varchar    Username
# int        UserProfile
# varchar    Email
# number     Phone
# varchar    Password
# bool       IsActive


class User:
    def __init__(self, UserID, Username, UserProfile, Email, Phone, IsActive):
        self.UserID = UserID
        self.Username = Username
        self.UserProfile = UserProfile
        self.Email = Email
        self.Phone = Phone
        self.IsActive = IsActive
    
    def __init__(self, row):
        self.UserID = row[0]
        self.Username = row[1]
        self.UserProfile = row[2]
        self.Email = row[3]
        self.Phone = row[4]
        self.IsActive = row[5]

    def to_dict(self):
        return {
            "UserID": self.UserID,
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
            "IsActive": self.IsActive
        }

    def getUserID(self):
        return self.UserID
    
    def getIsActive(self):
        return self.IsActive
