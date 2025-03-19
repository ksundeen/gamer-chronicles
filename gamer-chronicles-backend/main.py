from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base
from schemas import UserCreate, UserResponse, GameDataCreate, GameDataUpdate
from auth import create_access_token, get_current_user, verify_password, get_password_hash
from crud import create_user, create_game_data
import shutil

app = FastAPI()

Base.metadata.create_all(bind=engine)

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
def create_game_entry(data: GameDataCreate, image: UploadFile = File(...), db: Session = Depends(get_db), user=Depends(get_current_user)):
    image_path = f"uploads/{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return create_game_data(db, data, user.id)

@app.get("/game/")
def get_game_data(db: Session = Depends(get_db)):
    return db.query(GameData).all()
