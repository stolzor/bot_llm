from typing import AsyncContextManager, Callable

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
        user = await self.session.get(Session, kwargs["id"])
        return user
