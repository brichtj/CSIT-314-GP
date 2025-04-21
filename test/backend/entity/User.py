from Classes.LoginResponse import LoginResponse
from 


class User:
    #Password =  input_Password
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def login(self):
        
    


        return LoginResponse(success:bool,message:str,user) 

    def pullDetails(self):
        query = """
                SELECT "UserID", "Username", "UserProfile", "Email", "Phone", "IsActive"
                FROM "User"
                WHERE "Email" = %s"""
        params = (self.Email,)

        db = DB()
        result = db.execute_fetchone(query, params)

        if result:
            self.UserID = result[0]
            self.Username = result[1]
            self.UserProfile = result[2]
            self.Email = result[3]
            self.Phone = result[4]
            self.IsActive = result[5]
            print(f"{self.Email}: Details pulled")
        else:
            print(f"{self.Email}: Failed to pull details")
            return

        print(f"{self.Email}: Failed to pull details")
        raise Exception("Failed to pull details")