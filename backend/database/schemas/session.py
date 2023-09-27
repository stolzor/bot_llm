from datetime import datetime

from pydantic import BaseModel


class SessionBase(BaseModel):
    id: int
    session_id: int


class SessionCreate(SessionBase):
    user_message: str
    user_date: datetime
    user_id: int


class SessionUpdate(SessionBase):
    ai_message: str | None
    ai_date: datetime | None


class Session(SessionCreate, SessionUpdate):
    ...

    class Config:
        from_attributes = True
