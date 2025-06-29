from datetime import time, datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator, EmailStr, model_validator, ConfigDict

class UserModel(BaseModel):
    id: int = Field(default=None, description="ID of the user")
    username: str = Field(default=None, description="Username from the user")
    first_name: str
    last_name: str


class CreateUserModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str = Field(default=None, description="Username from the user")
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    confirm_password: str
    date_register: Optional[datetime] = Field(default=datetime.now())

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(character.isupper() for character in value):
            raise ValueError('Password must contain at least one uppercase letter')
        return value

    @model_validator(mode="after")
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    

class AuthenticateUserModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    email: EmailStr
    password: str