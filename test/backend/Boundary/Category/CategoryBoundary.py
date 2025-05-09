
from fastapi.responses import JSONResponse
from controller.Category.CategoryController import *
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


#req 7 create category
class CategoryCreateRequest(BaseModel):
    Title:str
    Description:str


@router.post("/CreateCategory")
def CreateCategoryBoundary(data: CategoryCreateRequest):
    try:
        controller = CreateCategoryController()
        result = controller.CreateCategoryController(data.Title,data.Description)
        if result:
            return JSONResponse(Response(True, "Successfully created Category").to_json())
        else:
            return JSONResponse(
                content=Response(False, "Error creating category").to_json(),
                status_code=409
            )
    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate category?): {e}")
        # log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False, "Category already exists").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        # log_exception(e)
        print(f"Database error: {e}")
        return JSONResponse(
            content=Response(False, "Error creating Category").to_json(),
            status_code=400
        )

    except Exception as e:
        print("exception has occured")
        # log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )

#req 7 view category
@router.get("/ViewCategory")
def ViewCategoryBoundary(CategoryID:int):
    try:
        controller = ViewCategoryController()
        result = controller.ViewCategoryController(CategoryID)
        if result is not None:
            return JSONResponse(Response(True,result.to_json()).to_json())
        else:
            return JSONResponse(Response(True,None).to_json())

    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )

#req 7 update category
class CategoryUpdateRequest(BaseModel):
    CategoryID:int
    Title:str
    Description:str
    Is_Active:bool

@router.put("/UpdateCategory")
def UpdateCategoryBoundary(data: CategoryUpdateRequest):
    try:
        controller = UpdateCategoryController()
        result = controller.UpdateCategoryController(data.CategoryID,data.Title,data.Description,data.Is_Active)
        if result:
            return JSONResponse(Response(True, "Successfully updated Category").to_json())
        else:
            return JSONResponse(
                content=Response(False, "CateogryID does not exist").to_json(),
                status_code=409
            )
    except psycopg2.Error as e:
        # log_exception(e)
        print(f"Database error: {e}")
        return JSONResponse(
            content=Response(False, "Title already exists").to_json(),
            status_code=400
        )
    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )
    
#req 7 suspend category
class CategorySuspendRequest(BaseModel):
    CategoryID:int

@router.put("/SuspendCategory")
def SuspendCategoryBoundary(data: CategorySuspendRequest):
    try:
        controller = SuspendCategoryController()
        result = controller.SuspendCategoryController(data.CategoryID)
        if result:
            return JSONResponse(Response(True, "Successfully suspended Category").to_json())
        else:
            return JSONResponse(
                content=Response(False, "CategoryID does not exist").to_json(),
                status_code=409
            )
    except psycopg2.Error as e:
        # log_exception(e)
        print(f"Database error: {e}")
        return JSONResponse(
            content=Response(False, "error suspending category").to_json(),
            status_code=400
        )
    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )

#req 7 search category
@router.get("/SearchCategory")
def SearchCategoryBoundary(keyword:str):
    try:
        controller = SearchCategoryController()
        result = controller.SearchCategoryController(keyword)
        return JSONResponse(Response(True,[row.to_json() for row in result]).to_json())
    except psycopg2.Error as e:
        # log_exception(e)
        print(f"Database error: {e}")
        return JSONResponse(
            content=Response(False, "error searching category").to_json(),
            status_code=400
        )
    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=505
        )