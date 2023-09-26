from dependency_injector import containers, providers

from ..crud.session import SessionRepository
from ..services.session import SessionService


class SessionContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    session = providers.DependenciesContainer()

    session_repository = providers.Factory(SessionRepository, session=session)
    session_service = providers.Factory(
        SessionService, session_repository=session_repository
    )
