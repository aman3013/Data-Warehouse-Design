from pydantic import BaseModel
from datetime import datetime

# Schema for creating new data entries
class MedicalDataCreate(BaseModel):
    channel_title: str
    channel_username: str
    message: str
    date: datetime
    media_path: str

# Schema for representing data (includes id field)
class MedicalData(BaseModel):
    id: int
    channel_title: str
    channel_username: str
    message: str
    date: datetime
    media_path: str

    class Config:
        from_attributes = True  # This ensures compatibility with SQLAlchemy models
