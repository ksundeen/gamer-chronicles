from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    game_data = relationship("GameData", back_populates="user")  # Relationship to GameData

class GameData(Base):
    __tablename__ = "game_data"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    title = Column(String, nullable=False)
    game_genre = Column(ARRAY(String), nullable=False)  # Storing lists using ARRAY
    game_type = Column(ARRAY(String), nullable=False)
    number_players = Column(ARRAY(String), nullable=False)
    play_time = Column(ARRAY(String), nullable=False)
    description = Column(String)
    first_released_location = Column(String)
    first_published_year = Column(Integer, nullable=False)
    image = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="game_data")  # Link to User
