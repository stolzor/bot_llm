from dependency_injector import containers, providers

from .base import BaseContainer
from .session import SessionContainer
from .users import UsersContainer


class Application(containers.DeclarativeContainer):
    database = providers.Container(BaseContainer)

    users = providers.Container(UsersContainer, database=database)

    session = providers.Container(SessionContainer, database=database)
