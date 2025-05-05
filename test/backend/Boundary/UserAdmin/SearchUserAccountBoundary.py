from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from controller.UserAdmin.SearchUserAccountController import AdminSearchUserController
from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()



@router.get("/AdminSearchUserAccount")
def AdminSearchUserAccount(searchTerm:str):
    try:
        controller = AdminSearchUserController()
        result = controller.adminSearchUserController(searchTerm)
        if result is not None:
            return JSONResponse(Response(True,result).to_json())
        else:
            return JSONResponse(Response(False,None).to_json())

    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error searching user").to_json(),
            status_code=400
        )
    except Exception as e:
        print("exception has occured")
        #log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )
