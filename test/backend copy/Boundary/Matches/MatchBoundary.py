
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


#match boundary
class MatchesRequest(BaseModel):
    HomeOwnerID: int
    ServiceID: int
    Price: float
@router.post("/CreateMatch")
def CreateMatchBoundary(data: MatchesRequest):
    try:
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