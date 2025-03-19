from pydantic import BaseModel
from typing import Optional, List

### 🔹 User Schemas ###
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True  # ✅ Enables ORM mode for SQLAlchemy

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None  # ✅ Allow updating password

### 🔹 GameData Schemas ###
class GameDataCreate(BaseModel):
    latitude: float
    longitude: float
    title: str
    description: Optional[str] = None
    game_genre: List[str]  # ✅ Matches `ARRAY(String)` in the database
    game_type: List[str]
    number_players: List[str]
    play_time: List[str]
    first_released_location: Optional[str] = None
    first_published_year: int
    image: Optional[str] = None  # ✅ Allow optional image

class GameDataResponse(BaseModel):
    id: int
    latitude: float
    longitude: float
    title: str
    description: Optional[str] = None
    game_genre: List[str]
    game_type: List[str]
    number_players: List[str]
    play_time: List[str]
    first_released_location: Optional[str] = None
    first_published_year: int
    image: Optional[str] = None
    user_id: int

    class Config:
        from_attributes = True  # ✅ Enables ORM mode for SQLAlchemy

class GameDataUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    game_genre: Optional[List[str]] = None
    game_type: Optional[List[str]] = None
    number_players: Optional[List[str]] = None
    play_time: Optional[List[str]] = None
    first_released_location: Optional[str] = None
    first_published_year: Optional[int] = None
    image: Optional[str] = None
