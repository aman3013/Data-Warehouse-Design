from sqlalchemy.orm import Session
import models, schemas

# Create a new medical data entry
def get_medical_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MedicalData).offset(skip).limit(limit).all()

def create_medical_data(db: Session, channel_title: str, channel_username: str, message: str, date, media_path: str):
    db_data = models.MedicalData(
        channel_title=channel_title,
        channel_username=channel_username,
        message=message,
        date=date,
        media_path=media_path
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

