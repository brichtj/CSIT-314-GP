from entity.user_login import UserLogin
from entity.User import User
from entity.UserAdmin import UserAdmin
from entity.Cleaner import Cleaner
from entity.HomeOwner import HomeOwner
from entity.PlatformManagement import PlatformManagement


import json

# funtion name to used for different mode
user_classes = {
    'UserAdmin': UserAdmin,
    'Cleaner': Cleaner,
    'HomeOwner': HomeOwner,
    'PlatformManagement': PlatformManagement
}

class UserLoginController:
    def __init__(self, login_gateway, user_gateway):
        self.login_gateway = login_gateway
        self.user_gateway = user_gateway

    def login(self, profile, email, password):
        login_entity = UserLogin(profile, email, password)

        if not login_entity.is_valid():
            return {'success': False, 'error': 'Missing email or password'}

        row = self.login_gateway.authenticate(profile, email, password)

        if row:
            user_role = row[2]
            userClass = user_classes[user_role]
            user = userClass(row[0], row[1], row[2], row[3], row[4], row[5])
            
            if type(user).__name__ == 'HomeOwner':
                row = self.user_gateway.getAddress(user.getUserID())
                user.setAddress(row[0])
            
            return {'success': True, 'user': user}
        
        return {'success': False, 'error': 'Invalid credentials'}
    

