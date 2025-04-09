from entity import User, UserAdmin, Cleaner, HomeOwner, PlatfromManagement

user_classes = {
    UserAdmin: UserAdmin,
    Cleaner: Cleaner,
    HomeOwner: HomeOwner,
    PlatfromManagement: PlatfromManagement
}

def login_control(mode, username, password) ->User:
    if mode not in user_classes:
        raise Exception("Invalid mode")

    user = user_classes[mode](username, password)

    try:
        user.authenticate()
        return user
    except Exception as e:
        raise Exception(e)