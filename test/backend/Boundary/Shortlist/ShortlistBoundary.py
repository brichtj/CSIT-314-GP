
from fastapi.responses import JSONResponse
from controller.Shortlist.ShortlistController import *
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()

class ShortlistServiceRequest(BaseModel):
    serviceID: int
    HomeOwnerID: int

#req 3.3 shortlist
@router.post("/ShortlistService")
def ShortlistService(data: ShortlistServiceRequest):
    try:
        print(data)
        controller = ShortListServiceController()
        result = controller.ShortListServiceController(data.serviceID, data.HomeOwnerID)
        if result:
            return JSONResponse(content=Response(True,"Shortlisted").to_json())
        else:
            return JSONResponse(
                content=Response(False, "Wrong input").to_json(),
                status_code=400
            )
    except Exception as e:
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=500
        )
    
#req 3.4 searchShortlist
@router.get("/SearchShortlistForHomeOwner")
def SearchShortlistForHomeOwner(HomeOwnerID: int,Title:str):
    try:
        controller = SearchShortListController()
        result = controller.SearchShortListForHomeOwnerController(HomeOwnerID,Title)
        
        return JSONResponse(Response(True, [row.to_json() for row in result]).to_json())
    except Exception as e:
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=500
        )
    