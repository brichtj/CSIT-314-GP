import bcrypt


# User:
# int        UserID
# varchar    Username
# int        UserProfile
# varchar    Email
# number     Phone
# varchar    Password
# bool       IsActive


class User:
    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password

    def checkPassword(self, input_password) -> bool:
        input_password_bytes = input_password.encode('utf-8')
        hash_password_bytes = self.Password.encode('utf-8')

        print(f"{self.Email}: Authenticating")
        return bcrypt.checkpw(input_password_bytes, hash_password_bytes)

    def setDetails(self, UserID, Username, UserProfile, Email, Phone, IsActive):
        if IsActive:
            self.UserID = UserID
            self.Username = Username
            self.UserProfile = UserProfile
            self.Email = Email
            self.Phone = Phone
        else:
            raise Exception('User Suspended')

    def to_dict(self) -> dict:
        return {
            "Username": self.Username,
            "UserProfile": self.UserProfile,
            "Email": self.Email,
            "Phone": self.Phone,
        }
