
from fastapi.responses import JSONResponse
from controller.Matches.MatchController import *
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
from Classes.UserResponse import UserResponse
from Classes.ShortlistResponse import ShortlistResponse
from Classes.ServiceResponse import ServiceResponse
from Classes.MatchesResponse import MatchesResponse
import psycopg2

router = APIRouter()


#match boundary req 3 extras
class MatchesRequest(BaseModel):
    HomeOwnerID: int
    ServiceID: int
    Price: float
@router.post("/CreateMatch")
def CreateMatchBoundary(data: MatchesRequest):
    try:
        print(data)
        controller = CreateMatchController()
        result = controller.CreateMatchController(data.HomeOwnerID, data.ServiceID, data.Price,)
        if result:
            return JSONResponse(Response(True,"Created match").to_json())
        else:
            return JSONResponse(Response(False,"ServiceID and HomeOwnerID combination does not exist").to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        print(message)
        return JSONResponse(
            content=Response(False, "Request error").to_json(),
            status_code=400
        )
    except Exception as e:
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=500
        )
    
#req 5.1 and req 6.1
@router.get("/ViewMatchHistory")
def ViewMatchBoundary(ServiceID:int):
    try:
        controller = ViewMatchController()
        result = controller.ViewMatchController(ServiceID)
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,result.to_json()).to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        print(message)
        return JSONResponse(
            content=Response(False, "Database Error").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )

#req 5.2
@router.get("/SearchMatchCleaner")
def SearchMatchCleanerBoundary(searchTerm:str, CleanerID:int):
    try:
        controller = SearchMatchCleanerController()
        result = controller.SearchMatchCleanerController(searchTerm,CleanerID)
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,[row.to_json() for row in result]).to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        print(message)
        return JSONResponse(
            content=Response(False, "Database Error").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )
    
#req 6.2
@router.get("/SearchMatchHomeOwner")
def SearchMatchHomeOwnerBoundary(searchTerm:str, HomeOwnerID:int):
    try:
        controller = SearchMatchHomeOwnerController()
        result = controller.SearchMatchHomeOwnerController(searchTerm,HomeOwnerID)
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,[row.to_json() for row in result]).to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        print(message)
        return JSONResponse(
            content=Response(False, "Database Error").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )