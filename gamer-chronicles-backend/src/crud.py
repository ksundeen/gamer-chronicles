from sqlalchemy.ext.asyncio import AsyncSession
from src.models import User, GameData
from src.schemas import UserCreate, GameDataCreate
from src.auth import get_password_hash

async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def create_game_data(db: AsyncSession, data: GameDataCreate, user_id: int):
    game_entry = GameData(**data.dict(), user_id=user_id)
    db.add(game_entry)
    await db.commit()
    await db.refresh(game_entry)
    return game_entry
