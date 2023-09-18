import contextlib
from typing import AsyncIterator, Optional, Dict

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from .settings import Settings

# TODO: Add logging
class DatabaseManager:
    def __init__(self) -> None:
        self._engine: Optional[AsyncEngine] = None
        self._sessionmaker: Optional[async_sessionmaker] = None
    
    def init(self, db_url: str) -> None:
        self._engine = create_async_engine(
            url=db_url,
            pool_pre_ping=True,
        )
        
        self._sessionmaker = async_sessionmaker(
            bind=self._engine,
            expire_on_commit=False
        )

    async def close(self) -> None:
        if self._engine is None:
            return
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None
    
    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise IOError("DatabaseManager is not initialized")
        async with self._sessionmaker() as session:
            try:
                yield session
            except Exception as e:
                print('qwew')
                await session.rollback()
                raise e
    
    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise IOError("DatabaseManager is not initialized")
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception as e:
                await connection.rollback()
                raise e


async def get_session(db_manager: DatabaseManager) -> AsyncIterator[AsyncSession]:
    async with db_manager.session() as session:
        yield session
        

async def get_connect(db_manager: DatabaseManager) -> AsyncIterator[AsyncConnection]:
    async with db_manager.connect() as connect:
        yield connect


if __name__ == "__main__":
    db_manager = DatabaseManager()
    settings = Settings()
    url = settings.database_url.format(
        user=settings.user,
        password=settings.password,
        db_name=settings.db_name
        )
    db_manager.init(url)
    
