from entity.UserAdmin import UserAdmin

class UpdateUserController:
    def update_user(self, username: str, updated_data: dict) -> bool:
        return UserAdmin().update_user(username, updated_data)
