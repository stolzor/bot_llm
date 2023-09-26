from typing import AsyncContextManager, Callable, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.users import Users


class UsersRepository:
    def __init__(
        self, session: Callable[..., AsyncContextManager[AsyncSession]]
    ) -> None:
        self.session = session

    async def add(self, **kwargs) -> Users:
        user = Users(**kwargs)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get(self, **kwargs) -> Users:
        user = await self.session.get(Users, kwargs["id"])
        return user

    async def get_users(self, **kwargs) -> List[Users]:
        query = select(Users).limit(kwargs["limit"])
        users = await self.session.execute(query)
        return users
