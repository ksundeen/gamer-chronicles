from sqlalchemy.orm import Session
from models import User, GameData
from schemas import UserCreate, GameDataCreate
from auth import get_password_hash

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_game_data(db: Session, data: GameDataCreate, user_id: int):
    game_entry = GameData(**data.dict(), user_id=user_id)
    db.add(game_entry)
    db.commit()
    db.refresh(game_entry)
    return game_entry
