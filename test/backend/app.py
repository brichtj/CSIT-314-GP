from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from controller.UserLoginController import UserLoginController


app = FastAPI()

@app.post("/login")
def loginBoundary():
    return JSONResponse(content={"success":True})