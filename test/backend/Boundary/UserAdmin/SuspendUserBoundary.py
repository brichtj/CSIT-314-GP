
from fastapi.responses import JSONResponse
from controller.UserAdmin.SuspendUserController import SuspendUserController
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()

class ViewUserRequest(BaseModel):
    username: str


@router.put("/SuspendUserAccount")
def SuspendUserAccount(data: ViewUserRequest):
    try:
        controller = SuspendUserController()
        #print(data)
        # Your login logic here
        result = controller.suspendUserController(data.username)
        #controller returns true if updated, false if not updated(in the case of no such user)
        if result:
            return JSONResponse(Response(True,"User Successfully suspended").to_json())
        else:
            return JSONResponse(Response(False,"No Such User").to_json())

    except psycopg2.IntegrityError as e:
        print(f"Integrity error: {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"database error").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"database error").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        #log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )

