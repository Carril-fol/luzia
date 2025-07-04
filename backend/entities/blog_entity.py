from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database.db import Base

class BlogEntity(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225))
    body = Column(Text)
    id_user = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserEntity")