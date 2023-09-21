from typing import Callable, AsyncContextManager

from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Users


class UsersRepository:
    def __init__(
        self, session: Callable[..., AsyncContextManager[AsyncSession]]
    ) -> None:
        self.session = session

    async def add(self) -> Users:
        username: str = "Test"
        user = Users(username=username)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return await user
