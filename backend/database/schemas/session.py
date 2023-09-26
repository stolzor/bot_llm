from datetime import datetime

from pydantic import BaseModel


class SessionBase(BaseModel):
    id: int
    session_id: int


class SessionCreate(SessionBase):
    user_message: str
    user_date: datetime


class SessionUpdate(SessionBase):
    ai_message: str
    ai_date: datetime


class Session(SessionCreate, SessionUpdate):
    ...

    class Config:
        from_attributes = True
