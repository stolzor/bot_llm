from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from ..crud.users_repositories import UsersRepository
from ..containers import Container
from ..settings import Settings


router = APIRouter()


@router.on_event("startup")
async def start():
    container = Container()

    settings = Settings()

    db_url = settings.database_url.format(
        user="postgres", password=settings.password, db_name="postgres"
    )
    db = container.db_manager()
    db.init(db_url)
    await db.create_all()

    await container.session()
    await container.user_repository()
    return container


@router.post("/users")
@inject
async def create_user(
    user_repository: UsersRepository = Depends(Provide[Container.user_repository]),
):
    return await user_repository.add()
