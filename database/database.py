from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings

engine = create_async_engine(
    settings.DataBase_URL
)

session = async_sessionmaker(engine, class_=AsyncSession)


class Base(DeclarativeBase):
    pass