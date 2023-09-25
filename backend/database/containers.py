from dependency_injector import containers, providers

from .crud.users import UsersRepository
from .services.users import UserService
from .session_manager import DatabaseManager, get_session


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routers.users"])

    db_manager = providers.Singleton(DatabaseManager)
    session = providers.Resource(get_session, db_manager=db_manager)

    user_repository = providers.Factory(UsersRepository, session=session)
    user_service = providers.Factory(UserService, user_repository=user_repository)
