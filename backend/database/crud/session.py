from typing import AsyncContextManager, Callable

from sqlalchemy import and_, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.session import Session


class SessionRepository:
    def __init__(
        self, session: Callable[..., AsyncContextManager[AsyncSession]]
    ) -> None:
        self.session = session

    async def add(self, **kwargs) -> Session:
        session = Session(**kwargs)
        self.session.add(session)
        await self.session.commit()
        await self.session.refresh(session)
        return session

    async def get(self, **kwargs) -> Session:
        if "count_message" in kwargs.keys():
            expession = and_(
                Session.session_id == kwargs["session_id"],
                Session.count_message == kwargs["count_message"],
            )
        else:
            expession = Session.session_id == kwargs["session_id"]

        stmt = select(Session).where(expession)
        session = await self.session.execute(stmt)

        return session

    async def put(self, **kwargs) -> Session:
        session_id = kwargs["session_id"]
        count_message = kwargs["count_message"]
        del kwargs["session_id"], kwargs["count_message"]

        stmt = (
            update(Session)
            .where(
                and_(
                    Session.session_id == session_id,
                    Session.count_message == count_message,
                )
            )
            .values(**kwargs)
            .returning(Session)
        )

        session = await self.session.execute(stmt)
        session = session.first()

        if session is None:
            return None

        await self.session.commit()

        return session[0]
