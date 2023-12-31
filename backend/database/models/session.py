from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import OrmBase


class Session(OrmBase):
    __tablename__ = "session"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user_message: Mapped[str] = mapped_column(String)
    user_date: Mapped[datetime] = mapped_column(DateTime)
    ai_message: Mapped[str] = mapped_column(String, nullable=True)
    ai_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    count_message: Mapped[int] = mapped_column(Integer, default=0)
