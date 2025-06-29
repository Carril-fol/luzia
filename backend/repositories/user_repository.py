from entities.user_entity import UserEntity
from repositories.repository import Repository

class UserRepository(Repository):
  
    def get_user_by_id(self, user_entity, id):
        return self.get_register_entity(user_entity, id)

    def get_users(self, user_entity):
        return self.get_registers_entity(user_entity)

    def create_user(self, user_entity_instance):
        return self.create_register_entity(user_entity_instance)
    
    def update_user(self, user_entity_instance):
        return self.update_register_entity(user_entity_instance)

    def delete_user(self, user_entity_instance):
        return self.delete_register_entity(user_entity_instance)