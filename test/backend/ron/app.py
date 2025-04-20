from fastapi import FastAPI, Depends, Request
from flask import jsonify
from database import get_db_connection
from controllers.auth_controller import AuthController
from schemas.auth_schema import LoginRequest

app = FastAPI()

def get_conn():
    conn = get_db_connection()
    try:
        yield conn
    finally:
        conn.close()

@app.post("/login")
def login_route(request: LoginRequest, conn = Depends(get_conn)):
    controller = AuthController(conn)
    return controller.login(request)
@app.route('/', methods=['GET'])
def default():
    return jsonify({'success':"true"})