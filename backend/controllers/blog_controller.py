from flask import request, make_response, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from pydantic import ValidationError

from repositories.blog_repository import BlogRepository
from repositories.user_repository import UserRepository

from services.blog_service import BlogService

from decorators.blog_decorator import is_blog_from_user

blog_repository = BlogRepository()
user_repository = UserRepository()

blog_service = BlogService(blog_repository, user_repository)
blog_controller = Blueprint("blog_controller", __name__, url_prefix="/blogs/api/v1")

@blog_controller.route("/create", methods=["POST"])
@jwt_required()
def create_blog():
    data = request.get_json()
    if not data:
        return {"error": "Missing JSON in request"}, 400
    try:
        user_id = get_jwt_identity()
        blog_service.create_blog(data, user_id)
        return make_response({"data": "Blog created"},201)
    except ValidationError as error:
        return {"error": error.errors()}, 400
    except Exception as error:
        return {"error": str(error)}, 400

@blog_controller.route("/get/<int:id>", methods=["GET"])
@jwt_required()
def get_blog(id: int):
    try:
        blog = blog_service.get_blog_by_id(id)
        return make_response({"data": blog}, 200)
    except Exception as error:
        return {"error": str(error)}, 400
    
@blog_controller.route("/all", methods=["GET"])
@jwt_required()
def get_blogs():
    try:
        blogs = list(blog_service.get_blogs())
        return make_response({"data": blogs}, 200)
    except Exception as error:
        return {"error": str(error)}, 400
    
@blog_controller.route("/delete/<int:id>", methods=["DELETE"])
@jwt_required()
@is_blog_from_user
def delete_blog(id: int):
    try:
        blog_service.delete_blog(id)
        return make_response({"data": "Blog deleted"})
    except Exception as error:
        return {"error": str(error)}, 400

@blog_controller.route("/update/<int:id>", methods=["PATCH", "PUT"])
@jwt_required()
@is_blog_from_user
def update_blog(id: int):
    data = request.get_json()
    if not data:
        return {"error": "Missing JSON in request"}, 400
    try:
        blog_service.update_blog(data, id)
        return make_response({"data": "Blog updated"})
    except ValidationError as error:
        return {"error": error.errors()}, 400
    except Exception as error:
        return {"error": str(error)}, 400
