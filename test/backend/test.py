from fastapi.responses import JSONResponse
from controller.UserLoginController import UserLoginController
from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from Database import DB
from boundary import *
from entity.Matches import *
from entity.Service import *
from entity.Category import *
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# Force singleton to initialize and connect DB
_ = DB()


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginRequest):
    try:
        controller = UserLoginController()
        username = data.username
        password = data.password
        result = controller.login(username, password)
        # Your login logic here
        return JSONResponse(result.to_json())

    except Exception as e:
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error"),
            status_code=500
        )


@app.post("/test")
def test(data: str):
    try:
        service = Category()
        result = service.searchByCategoryID(data)
        return JSONResponse(content=jsonable_encoder(result.to_json()))

    except Exception as e:
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error"),
            status_code=500
        )
