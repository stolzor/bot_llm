from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from ..crud.users_repositories import UsersRepository
from ..containers import Container


router = APIRouter()


@router.post("/users")
@inject
async def create_user(
    user_repository: UsersRepository = Depends(Provide[Container.user_repository]),
):
    return await user_repository.add()
