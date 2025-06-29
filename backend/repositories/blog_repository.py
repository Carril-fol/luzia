from entities.blog_entity import BlogEntity
from repositories.repository import Repository

class BlogRepository(Repository):
  
    def get_blog_by_id(self, blog_entity, id):
        return self.get_register_entity(blog_entity, id)

    def get_blogs(self, blog_entity):
        return self.get_registers_entity(blog_entity)

    def create_blog(self, blog_entity_instance):
        return self.create_register_entity(blog_entity_instance)
    
    def update_blog(self, blog_entity_instance):
        return self.update_register_entity(blog_entity_instance)

    def delete_blog(self, blog_entity_instance):
        return self.delete_register_entity(blog_entity_instance)