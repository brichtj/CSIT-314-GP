
from fastapi.responses import JSONResponse
from controller.Cleaner.CleanerController import *
from fastapi import APIRouter, Request
from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
from Classes.DataResponse import DataResponse
from Classes.ServiceResponse import ServiceResponse
from Classes.MatchesResponse import MatchesResponse
from Classes.DataResponse import DataResponse
import psycopg2


router = APIRouter()


class CleanerCreateRequest(BaseModel):
    username: str
    password: str
    email: str
    phone: str
    experience: float


@router.post("/CreateCleanerAccount")
def CreateHomeOwnerAccount(data: CleanerCreateRequest):
    try:
        controller = CleanerCreationController()

        # controller method
        result = controller.register(
            username=data.username,
            password=data.password,
            email=data.email,
            phone=data.phone,
            experience=data.experience
        )

        return JSONResponse(Response(True, "Successfully created user").to_json())
    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate user?): {e}")
        # log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False, "Username already exists").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        # log_exception(e)
        print(f"Database error: {e}")
        return JSONResponse(
            content=Response(False, "Error creating user").to_json(),
            status_code=400
        )

    except Exception as e:
        print("exception has occured")
        # log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )


##################################################################################
# Req4.1 View Total Views of Services
##################################################################################

@router.get("/ViewTotalViewByID")
def ViewTotalViewbyID(ServiceID: str):
    try:
        controller = CleanerViewServiceTotalViewsController()
        result = controller.ViewTotalViewbyID(ServiceID)
        return JSONResponse(DataResponse(True, "Total count found", result).to_json())
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


##################################################################################
# Req4.2 View Total Shortlisted Count of Services
##################################################################################

@router.get("/ViewTotalShortlistedCountByID")
def ViewTotalShortlistedCountbyID(ServiceID: str):
    try:
        controller = CleanerViewServiceShortlistedCountController()
        result = controller.ViewTotalShortlistedCountByID(ServiceID)
        return JSONResponse(DataResponse(True, "Total count found", result).to_json())
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

##################################################################################
# Req5.1 View History
##################################################################################


@router.get("/Cleaner/ViewHistory")
def ViewHistory(CleanerID: str):
    try:
        controller = CleanerViewHistoryController()
        result = controller.ViewHistory(CleanerID)
        return JSONResponse(MatchesResponse(True, "Match(s) found", result).to_json())
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

##################################################################################
# Req5.2 Search History
##################################################################################


@router.get("/Cleaner/SearchHistoryByServiceID")
def SearchHistoryByServiceID(CleanerID: str, ServiceID: str):
    try:
        controller = CleanerSearchHistoryController()
        result = controller.SearchHistoryByServiceID(CleanerID, ServiceID)
        return JSONResponse(MatchesResponse(True, "Match(s) found", result).to_json())
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

##################################################################################
# Req2 View My service
##################################################################################
@router.get("/ViewMyService")
def ViewMyService(CleanerID: int):
    try:
        controller = ViewMyServiceController()
        result = controller.ViewMyService(CleanerID)
        return JSONResponse(MatchesResponse(True, "Match(s) found", result).to_json())
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
    
##################################################################################
# Req2 delete My service
##################################################################################
@router.delete("/DeleteService")
def DeleteService(cleanerID: int,serviceID:int):
    try:
        controller = DeleteServiceController()
        result = controller.deleteService(cleanerID,serviceID)
        return JSONResponse(Response(True, "Deleted").to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        #print(message)
        return JSONResponse(
            content=Response(False, "No rows were deleted").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )