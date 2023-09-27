from dependency_injector import containers, providers

from ..session_manager import DatabaseManager, get_session


class BaseContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_manager = providers.Singleton(DatabaseManager)
    session = providers.Resource(get_session, db_manager=db_manager)
