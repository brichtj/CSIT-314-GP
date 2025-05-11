
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
    
#req 2 create
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
    

#req 2, 3.3, 3.5 view service==================
@router.get("/ViewServiceCleaner")
def ViewServiceCleanerBoundary(ServiceID:int):

    try:
        controller = ViewServiceController()
        result = controller.ViewServiceController(ServiceID,False)
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
    

@router.get("/ViewServiceHomeOwner")#only when homeowner view service, should the view count be updated
def ViewServiceHomeownerBoundary(ServiceID:int):

    try:
        controller = ViewServiceController()
        result = controller.ViewServiceController(ServiceID,True)
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
@router.get("/ViewServiceShortlist")
def ViewServiceShortlistBoundary(ServiceID:int):

    try:
        controller = ViewServiceController()
        result = controller.ViewServiceController(ServiceID,False)
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
    
#==========================
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


##################################################################################
# Req3.1 Search Service
##################################################################################

@router.get("/SearchService")
def SearchService(mode: int, searchTerm: str):
    try:
        controller = HomeOwnerSearchServiceController()
        result = controller.SearchService(mode, searchTerm)
        return JSONResponse(Response(True, [row.to_json() for row in result]).to_json())
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
# Req3.7 View Account
##################################################################################


@router.get("/ViewAccount")
def ViewAccount(HomeOwnerID: str):
    try:
        controller = HomeOwnerViewAccountController()
        result = controller.ViewAccount(HomeOwnerID)

        return JSONResponse(Response(True,  result).to_json())
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
# Req3.8 Update Account
##################################################################################

class UpdateAccountRequest(BaseModel):
    HomeOwnerID: str
    newUserName: str
    newEmail: str
    newPhone: str
    newAddress: str
@router.post("/UpdateAccount")
def UpdateAccount(data: UpdateAccountRequest):
    try:
        controller = HomeOwnerUpdateAccountController()
        result = controller.UpdateAccount(
            data.HomeOwnerID, data.newUserName, data.newEmail, data.newPhone, data.newAddress)

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
# Req3.9 Suspend Account
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
# View History req 6.1
##################################################################################


@router.get("/HomeOwner/ViewHistory")
def ViewHistory(HomeOwnerID: str):
    try:
        controller = HomeOwnerViewHistoryController()
        result = controller.ViewHistory(HomeOwnerID)

        return JSONResponse(Response(True,result).to_json())
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
# Search History req 6.2
##################################################################################


@router.get("/HomeOwner/SearchHistoryByServiceID")
def SearchHistoryByServiceID(HomeOwnerID: str, ServiceID: str):
    try:
        controller = HomeOwnerSearchHistoryController()
        result = controller.SearchHistoryByServiceID(HomeOwnerID, ServiceID)

        return JSONResponse(Response(True,  result).to_json())
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

