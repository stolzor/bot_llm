from fastapi import FastAPI

from .containers import Container
from .routers import session, users
from .settings.database import ServiceDatabaseSettings

app = FastAPI()


@app.on_event("startup")
async def start():
    container = Container()
    # container.wire(modules=[__name__])

    settings = ServiceDatabaseSettings()
    db_url = settings.postgresql_url
    print(db_url)
    db = container.db_manager()
    db.init(db_url)
    await db.create_all()

    await container.session()

    await container.user_repository()
    await container.user_service()

    # await container.session_repository()
    # await container.session_service()

    app.container = container
    return container


app.include_router(users.router)
app.include_router(session.router)
