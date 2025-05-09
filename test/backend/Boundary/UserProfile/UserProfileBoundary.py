
from fastapi.responses import JSONResponse
from controller.UserProfile.UserProfileController import *
from fastapi import APIRouter, Request

from pydantic import BaseModel
from utils.utils import log_exception
from Classes.Response import Response
import psycopg2

router = APIRouter()

#req 1.2 create UserProfile
class UserProfileCreateRequest(BaseModel):
    name:str
    privilege:str

@router.post("/CreateUserProfile")
def CreateUserProfileBoundary(data: UserProfileCreateRequest):
    try:
        controller = UserProfileCreateController()
        #print(data)
        # Your login logic here
        result = controller.createUserProfileController(data.name,data.privilege)
        #print(result)
        if result:
            return JSONResponse(Response(True,"Successfully created user Profile").to_json())
        else:
            #result is false, means not inserted       
            return JSONResponse(
                content=Response(False,"Error creating userProfile").to_json(),
                status_code=400
            )
    except psycopg2.IntegrityError as e:
        print(f"Integrity error (maybe duplicate profile name?): {e}")
        #log_exception(e)
        # maybe raise a custom DuplicateUserError()
        return JSONResponse(
            content=Response(False,"User Profile name already exists").to_json(),
            status_code=409
        )
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error creating userProfile").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        #log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )
    

#req 1.2 viewUserProfile
@router.get("/ViewUserProfile")
def ViewUserProfileBoundary(UserProfileID:int):
    try:
        controller = ViewUserProfileController()
        #print(data)
        # Your login logic here
        result = controller.viewUserProfileController(UserProfileID)
        print(result)
        if result is not None:
            return JSONResponse(Response(True,result.to_json()).to_json())
        else:
            print(result)
            return JSONResponse(Response(False,None).to_json())

   
    except psycopg2.Error as e:
        #log_exception(e)
        print(f"Database error: {e}")       
        return JSONResponse(
            content=Response(False,"Error finding profile").to_json(),
            status_code=400
        )


    except Exception as e:
        print("exception has occured")
        log_exception(e)
        return JSONResponse(
            content=Response(False,"internal server error").to_json(),
            status_code=505
        )





#req 1.2 update UserProfile
class UpdateUserProfileRequest(BaseModel):
    name:str
    privilege:str
    is_active:bool
    userprofileID:int
    


@router.put("/updateUserProfile")
def updateUserProfile(data: UpdateUserProfileRequest):
    try:
        controller = UpdateUserProfileController()
        #print(data)
        # Your login logic here
        result = controller.updateUserProfileController(data.name,data.privilege,data.is_active,data.userprofileID)
        #controller returns true if updated, false if not updated(in the case of no such user)
        if result:
            return JSONResponse(Response(True,"UserProfile Successfully updated").to_json())
        else:
            return JSONResponse(
            content=Response(False,"No such user Profile").to_json(),
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
#req 1.2 suspend user profile(entire group of users cannot use anymore)
class SuspendUserProfileRequest(BaseModel):
    UserProfileID: int


@router.put("/SuspendUserProfile")
def SuspendUserProfile(data: SuspendUserProfileRequest):
    try:
        controller = SuspendUserProfileController()
        #print(data)
        # Your login logic here
        result = controller.suspendUserProfileController(data.UserProfileID)
        #controller returns true if updated, false if not updated(in the case of no such user)
        if result:
            return JSONResponse(Response(True,"UserProfile Successfully suspended").to_json())
        else:
            return JSONResponse(
            content=Response(False,"No such user Profile").to_json(),
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

#req 1.2 search
@router.get("/SearchUserProfile")
def SearchUserProfile(searchTerm:str):
    try:
        controller = SearchUserProfileController()
        result = controller.searchUserProfileController(searchTerm)
        return JSONResponse(Response(True,[row.to_json() for row in result]).to_json())
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
    