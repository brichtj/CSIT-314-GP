from fastapi.responses import JSONResponse
from controller.HomeOwner.HomeOwnerCreationController import HomeOwnerCreationController
from fastapi import APIRouter
from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()

class HomeOwnerCreateRequest(BaseModel):
    username: str
    password: str
    email: str
    phone: str
    address: str

@router.post("/CreateHomeOwnerAccount")
def CreateAccount(data: HomeOwnerCreateRequest):
    try:
        controller = HomeOwnerCreationController()

        result = controller.register(
            username=data.username,
            password=data.password,
            email=data.email,
            phone=data.phone,
            address=data.address
        )

        return JSONResponse(Response(True, "Successfully created user").to_json())

    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate user?): {e}")
        # log_exception(e)
        return JSONResponse(
            content=Response(False, "Username already exists").to_json(),
            status_code=409
        )

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        # log_exception(e)
        return JSONResponse(
            content=Response(False, "Error creating user").to_json(),
            status_code=400
        )

    except Exception as e:
        print("An unexpected exception has occurred")
        # log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )
