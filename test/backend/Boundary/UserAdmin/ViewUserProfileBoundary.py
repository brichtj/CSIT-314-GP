
from fastapi.responses import JSONResponse
from controller.UserAdmin.ViewUserProfileController import ViewUserProfileController
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()

class ViewUserProfileRequest(BaseModel):
    name: str


@router.get("/ViewUserProfile")
def ViewUserProfile(data: ViewUserProfileRequest):
    try:
        controller = ViewUserProfileController()
        #print(data)
        # Your login logic here
        result = controller.viewUserProfileController(data.name)
        if result is not None:
            return JSONResponse(Response(True,result).to_json())
        else:
            print(result)
            return JSONResponse(Response(False,None).to_json())

   
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error finding profile").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        #log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )

