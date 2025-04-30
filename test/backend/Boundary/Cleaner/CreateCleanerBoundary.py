
from fastapi.responses import JSONResponse
from controller.Cleaner.CleanerCreationController import CleanerCreationController
from fastapi import APIRouter, Request
from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2


router = APIRouter()

class CleanerCreateRequest(BaseModel):
    username: str
    email: str
    phone: str
    experience: float

@router.post("/CreateCleanerAccount")
def CreateAccount(data: CleanerCreateRequest):
    try:
        controller = CleanerCreationController()
        #print(data)
        # Your login logic here
        result = controller.CleanerCreationController(data.username,data.email,data.phone,data.experience)
        #print(result)
        return JSONResponse(Response(True,"Successfully created user").to_json())
    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate user?): {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"Username already exists").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error creating user").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        #log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )