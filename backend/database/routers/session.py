from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from ..containers.services import Application
from ..schemas.session import Session, SessionCreate, SessionUpdate
from ..services.session import SessionService

router = APIRouter(tags=["session"])


@router.post("/api/v1/session", response_model=Session)
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
        raise HTTPException(status_code=400, detail="Number message exists")

    return await session_service.create_session(**params)


@router.put("/api/v1/session", response_model=Session)
@inject
async def update_session(
    session: SessionUpdate,
    session_service: SessionService = Depends(
        Provide[Application.session.session_service]
    ),
):
    params = dict(session)
    params["ai_date"] = params["ai_date"].replace(tzinfo=None)

    checker = await session_service.get_session(**params)

    if checker.first() is None:
        raise HTTPException(
            status_code=404, detail="Session or number message no exists"
        )

    update = await session_service.update_session(**params)

    return update


@router.get("/api/v1/session/{session_id}", response_model=Session | List[Session])
@inject
async def get_session(
    session_id: int,
    session_service: SessionService = Depends(
        Provide[Application.session.session_service]
    ),
):
    params = dict(session_id=session_id)

    session = await session_service.get_session(**params)
    session = [i[0] for i in session]

    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    return session
