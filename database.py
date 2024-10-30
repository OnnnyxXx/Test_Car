from typing import AsyncGenerator
from sqlalchemy import MetaData, NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import logging

logging.basicConfig(level=logging.INFO)

DATABASE_URL = "postgresql+asyncpg://postgres_user:postgres_password@localhost:5432/postgres_db"

Base = declarative_base()
metadata = MetaData()

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise
