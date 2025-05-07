
from fastapi.responses import JSONResponse
from controller.Service.ServiceController import *
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()


#req 2  create
class CreateServiceRequest(BaseModel):
    CategoryID: int
    Title: str
    Description: str
    CleanerID: int
    Price: float
    ImageLink: str
    
@router.post("/CreateService")
def CreateService(data: CreateServiceRequest):
    try:
        controller = CreateServiceController()
        #print(data)
        # Your login logic here
        result = controller.createServiceController(data.CategoryID,data.Title,data.Description,data.CleanerID,data.Price,data.ImageLink)
       
        return JSONResponse(Response(True,"Successfully created Service").to_json())
    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate Service?): {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"Error").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error creating Service").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        #log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )
    
