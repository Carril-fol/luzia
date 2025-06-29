from sqlalchemy import Column, Integer, String, Time

from database.db import Base

class UserEntity(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    last_login = Column(Time)
    date_register = Column(Time)