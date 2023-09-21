import asyncio

from fastapi import FastAPI

from .containers import Container
from .routers.users import router
from .settings import Settings


settings = Settings()
url = settings.database_url.format(
    user=settings.user, password=settings.password, db_name=settings.db_name
)


async def main(container: Container) -> FastAPI:
    db = await container.session()
    await db


app = FastAPI()
container = Container()
app.container = asyncio.run_until_complete(main(container))
app.include_router(router)
