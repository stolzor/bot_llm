from dependency_injector import containers, providers

from ..crud.users import UsersRepository
from ..services.users import UserService


class UsersContainer(containers.DeclarativeContainer):
    database = providers.DependenciesContainer()

    user_repository = providers.Factory(UsersRepository, session=database.session)
    user_service = providers.Factory(UserService, user_repository=user_repository)
