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
        async with self.session as session:
            user = Users(username=username)
            await session.add(user)
            await session.commit()
            await session.refresh(user)
            return await user
