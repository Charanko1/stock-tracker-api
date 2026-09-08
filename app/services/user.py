from app.core.exceptions import BadRequestException, NotFoundException
from app.core.security import get_password_hash
from app.models.user import User
from app.repositories import UserRepository
from app.schemas.user import UserCreate

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, user_data: UserCreate) -> User:
        existing_user = self.user_repo.get_by_email(user_data.email)
        if existing_user:
            raise BadRequestException("Email sudah terdaftar")

        hashed_pwd = get_password_hash(user_data.password)
        new_user = User(email=user_data.email, password=hashed_pwd)
        return self.user_repo.create(new_user)

    def get_user_by_id(self, user_id : int) -> User:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise NotFoundException("User tidak ditemukan")
        return user