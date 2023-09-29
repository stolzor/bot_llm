from dependency_injector import containers, providers

from ..middlewares.spam import SpamMiddleware
from ..services.redis import RedisClient


class RedisContainers(containers.DeclarativeContainer):
    redis_client = providers.Singleton(RedisClient)

    spam_middlewares = providers.Factory(SpamMiddleware, redis_client=redis_client)
