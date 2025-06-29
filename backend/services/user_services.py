from werkzeug.security import generate_password_hash, check_password_hash

from .base_service import BaseService
from entities.user_entity import UserEntity
from repositories.user_repository import UserRepository
from models.user_model import CreateUserModel


class UserServices(BaseService):

    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def create_user(self, data: dict):
        validated_data = self._prepare_to_entity(data, CreateUserModel).model_dump()
        validated_data["password"] = generate_password_hash(data["password"])
        validated_data.pop("confirm_password", None)

        user_to_create = UserEntity(**validated_data)
        return self._user_repository.create_user(user_to_create)