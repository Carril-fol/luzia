from functools import wraps
from flask_jwt_extended import get_jwt_identity

from repositories.blog_repository import BlogRepository
from repositories.user_repository import UserRepository

from services.blog_service import BlogService
from services.user_services import UserServices

blog_repository = BlogRepository()
user_repository = UserRepository()

blog_service = BlogService(blog_repository, user_repository)
user_service = UserServices(user_repository)

def is_blog_from_user(fn):
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            user_id_from_token = get_jwt_identity()
            user_instance = user_service.get_user_by_id(user_id_from_token)

            blog_id = kwargs.get("id")
            blog_instance = blog_service.get_blog_by_id(blog_id)

            if blog_instance.get("id_user") != user_instance.get("id"):
                return {"error": "Unauthorized access to this task"}, 403
            return fn(*args, **kwargs)
        except Exception as error:
            return {"error": (str(error))}, 400
    return wrapper