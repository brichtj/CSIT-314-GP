from fastapi import APIRouter
from controller.UserLoginController import UserLoginController
from pydantic import BaseModel

login_boundary = APIRouter()


class LoginRequest(BaseModel):
    Username: str
    Password: str


@login_boundary.post("/login")
def login(data: LoginRequest):
    user = UserLoginController()
    return user.login(data.Username, data.Password)


@login_boundary.get("/logout")
def logout():
    return {'Logout'}
