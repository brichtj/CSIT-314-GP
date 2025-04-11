

from Entity import User, UserAdmin, Cleaner, HomeOwner, PlatformManagement

# funtion name to used for different mode
user_classes = {
    UserAdmin: UserAdmin,
    Cleaner: Cleaner,
    HomeOwner: HomeOwner,
    PlatformManagement: PlatformManagement
}


# controller for login
def login_control(mode, username, password) -> User:
    # checking input mode
    if mode not in user_classes:
        raise Exception("Invalid mode")

    # construct user object
    user = user_classes[mode](username)

    try:
        user.authenticate(password) #authenticate password
        user.pullDetail()   #pull user details
        return user
    except Exception as e:
        raise Exception(e)
