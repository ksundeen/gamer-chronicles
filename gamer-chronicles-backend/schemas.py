from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

class UserUpdate(BaseModel):
    email: Optional[str] = None

class GameDataCreate(BaseModel):
    latitude: float
    longitude: float
    title: str
    description: str

class GameDataUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
