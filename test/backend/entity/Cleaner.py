from Classes.Response import Response
from Database import DB
from utils.utils import log_exception
from User import User

#make cleaner class, inherits from user.py
class Cleaner(User):
    def __init__(self,  username=None, email=None, phone=None,  is_active=True,homeOwnerAddress = None, Experience = None, db=DB()):
        super().__init__(username, None, email, phone, "Cleaner", is_active,None)   
        self.Experience = Experience
        self.db = db or DB()