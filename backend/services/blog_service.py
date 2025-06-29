from entities.blog_entity import BlogEntity
from entities.user_entity import UserEntity

from models.blog_model import CreateBlogModel, BlogModel, UpdateBlogModel

from repositories.blog_repository import BlogRepository
from repositories.user_repository import UserRepository

from services.base_service import BaseService


class BlogService(BaseService):
    
    def __init__(self, blog_repository: BlogRepository, user_repository: UserRepository):
        self._blog_repository = blog_repository
        self._user_repository = user_repository

    def _get_user_by_id(self, id_user):
        user = self._user_repository.get_user_by_id(UserEntity, id_user)
        if not user:
            raise Exception("User not found")
        
        return user

    def create_blog(self, data: dict, user_id):
        user = self._get_user_by_id(user_id)
        data["id_user"] = user.id

        blog_data = CreateBlogModel(**data)
        blog_data_dict = blog_data.model_dump()
        
        blog_entity = BlogEntity(**blog_data_dict)
        return self._blog_repository.create_blog(blog_entity)
    
    def get_blog_by_id(self, id):
        blog = self._blog_repository.get_blog_by_id(BlogEntity, id)
        if not blog:
            raise Exception("Blog not found")
        
        return self._validate_entity_and_serialize(blog, BlogModel)
    
    def get_blogs(self):
        blogs = self._blog_repository.get_blogs(BlogEntity)
        for blog in blogs:
            yield self._validate_entity_and_serialize(blog, BlogModel)

    def delete_blog(self, id: int):
        blog = self._blog_repository.get_blog_by_id(BlogEntity, id)
        if not blog:
            raise Exception("Blog not found")
        
        return self._blog_repository.delete_blog(blog)
    
    def update_blog(self, data: dict, id: int):
        blog = self._blog_repository.get_blog_by_id(BlogEntity, id)
        if not blog:
            raise Exception("Blog not found")
        
        blog_updated = self._prepare_to_entity(data, UpdateBlogModel, blog)
        return self._blog_repository.update_blog(blog_updated)
