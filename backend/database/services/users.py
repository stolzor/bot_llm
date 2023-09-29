from ..crud.users import UsersRepository
from ..models.users import Users


class UserService:
    def __init__(self, user_repository: UsersRepository) -> None:
        self._repository: UsersRepository = user_repository

    async def create_user(self, **kwargs) -> Users:
        return await self._repository.add(**kwargs)

    async def get_user(self, **kwargs) -> Users:
        return await self._repository.get(**kwargs)
