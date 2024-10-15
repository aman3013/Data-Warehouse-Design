import sys
import os
sys.path.append("app/")
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database
from datetime import datetime
from database import SessionLocal, engine, get_db

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Welcome to the Medical Data API"}

# Create new medical data entry
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/medical_data/")
def read_medical_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    medical_data = crud.get_medical_data(db, skip=skip, limit=limit)
    return medical_data

@app.post("/medical_data/")
def create_medical_data(channel_title: str, channel_username: str, message: str, date: str, media_path: str, db: Session = Depends(get_db)):
    # Convert string date to datetime object
    date_obj = datetime.fromisoformat(date)
    return crud.create_medical_data(db, channel_title, channel_username, message, date_obj, media_path)

