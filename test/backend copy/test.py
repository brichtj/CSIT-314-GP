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
from fastapi.testclient import TestClient

app = FastAPI()

# Force singleton to initialize and connect DB
_ = DB()


# Register routers
app.include_router(login_boundary)
app.include_router(cleaner_boundary)
app.include_router(user_admin_boundary)
app.include_router(home_owner_boundary)

if __name__ == "__main__":
    client = TestClient(app)
    response = client.get("/Cleaner/SearchHistoryByServiceID", params={"CleanerID": "31", "ServiceID" : "5"})
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

# if __name__ == "__main__":
#     client = TestClient(app)
#     response = client.post(
#         "/UpdateAccount",
#         json={
#             "HomeOwnerID": "55",
#             "newUserName": "New",
#             "newEmail": "ew@gmail.com",
#             "newPhone": "9876543210",
#             "newAddress": "newAddress"
#         }
#     )
#     print("Status Code:", response.status_code)
#     print("Response JSON:", response.json())
