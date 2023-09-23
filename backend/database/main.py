from fastapi import FastAPI

from .containers import Container
from .routers.users import router
from .settings import get_url


app = FastAPI()


@app.on_event("startup")
async def start():
    container = Container()

    db_url = get_url()
    print(db_url)

    db = container.db_manager()
    db.init(db_url)
    await db.create_all()

    await container.session()
    await container.user_repository()
    return container


app.include_router(router)
