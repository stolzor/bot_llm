from ..crud.session import SessionRepository
from ..models.session import Session


class SessionService:
    def __init__(self, session_repository: SessionRepository) -> None:
        self._repository: SessionRepository = session_repository

    async def create_session(self, **kwargs) -> Session:
        return await self._repository.add(**kwargs)

    async def get_session(self, **kwargs) -> Session:
        return await self._repository.get(**kwargs)

    async def update_session(self, **kwargs) -> Session:
        return await self._repository.put(**kwargs)
