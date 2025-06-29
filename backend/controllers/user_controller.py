from flask import request, make_response, Blueprint

from repositories.user_repository import UserRepository
from services.user_services import UserServices

user_repository = UserRepository()
user_service = UserServices(user_repository)
user_controller = Blueprint("user_controller", __name__, url_prefix="/users/api/v1")

@user_controller.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    try:
        user_service.create_user(data)
        return make_response({"msg": "User created successfully"}, 201)
    except Exception as error:
        return make_response({"msg": str(error)}, 400)