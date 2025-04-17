from .HomeOwner import HomeOwner
from .PlatformManager import PlatformManager

# HomeOwner mock users
homeowners = [
    HomeOwner("ho1", "password1", "ho1@example.com", "91234567", "Singapore")
]

# Platform Manager mock users
platform_managers = [
    PlatformManager("pm1", "password1", "pm1@example.com", "99887766", "Singapore")
]

# Lookup functions
def find_homeowner_by_username(username):
    for user in homeowners:
        if user.username == username:
            return user
    return None

def find_platform_manager_by_username(username):
    for user in platform_managers:
        if user.username == username:
            return user
    return None