from entity.UserAdmin import UserAdmin

class SearchUserController:
    def __init__(self):
        self.user_admin = UserAdmin()

    def search_user(self, search_term: str):
        return self.user_admin.search_users(search_term)
