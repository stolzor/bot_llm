from fastapi import FastAPI

from .containers import Container
from .routers.users import router
from .settings import Settings


settings = Settings()
url = settings.database_url.format(
    user=settings.user, password=settings.password, db_name=settings.db_name
)


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.init(url)
    print("Init complete!")
    app = FastAPI()
    app.container = container
    app.include_router(router)
    return app


app = create_app()
