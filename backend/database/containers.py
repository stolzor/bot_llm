from dependency_injector import providers, containers

from .crud.users_repositories import UsersRepository
from .session_manager import get_session, db_manager


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routers.users"])

    session = providers.Resource(get_session, db_manager=db_manager)
    user_repository = providers.Factory(UsersRepository, session=session)
