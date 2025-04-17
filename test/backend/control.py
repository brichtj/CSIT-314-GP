from Entity.mockdb import (
    find_homeowner_by_username,
    find_platform_manager_by_username
)

def login_control(profile, username, password):
    if profile == "homeowner":
        user = find_homeowner_by_username(username)

    elif profile == "platform_manager":
        user = find_platform_manager_by_username(username)

    elif profile == "cleaner":
        raise Exception("Cleaner login not yet implemented")

    elif profile == "admin":
        raise Exception("Admin login not yet implemented")

    else:
        raise Exception("Unsupported profile type")

    if not user:
        raise Exception("User not found")
    if user.password != password:
        raise Exception("Incorrect password")

    return user