from entity.HomeOwner import HomeOwner

class HomeOwnerCreationController:
    def register(self, username, password, email, phone, address):
        homeowner = HomeOwner(
            username=username,
            email=email,
            phone=phone,
            address=address,
            input_password=password
        )
        return homeowner.create_account()
