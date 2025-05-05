
from fastapi.responses import JSONResponse
from controller.UserAdmin.ViewUserAccountController import ViewUserController
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()



@router.get("/ViewUserAccount")
def ViewUserAccount(username:str):
    try:
        controller = ViewUserController()
        #print(data)
        # Your login logic here
        result = controller.viewUserController(username)
        if result is not None:
            return JSONResponse(Response(True,result).to_json())
        else:
            print(result)
            return JSONResponse(Response(False,None).to_json())

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

