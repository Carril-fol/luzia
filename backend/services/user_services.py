from werkzeug.security import generate_password_hash, check_password_hash

from .base_service import BaseService
from entities.user_entity import UserEntity
from repositories.user_repository import UserRepository
from models.user_model import CreateUserModel, AuthenticateUserModel, UserModel


class UserServices(BaseService):

    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user_by_email(self, data: dict):
        user = self._user_repository.get_user_by_email(data["email"])
        if not user:
            raise Exception("User not exists")
        
        return self._validate_entity_and_serialize(user, UserModel)
    
    def get_user_by_id(self, id):
        user = self._user_repository.get_user_by_id(UserEntity, id)
        if not user:
            raise Exception("User not exists")
        
        return self._validate_entity_and_serialize(user, UserModel)

    def authenticate_user(self, data: dict):
        auth_data = AuthenticateUserModel(**data)

        user = self._user_repository.get_user_by_email(data["email"])
        if not user:
            raise Exception("User not exists")
        
        if not check_password_hash(user.password, auth_data.password):
            raise Exception("Password not match")
        
        return user

    def create_user(self, data: dict):
        register_data = CreateUserModel(**data)
        hashed_password = generate_password_hash(register_data.password)
        register_data.password = hashed_password

        register_data_dict = register_data.model_dump(exclude={"confirm_password"})
        user_to_create = UserEntity(**register_data_dict)
        return self._user_repository.create_user(user_to_create)