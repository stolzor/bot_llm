from dependency_injector import providers, containers

from .crud.users_repositories import UsersRepository
from .session_manager import DatabaseManager


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routers.users"])

    db = providers.Singleton(DatabaseManager)
    user_repository = providers.Factory(UsersRepository, session=db.provided.session)
