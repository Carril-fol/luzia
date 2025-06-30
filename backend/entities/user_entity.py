from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.db import Base

class UserEntity(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    date_register = Column(DateTime, default=datetime.now)