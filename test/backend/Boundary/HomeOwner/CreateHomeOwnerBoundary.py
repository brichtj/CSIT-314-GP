
from fastapi.responses import JSONResponse
from controller.HomeOwner.HomeOwnerController import *
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


class HomeOwnerCreateRequest(BaseModel):
    username: str
    email: str
    phone: str
    address: str


@router.post("/CreateHomeOwner")
def CreateHomeOwnerAccount(data: HomeOwnerCreateRequest):
    try:
        controller = HomeOwnerCreationController()
        # print(data)
        # Your login logic here
        result = controller.HomeOwnerCreationController(
            data.username, data.email, data.phone, data.address)
        # print(result)
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
# Search Service
##################################################################################

@router.get("/SearchServiceByTitle")
def SearchServiceByTitle(Title: str):
    try:
        controller = HomeOwnerSearchServiceController()
        result = controller.SearchServiceByTitle(Title)
        return JSONResponse(ServiceResponse(True, "Service(s) found", result).to_json())
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


@router.get("/SearchServiceByCategory")
def SearchServiceByCategoryName(CategoryName: str):
    try:
        controller = HomeOwnerSearchServiceController()
        result = controller.SearchServiceByCategoryName(CategoryName)
        return JSONResponse(ServiceResponse(True, "Service(s) found", result).to_json())
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


@router.get("/SearchServiceByCategoryID")
def SearchServiceByCategoryID(CategoryID: str):
    try:
        controller = HomeOwnerSearchServiceController()
        result = controller.SearchServiceByCategoryID(CategoryID)
        return JSONResponse(ServiceResponse(True, "Service(s) found", result).to_json())
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


@router.get("/SearchServiceByCleanerID")
def SearchServiceByCleanerID(CleanerID: str):
    try:
        controller = HomeOwnerSearchServiceController()
        result = controller.SearchServiceByCleanerID(CleanerID)
        return JSONResponse(ServiceResponse(True, "Service(s) found", result).to_json())
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
# View Service
##################################################################################

@router.get("/ViewServiceByID")
def ViewServiceByID(ServiceID: str):
    try:
        controller = HomeOwnerViewServiceController()
        result = controller.ViewServiceByID(ServiceID)
        return JSONResponse(ServiceResponse(True, "Service(s) found", result).to_json())
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
# Save/Shortlist Service
##################################################################################


@router.get("/ShortlistServiceByID")
def ShortlistServiceByID(ServiceID: str, HomeOwnerID: str):
    try:
        controller = HomeOwnerShorlistServiceController()
        result = controller.ShortlistServiceByID(ServiceID, HomeOwnerID)
        return JSONResponse(Response(True, "Service Shortlisted").to_json())
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
# Search Shortlist Service
##################################################################################


@router.get("/ViewShortlistByHomeOwnerID")
def ViewShortlistByHomeOwnerID(HomeOwnerID: str):
    try:
        controller = HomeOwnerViewShortListController()
        result = controller.ViewShortlistByHomeOwnerID(HomeOwnerID)
        return JSONResponse(ShortlistResponse(True, "Shortlist found", result).to_json())
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
# View Shortlist Service
##################################################################################


@router.get("/ViewShortlistedServiceByID")
def ViewShortlistedServiceByID(ServiceID: str):
    try:
        controller = HomeOwnerViewShortlistedServiceController()
        result = controller.ViewShortlistedServiceByID(ServiceID)
        return JSONResponse(ServiceResponse(True, "Service(s) found", result).to_json())
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
# View Account
##################################################################################


@router.get("/ViewAccount")
def ViewAccount(HomeOwnerID: str):
    try:
        controller = HomeOwnerViewAccountController()
        result = controller.ViewAccount(HomeOwnerID)

        return JSONResponse(UserResponse(True, "User(s) found", result).to_json())
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
# Update Account
##################################################################################


@router.post("/UpdateAccount")
def UpdateAccount(HomeOwnerID: str, newUserName: str, newEmail: str, newPhone: str, newAddress: str):
    try:
        controller = HomeOwnerUpdateAccountController()
        result = controller.UpdateAccount(
            HomeOwnerID, newUserName, newEmail, newPhone, newAddress)

        return JSONResponse(Response(True, "Account Updated").to_json())
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
# Suspend Account
##################################################################################


@router.post("/SuspendAccount")
def SuspendAccount(HomeOwnerID: str):
    try:
        controller = HomeOwnerSuspendAccountController()
        result = controller.SuspendAccount(HomeOwnerID)

        return JSONResponse(Response(True, "Account Suspended").to_json())
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
# View History
##################################################################################


@router.get("/ViewHistory")
def ViewHistory(HomeOwnerID: str):
    try:
        controller = HomeOwnerViewHistoryController()
        result = controller.ViewHistory(HomeOwnerID)

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
# Search History
##################################################################################


@router.get("/SearchHistoryByServiceID")
def SearchHistoryByServiceID(HomeOwnerID: str, ServiceID: str):
    try:
        controller = HomeOwnerSearchHistoryController()
        result = controller.SearchHistoryByServiceID(HomeOwnerID, ServiceID)

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
