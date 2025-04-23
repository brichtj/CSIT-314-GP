
from fastapi.responses import JSONResponse
from controller.UserLoginController import UserLoginController
from fastapi import APIRouter, Request
from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response


router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    try:
        controller = UserLoginController()
        username = data.username
        password = data.password
        result = controller.login(username,password)
        # Your login logic here
        return JSONResponse(result.to_json())

    except Exception as e:
        log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error"),
            status_code=500
        )