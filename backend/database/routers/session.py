from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from ..containers.services import Application
from ..schemas.session import Session, SessionCreate
from ..services.session import SessionService
from ..utils import orm2dict

router = APIRouter(tags=["session"])


@router.post("/session", response_model=Session)
@inject
async def create_session(
    session: SessionCreate,
    session_service: SessionService = Depends(
        Provide[Application.session.session_service]
    ),
):
    params = dict(session)
    params["user_date"] = params["user_date"].replace(tzinfo=None)

    checker = await session_service.get_session(**params) is not None
    if checker:
        raise HTTPException(status_code=400, detail="Session exists")

    return await session_service.create_session(**params)


@router.get("/session/{session_id}", response_model=Session)
@inject
async def get_session(
    session_id: int,
    session_service: SessionService = Depends(
        Provide[Application.session.session_service]
    ),
):
    params = dict(id=session_id)

    session = await session_service.get_session(**params)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    return session


@router.get("/session/", response_model=List[Session])
@inject
async def get_sessions(
    limit: int,
    session_service: SessionService = Depends(
        Provide[Application.session.session_service]
    ),
):
    params = dict(limit=limit)

    sessions = [i for i in await session_service.get_sessions(**params)]

    if sessions is None:
        raise HTTPException(status_code=404, detail="Session not found")

    return orm2dict(sessions)
