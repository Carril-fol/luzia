from flask import request, make_response, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies

from repositories.user_repository import UserRepository
from services.user_services import UserServices

user_repository = UserRepository()
user_service = UserServices(user_repository)
user_controller = Blueprint("user_controller", __name__, url_prefix="/users/api/v1")


@user_controller.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    if not data:
        return {"error": "Missing JSON in request"}, 400
    try:
        user_service.create_user(data)
        user_data = user_service.get_user_by_email(data)
        access_token = create_access_token(user_data)
        refresh_token = create_refresh_token(user_data)
        response = make_response({"msg": "User created successfully"}, 201)
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response
    except Exception as error:
        return make_response({"error": str(error)}, 400)
    
@user_controller.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    if not data:
        return {"error": "Missing JSON in request"}, 400
    try:
        user = user_service.authenticate_user(data)
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=str(user.id))
        response = make_response({"msg": "User logged successfully"}, 200)
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response
    except Exception as error:
        return make_response({"msg": str(error)}, 400)
    
@user_controller.route("/logout", methods=["POST"])
def logout_user():
    try:
        response = make_response(({"msg": "Logout succesfully"}), 200)
        unset_jwt_cookies(response)
        return response
    except Exception as error:
        return {"error": (str(error))}, 400