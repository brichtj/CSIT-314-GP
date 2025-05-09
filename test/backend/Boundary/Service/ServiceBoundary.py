
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
def CreateServiceBoundary(data: CreateServiceRequest):
    try:
        controller = CreateServiceController()
        #print(data)
        # Your login logic here
        result = controller.createServiceController(data.CategoryID,data.Title,data.Description,data.CleanerID,data.Price,data.ImageLink)
       
        return JSONResponse(Response(True,"Successfully created Service").to_json())
    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate Title?): {e}")
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
    

#req 2 view service
@router.get("/ViewService")
def ViewServiceBoundary(ServiceID:int):

    try:
        controller = ViewServiceController()
        result = controller.ViewServiceController(ServiceID)
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,result.to_json()).to_json())
    except psycopg2.Error as e:
        # log_exception(e)
        print(f"Database error: {e}")
        return JSONResponse(
            content=Response(False, "error searching Service").to_json(),
            status_code=400
        )
    except Exception as e:
        print("exception has occured")
        #log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )   
    
#req 2 update service
class UpdateServiceRequest(BaseModel):
    ServiceID: int
    CategoryID: int
    Title: str
    Description: str
    CleanerID: int
    Price: float
    ImageLink: str

@router.put("/UpdateService")
def UpdateServiceBoundary(data:UpdateServiceRequest):   
    try:
        controller = UpdateServiceController()
        result = controller.UpdateServiceController(data.CategoryID,data.Title,data.Description,data.Price,data.ImageLink,data.ServiceID,data.CleanerID)
        if result:
            return JSONResponse(Response(True,"Updated").to_json())
        else:
            return JSONResponse(Response(False,"ServiceID and CleanerID combination does not exist").to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        print(message)
        return JSONResponse(
            content=Response(False, "Request error").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )

#delete service
@router.delete("/DeleteService")
def DeleteServiceBoundary(ServiceID:int,CleanerID:int):
    try:
        controller = DeleteServiceController()
        result = controller.DeleteServiceController(ServiceID,CleanerID)
        if result:
            return JSONResponse(Response(True,"Deleted").to_json())
        else:
            return JSONResponse(Response(False,"ServiceID does not exist").to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        print(message)
        return JSONResponse(
            content=Response(False, "Delete Request error, maybe ServiceID and cleanerID combination does not exist").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )

#search service
@router.get("/SearchServiceByCleanerID")
def SearchServiceByCleanerID(Title:str,CleanerID:int):
    try:
        controller = SearchServiceCleanerIDController()
        result = controller.SearchServiceCleanerIDController(Title,CleanerID)
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,[row.to_json() for row in result]).to_json())
    except psycopg2.Error as e:
        # log_exception(e)
        print(f"Database error: {e}")
        return JSONResponse(
            content=Response(False, "error searching Service").to_json(),
            status_code=400
        )
    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )