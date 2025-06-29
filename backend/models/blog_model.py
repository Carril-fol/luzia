from typing import Optional
from pydantic import BaseModel, ConfigDict

class BlogModel(BaseModel):
    id: int
    title: str
    body: str
    id_user: int


class CreateBlogModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    body: str
    id_user: int


class UpdateBlogModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: Optional[str] = None
    body: Optional[str] = None