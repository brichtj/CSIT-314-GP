from fastapi import FastAPI,Request
from flask import jsonify
from controller.UserLoginController import UserLoginController


app = FastAPI()

@app.post("/login")
def loginBoundary():
    return jsonify({"success":True})