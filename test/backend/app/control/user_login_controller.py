from app.entity.User import User
from app.entity.UserAdmin import UserAdmin
from app.entity.Cleaner import Cleaner
from app.entity.HomeOwner import HomeOwner
from app.entity.PlatformManagement import PlatformManagement

# Translate naming in DB to naming as entity
UserProfile_DB_Entity_Map = {
    'Admin': 'UserAdmin',
    'Cleaner': 'Cleaner',
    'HomeOwner': 'HomeOwner',
    'Manager': 'PlatformManagement'
}

# Translate ID to naming used in DB
UserProfileID_DB_Map = {
    0: 'Admin',
    1: 'Cleaner',
    2: 'HomeOwner',
    3: 'Manager'
}

# Used for recognize Class to be used when contructing user oject
user_classes = {
    'UserAdmin': UserAdmin,
    'Cleaner': Cleaner,
    'HomeOwner': HomeOwner,
    'PlatformManagement': PlatformManagement
}


class UserLoginController:
    def login(self, UserProfileID, Email, Password):

        user_type = UserProfileID_DB_Map.get(UserProfileID)
        if not user_type:
            return {'success': False, 'error':  "Invalid UserProfileID"}

        user = User.find_by_email(UserProfileID_DB_Map[UserProfileID], Email)

        if not user:
            return {'success': False, 'error': 'User not found'}

        if user.check_password(Password):
            userClass = user_classes[UserProfile_DB_Entity_Map[UserProfileID_DB_Map[UserProfileID]]]
            userProfile = userClass.from_user(user)
            userProfile.pullDetails()

            if userProfile.getIsActive():
                return {'success': True, 'user': userProfile.to_dict()}
            return {'success': False, 'error': 'Account suspended'}

        return {'success': False, 'error': 'Invalid password'}
