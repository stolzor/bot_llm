from ..crud.session import SessionRepository
from ..models.session import Session


class SessionService:
    def __init__(self, service_repository: SessionRepository) -> None:
        self._repository: SessionRepository = service_repository

    async def create_session(self, **kwargs) -> Session:
        return await self._repository.add(**kwargs)

    async def get_session(self, **kwargs) -> Session:
        return await self._repository.get(**kwargs)

    async def get_sessions(self, **kwargs) -> Session:
        return await self._repository.get_users(**kwargs)
