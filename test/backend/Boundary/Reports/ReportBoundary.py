
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
from controller.Report.ReportController import *
import psycopg2
from datetime import date

router = APIRouter()


    
#req 7 generate report
@router.get("/getDailyReport")
def getDailyReportBoundary():
    try:
        controller = GetReportController()
        result = controller.getReportController('daily')
        serialized = [
    {**row, 'date': row['date'].isoformat()} for row in result
]
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,serialized).to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        log_exception(e)
        return JSONResponse(
            content=Response(False, "Database Error").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )
@router.get("/getWeeklyReport")
def getWeeklyReportBoundary():
    try:
        controller = GetReportController()
        result = controller.getReportController('weekly')  
        serialized = [
    {**row, 'date': row['date'].isoformat()} for row in result
]
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,serialized).to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        log_exception(e)
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
@router.get("/getMonthlyReport")
def getMonthlyReportBoundary():
    try:
        controller = GetReportController()
        result = controller.getReportController('monthly')
        serialized = [
    {**row, 'date': row['date'].isoformat()} for row in result
]
        if result is None:
            return JSONResponse(Response(False,None).to_json())
        else:
            return JSONResponse(Response(True,serialized).to_json())
    except psycopg2.Error as e:
        message = f"Database Error: {e}"
        log_exception(e)
        return JSONResponse(
            content=Response(False, "Database Error").to_json(),
            status_code=400
        )
    except Exception as e:
        print(f"exception has occured: {e}")
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )