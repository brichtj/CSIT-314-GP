from fastapi import APIRouter
from pydantic import BaseModel
from controller.UserAdmin.SearchUserController import SearchUserController

router = APIRouter()
controller = SearchUserController()

class SearchUserRequest(BaseModel):
    search_term: str

@router.post("/SearchUsers")
def search_user(request: SearchUserRequest):
    return controller.search_user(request.search_term)
