from fastapi import HTTPException
from models.user_entity import UserEntity
from schemas.auth_schema import LoginRequest

class AuthController:
    def __init__(self, conn):
        self.conn = conn

    def login(self, request: LoginRequest):
        user_entity = UserEntity(self.conn)
        user = user_entity.get_user_by_username(request.username)

        #if not user or user["password"] != request.password:
            #raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Login successful"}
