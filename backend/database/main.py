from fastapi import FastAPI

from .containers import Container
from .routers.users import router
from .settings.database import ServiceDatabaseSettings


app = FastAPI()


@app.on_event("startup")
async def start():
    container = Container()

    settings = ServiceDatabaseSettings()
    db_url = settings.postgresql_url

    db = container.db_manager()
    db.init(db_url)
    await db.create_all()

    await container.session()
    await container.user_repository()
    return container


app.include_router(router)
