from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from ..containers.services import Application
from ..schemas.users import User, UserCreate
from ..services.users import UserService
from ..utils import orm2dict

router = APIRouter(tags=["users"])


@router.post("/users", response_model=User)
@inject
async def create_user(
    user: UserCreate,
    user_service: UserService = Depends(Provide[Application.users.user_service]),
):
    params = dict(user)

    checker = await user_service.get_user(**params) is not None
    if checker:
        raise HTTPException(status_code=400, detail="User exists")

    return await user_service.create_user(**params)


@router.get("/users/{user_id}", response_model=User)
@inject
async def get_user(
    user_id: int,
    user_service: UserService = Depends(Provide[Application.users.user_service]),
):
    params = dict(id=user_id)

    user = await user_service.get_user(**params)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/users/", response_model=List[User])
@inject
async def get_users(
    limit: int,
    user_service: UserService = Depends(Provide[Application.users.user_service]),
):
    params = dict(limit=limit)

    users = [i for i in await user_service.get_users(**params)]

    if users is None:
        raise HTTPException(status_code=404, detail="User not found")

    return orm2dict(users)
