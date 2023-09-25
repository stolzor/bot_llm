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
    print(db_url)
    db = container.db_manager()
    db.init(db_url)
    await db.create_all()

    await container.session()
    await container.user_repository()
    await container.user_service()

    app.container = container
    return container


app.include_router(router)
