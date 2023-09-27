from dependency_injector import containers, providers

from ..crud.session import SessionRepository
from ..services.session import SessionService


class SessionContainer(containers.DeclarativeContainer):
    database = providers.DependenciesContainer()

    session_repository = providers.Factory(SessionRepository, session=database.session)
    session_service = providers.Factory(
        SessionService, session_repository=session_repository
    )
