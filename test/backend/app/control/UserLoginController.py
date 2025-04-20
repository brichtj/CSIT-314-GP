from app.entity.User import User
from app.entity.UserAdmin import UserAdmin
from app.entity.Cleaner import Cleaner
from app.entity.HomeOwner import HomeOwner
from app.entity.PlatformManagement import PlatformManagement

from app.control.repository.UserRepository import UserRepository

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
    def login(self, UserProfileID, Email, Password) -> dict:
        try:
            user_type = UserProfileID_DB_Map.get(UserProfileID)
            if not user_type:
                raise Exception("Invalid UserProfileID")

            result = UserRepository.findByEmail(
                UserProfileID_DB_Map[UserProfileID], Email)

            userClass = user_classes[UserProfile_DB_Entity_Map[UserProfileID_DB_Map[UserProfileID]]]
            user = userClass(result[0], result[1])

            if user.checkPassword(Password):

                data = UserRepository.pullDetails(Email)

                user.setDetails(data["UserID"],
                                data["Username"],
                                data["UserProfile"],
                                data["Email"],
                                data["Phone"],
                                data["IsActive"])

                if isinstance(user, Cleaner):
                    data.update(
                        UserRepository.pullExperience(data['UserID']))
                    user.setExperience(data['Experience'])

                if isinstance(user, HomeOwner):
                    data.update(UserRepository.pullAddress(data['UserID']))
                    user.setAddress(data['Address'])

                return {'success': True, 'user': user.to_dict()}

            raise Exception('Invalid Password')

        except Exception as e:
            return {'success': False, 'error': str(e)}
