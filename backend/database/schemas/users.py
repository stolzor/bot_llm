from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str


class UserCreate(UserBase):
    ...


class User(UserBase):
    trime_created: datetime
    is_active: bool

    class Config:
        from_attributes = True
