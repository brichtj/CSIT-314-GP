
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

    def createUser(self):
        try:
            hashed_password = bcrypt.hashpw(
                '123'.encode('utf-8'), bcrypt.gensalt())
            # insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive") values (%s, 'Cleaner', %s,%s,%s,true) RETURNING "UserID"
                """
            params = (self.Username, self.Email, self.Phone, hashed_password,)
            result = self.db.execute_update(Userstatement, params)
            # SQL statement returns a userID, which is the first argument in a tuple returned by psycopg2
            id = result[0]
            # insert into cleaner table
            Userstatement = """
                Insert into "HomeOwner" ("HomeOwnerID","Address") values (%s, %s)
                """
            params = (id, self.Address)
            result = self.db.execute_update(Userstatement, params)

            return True

        except Exception as e:
            log_exception(e)
            raise e

    def pullAddress(self):
        query = """
                SELECT "Address"
                FROM "HomeOwner"
                WHERE "HomeOwnerID" = %s
                """
        params = (self.UserID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            self.Address = result[0]
            print(f'{self.Username}: Address pulled')
        else:
            print(f'{self.Username}: Failed to pull Address')

##################################################################################
# Save/Shortlist Service
##################################################################################

    def ShortlistServiceByID(self, ServiceID: str, HomeOwnerID: str):
        try:
            query = """
                    INSERT INTO "Shortlist_Record" ("SericeID", "HomeOwnerID")
                    VALUES (%s, %s)
                    """
            params = (ServiceID, HomeOwnerID)

            result = self.db.execute_update(query, params)

            return result

        except Exception as e:
            log_exception(e)
            raise (e)

##################################################################################
# Search Shortlist Service
##################################################################################

    def ViewShortListByHomeOwnerID(self, HomeOwnerID: str):
        try:
            query = """
                    SELECT "ServiceID"
                    FROM "Shortlist_Record"
                    WHERE "HomeOwnerID" = %s
                    """
            params = (HomeOwnerID,)

            result = self.db.execute_fetchall(query, params)

            return result
        except Exception as e:
            log_exception(e)
            raise (e)

##################################################################################
# View Shortlist Service
##################################################################################

    # Can use Service.ViewServiceByID() for this user story

##################################################################################
# View Account
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
# Update Account
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
# Suspend Account
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