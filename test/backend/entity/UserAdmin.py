import bcrypt
from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
import psycopg2
#make cleaner class, inherits from user.py
class UserAdmin():
    def __init__(self):
        self.db = DB()
    
    def createUser(self,username,email,phone,experience,address,userType):
        try:
            hashed_password = bcrypt.hashpw('123'.encode('utf-8'), bcrypt.gensalt())
            UserprofileID = 1
                 #swithch case based on userType to change userstatement
            if userType == "Cleaner":
                UserprofileID = 1
            elif userType == "HomeOwner":
                UserprofileID = 2
            elif userType == "UserAdmin":
                UserprofileID = 3
            elif userType == "PlatformManagement":
                UserprofileID = 4
            else:
                raise ValueError("Invalid user type")
            #insert into user table
            Userstatement = """
                Insert into "user" ("Username","UserProfileID", "Email","Phone","Password","IsActive","Address","Experience") values (%s, %s, %s,%s,%s,true,%s,%s) RETURNING "UserID"
                """
            params = (username,UserprofileID,email,phone,hashed_password,address,experience,)
            result =self.db.execute_update(Userstatement, params)
            id = result[0]#SQL statement returns a userID, which is the first argument in a tuple returned by psycopg2
            #insert into cleaner table
            
            return True


        except Exception as e:
            log_exception(e)
            raise e
    def viewUser(self,username):
        try:
            query = """
                        SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive", "Address", "Experience"
                        FROM "user"
                        WHERE LOWER("Username") = LOWER(%s)
                    """
            params = (username,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = self.db.execute_fetchone(query, params)
            #create json object based on query results
           

            if result is not None:
                data = {
                    "UserID": result[0],
                    "Username": result[1],
                    "UserProfileID": result[2],
                    "Email": result[3],
                    "Phone": result[4],
                    "IsActive": result[5],
                    "Address": result[6],
                    "Experience": result[7]
                }
                return data
            else:               
                return None
        except Exception as e:
            log_exception(e)
            raise (e)
    def suspendUser(self,username):
        try:
            query = """
                        UPDATE "user"
                        SET "IsActive" = false
                        WHERE LOWER("Username") = LOWER(%s)
                    """
            params = (username,)
            # formatted_query = query % tuple(map(lambda x: f"'{x}'", params))
            # print(f"Formatted query: {formatted_query}")

            result = self.db.execute_update(query, params)
            #create json object based on query results
            print(result)

            if result:
                return True
            else:               
                return False
        except Exception as e:
            log_exception(e)
            raise (e)

    def update_user(self, username, updated_data):
        try:
            if not updated_data:
                print("No data provided to update.")
                return False

            set_clauses = []
            params = []

            for key, value in updated_data.items():
                set_clauses.append(f'"{key}" = %s')
                params.append(value)

            set_clause_str = ", ".join(set_clauses)
            sql = f'UPDATE "user" SET {set_clause_str} WHERE "Username" = %s'
            params.append(username)

            print("Executing SQL:", sql)
            print("With parameters:", params)

            result = self.db.execute_update(sql, tuple(params))

            if result:
                print("User updated successfully.")
                return True
            else:
                print("No user found or nothing was updated.")
                return False

        except Exception as e:
            print("Exception during update_user:", e)
            return False

    def search_users(self, search_term):
        try:
            query = """
                SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive"
                FROM "user"
                WHERE LOWER("Username") LIKE LOWER(%s)
            """
            wildcard_term = f"%{search_term}%"
            params = (wildcard_term,)

            results = self.db.execute_fetchall(query, params)

            if results:
                users = []
                for row in results:
                    users.append({
                        "UserID": row[0],
                        "Username": row[1],
                        "UserProfileID": row[2],
                        "Email": row[3],
                        "Phone": row[4],
                        "IsActive": row[5],
                    })
                return Response(True, "Users found", users)
            else:
                return Response(False, "No users found")

        except Exception as e:
            log_exception(e)
            return Response(False, "Search failed")

    def search_users(self, search_term):
        try:
            query = """
                SELECT "UserID", "Username", "UserProfileID", "Email", "Phone", "IsActive"
                FROM "user"
                WHERE LOWER("Username") LIKE LOWER(%s)
            """
            wildcard_term = f"%{search_term}%"
            params = (wildcard_term,)
            cur = self.db.conn.cursor()
            cur.execute(query, params)
            results = cur.fetchall()


            if results:
                users = [
                    {
                        "UserID": row[0],
                        "Username": row[1],
                        "UserProfileID": row[2],
                        "Email": row[3],
                        "Phone": row[4],
                        "IsActive": row[5],
                    } for row in results
                ]
                return Response(True, "Users found", users)
            else:
                return Response(False, "No users found")
        except Exception as e:
            log_exception(e)
            return Response(False, "Search failed due to error")



    def pullExperience(self):
        query = """
                SELECT "Experience"
                FROM "Cleaner"
                WHERE "CleanerID" = %s
                """
        params = (self.UserID,)

        result = self.db.execute_fetchone(query, params)

        if result:
            self.Experience = result[0]
            print(f'{self.Username}: Experience pulled')
        else:
            print(f'{self.Username}: Failed to pull Experience')
