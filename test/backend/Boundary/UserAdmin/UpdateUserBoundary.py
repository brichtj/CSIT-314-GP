from fastapi import APIRouter
from pydantic import BaseModel
from controller.UserAdmin.UpdateUserController import UpdateUserController
from fastapi.responses import JSONResponse
from Classes.Response import Response

router = APIRouter()

class UpdateUserRequest(BaseModel):
    username: str
    updated_data: dict  # Accepts a dictionary of fields to update

@router.post("/UpdateUserAccount")
def update_user_account(data: UpdateUserRequest):
    controller = UpdateUserController()
    success = controller.update_user(data.username, data.updated_data)

    if success:
        return JSONResponse(Response(True, "User updated successfully").to_json())
    else:
        return JSONResponse(Response(False, "User not found or update failed").to_json())
