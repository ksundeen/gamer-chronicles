from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://admin:adminpass@localhost/gamer_chronicles"

# Create database engine
engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

# Dependency to get DB session
async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
