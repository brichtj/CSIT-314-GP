from entity.user_login import UserLogin
from entity.User import User
from entity.UserAdmin import UserAdmin
from entity.Cleaner import Cleaner
from entity.HomeOwner import HomeOwner
from entity.PlatformManagement import PlatformManagement

import json

UserProfile_DB_Entity_Map = {
    'Admin' : 'UserAdmin',
    'Cleaner' : 'Cleaner',
    'HomeOwner' : 'HomeOwner',
    'Manager' : 'PlatformManagement'
}

UserProfileID_UserProfile_Map = {
    0: 'Admin',
    1: 'Cleaner',
    2: 'HomeOwner',
    3: 'PlatformManagement'
}

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

    def login(self, UserProfileID, Email, Password):

        login_entity = UserLogin(UserProfileID_UserProfile_Map[UserProfileID], Email, Password)

        if not login_entity.is_valid():
            return {'success': False, 'error': 'Missing email or password'}

        row = self.login_gateway.authenticate(UserProfileID_UserProfile_Map[UserProfileID], Email, Password)

        if row:
            user_role = UserProfile_DB_Entity_Map[row[0]]
            
            row = self.user_gateway.getUserDetail(UserProfile_DB_Entity_Map[row[0]],row[1])

            if row:
                userClass = user_classes[user_role]
                temp_list = list(row)
                temp_list[2] = UserProfile_DB_Entity_Map[row[2]]
                row = tuple(temp_list)
                user = userClass(row)
                print(user.to_dict())
                if user.getIsActive():
                    return {'success': True, 'user': user}
                return {'success': False, 'error': 'User suspended'}
        
        return {'success': False, 'error': 'Invalid credentials'}
