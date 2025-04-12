

from Entity import User, UserAdmin, Cleaner, HomeOwner, PlatformManagement

# funtion name to used for different mode
user_classes = {
    UserAdmin: UserAdmin,
    Cleaner: Cleaner,
    HomeOwner: HomeOwner,
    PlatformManagement: PlatformManagement
}


# controller for login
def login_control(profile, email, password) -> User:
    # checking input mode
    if profile not in user_classes:
        raise Exception("Invalid mode")

    try:
        user = user_classes[profile](email)  # construct User Object
        # authenticate password and login afterwards
        user.login()
        return user
    except Exception as e:
        raise Exception(e)


def createUser_control(profile, username, password, email, phone, add):
    if profile not in user_classes:
        raise Exception("Invalid mode")

    try:
        user = user_classes[profile](email)
        user.createUser(username, email, phone, password)

        # additional details
        if type(user).__name__ == "HomeOwner":
            user.setModifiable()
            user.setAddress(add)
            user.setUnmidifiable()

        return True
    except Exception as e:
        raise Exception(e)
