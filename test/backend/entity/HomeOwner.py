
import bcrypt
from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
from entity.User import User
# make cleaner class, inherits from user.py


class HomeOwner(User):
    def __init__(self,  username=None, email=None, phone=None, Address=None,  is_active=True):
        super().__init__(username, None, email, phone, "HomeOwner", is_active)
        self.Address = Address
        self.db = DB()
##################################################################################
# Req3.5 View Shortlist Service
##################################################################################

    # Can use Service.ViewServiceByID() for this user story

##################################################################################
# Req3.7 View Account
##################################################################################

    def ViewAccount(self, HomeOwnerID: str):
        try:
            # need to make sure password is not returned
            query = """
                    SELECT u."UserID", u."Username", u."UserProfileID", u."Email", u."Phone", HO."Address"
                    FROM "user" u
                    JOIN "HomeOwner" HO ON u."UserID" = HO."HomeOwnerID"
                    WHERE HO."HomeOwnerID" = %s
                    """
            params = (HomeOwnerID,)
            result = self.db.execute_fetchall(query, params)
            return result
        except Exception as e:
            log_exception(e)
            raise (e)

##################################################################################
# Req3.8 Update Account
##################################################################################

    def UpdateAccount(self, HomeOwnerID: str, newUserName, newEmail, newPhone, newAddress):
        try:
            query = """
                    WITH updated_user AS (
                        UPDATE "user"
                        SET
                            "Username" = %s,
                            "Email" = %s,
                            "Phone" = %s
                        WHERE "UserID" = %s
                        RETURNING "UserID"
                    )
                    UPDATE "HomeOwner"
                    SET "Address" = %s
                    WHERE "HomeOwnerID" = (SELECT "UserID" FROM updated_user)
                    """
            params = (newUserName, newEmail, newPhone, HomeOwnerID, newAddress)
            result = self.db.execute_update(query, params)
            return result
        except Exception as e:
            log_exception(e)
            raise (e)

##################################################################################
# Req3.9 Suspend Account
##################################################################################

    def SuspendAccount(self, HomeOwnerID):
        try:
            query = """
                    UPDATE "user"
                    SET "IsActive" = false
                    WHERE "UserID" = %s
                    """
            params = (HomeOwnerID,)
            result = self.db.execute_update(query, params)
            return result
        except Exception as e:
            log_exception(e)
            raise (e)