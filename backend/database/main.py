from fastapi import FastAPI

# from .containers import Container
from .containers.services import Application
from .routers import session, users
from .settings.database import ServiceDatabaseSettings

app = FastAPI()


@app.on_event("startup")
async def start():
    settings = ServiceDatabaseSettings()
    db_url = settings.postgresql_url

    container = Application()

    db = container.database.db_manager()
    db.init(db_url)
    await db.create_all()

    await container.database.session()

    container.wire(modules=[".routers.users", ".routers.session"])

    app.container = container
    return container


app.include_router(users.router)
app.include_router(session.router)
