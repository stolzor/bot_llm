from fastapi import FastAPI

from .containers import Container
from .routers.users import router


app = FastAPI()
container = Container()
app.include_router(router)
