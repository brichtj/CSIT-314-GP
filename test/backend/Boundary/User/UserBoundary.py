
from fastapi.responses import JSONResponse
from controller.User.UserController import *
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()


# misc req login
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    try:
        controller = UserLoginController()
        result = controller.login(data.username, data.password)
        if result.success:
            return JSONResponse(Response(True, result.user.to_json()).to_json())
        else:
            return JSONResponse(
                content=Response(False, result.message).to_json(),
                status_code=400
            )
    except Exception as e:
        log_exception(e)
        return JSONResponse(
            content=Response(False, "internal server error").to_json(),
            status_code=500
        )


#req 1.1
class UserCreateRequest(BaseModel):
    username: str
    email: str
    phone: str
    address: str
    Experience:float
    UserProfileID:int

@router.post("/CreateUser")
def CreateUserBoundary(data: UserCreateRequest):
    try:
        controller = CreateUserController()
        #print(data)
        # Your login logic here
        result = controller.CreateUserController(data.username,data.email,data.phone,data.Experience,data.address,data.UserProfileID)
        #print(result)
        return JSONResponse(Response(True,"Successfully created user").to_json())
    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate user?): {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"Username already exists").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error creating user").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )
    

#req 1.1 search
@router.get("/SearchUserAccount")
def SearchUserBoundary(searchTerm:str):
    try:
        controller = SearchUserController()
        result = controller.SearchUserController(searchTerm)
        if result is not None and len(result)>0:
            return JSONResponse(Response(True,[row.to_json() for row in result]).to_json())
        else:
            return JSONResponse(Response(False,None).to_json())

    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error searching user").to_json(),
            status_code=400
        )
    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )

#req 1.1 suspend
class ViewUserRequest(BaseModel):
    UserProfileID: int


@router.put("/SuspendUserAccount")
def SuspendUserBoundary(data: ViewUserRequest):
    try:
        controller = SuspendUserController()
        #print(data)
        # Your login logic here
        result = controller.suspendUserController(data.UserProfileID)
        #controller returns true if updated, false if not updated(in the case of no such user)
        if result:
            return JSONResponse(Response(True,"User Successfully suspended").to_json())
        else:
            return JSONResponse(
            content=Response(False,"No such user").to_json(),
            status_code=400
        )

    except psycopg2.IntegrityError as e:
        print(f"Integrity error: {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"database error").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"database error").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )


#req 1.2
@router.get("/ViewUserAccount")
def ViewUserBoundary(UserID:int):
    try:
        controller = ViewUserController()
        #print(data)
        # Your login logic here
        result = controller.ViewUserController(UserID)
        if result is not None:
            return JSONResponse(Response(True,result.to_json()).to_json())
        else:
            #print(result)
            return JSONResponse(Response(False,None).to_json())

    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate user?): {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"Username already exists").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error creating user").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )
    
#req 1.3
class UpdateUserRequest(BaseModel):
    username: str
    email: str
    phone: str
    IsActive:bool
    UserID:int
    address: str
    Experience:float
    UserProfileID:int

@router.put("/UpdateUserAccount")
def UpdateUserBoundary(data:UpdateUserRequest):
    try:
        controller = UpdateUserController()
        #print(data)
        # Your login logic here
        result = controller.updateUserController(data.username,data.email,data.phone,data.IsActive,data.UserProfileID,data.address,data.Experience,data.UserID)
        if result:
            return JSONResponse(Response(True,"successfully updated").to_json())
        else:
            #print(result)
            return JSONResponse(Response(True,"UserID does not exist").to_json())

    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate user?): {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"Username already exists").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error creating user").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )

