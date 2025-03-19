from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, selectinload
from sqlalchemy import select
from src.database import engine, get_db
from src.models import Base, User, GameData
from src.schemas import UserCreate, UserResponse, GameDataCreate
from src.auth import create_access_token, get_current_user, verify_password, get_password_hash
from src.crud import create_user, create_game_data
import shutil
from typing import List

app = FastAPI()

# Ensure tables are created (not recommended for production, use Alembic instead)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/register/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_data = create_user(db, user)
    return user_data

@app.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(username)
    return {"token": token}

@app.post("/game/create/")
async def create_game_entry(data: GameDataCreate, image: UploadFile = File(...), db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    image_path = f"uploads/{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return await create_game_data(db, data, user.id)

@app.get("/game/geojson")
async def get_geojson(db: AsyncSession = Depends(get_db)):
    # Fetch game data with async session
    result = await db.execute(select(GameData).options(selectinload(GameData.user)))
    game_data: List[GameData] = result.scalars().all()

    # Convert database rows to GeoJSON format
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [game.longitude, game.latitude],
                },
                "properties": {
                    "id": game.id,
                    "title": game.title,
                    "description": game.description,
                    "game_genre": game.game_genre,
                    "game_type": game.game_type,
                    "number_players": game.number_players,
                    "play_time": game.play_time,
                    "first_released_location": game.first_released_location,
                    "first_published_year": game.first_published_year,
                    "image": game.image,
                    "user_id": game.user_id,
                },
            }
            for game in game_data
        ],
    }

    return geojson
