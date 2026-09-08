from fastapi import APIRouter, Depends, status
from app.api.deps import get_user_service
from app.schemas.user import UserCreate, UserResponse
from app.services import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    user_data : UserCreate,
    user_service : UserService = Depends(get_user_service)
):
    return user_service.register_user(user_data)

@router.get("/", response_model=UserResponse)
def get_user(
    user_id : int,
    user_service : UserService = Depends(get_user_service)
):
    return user_service.get_user_by_id(user_id)

