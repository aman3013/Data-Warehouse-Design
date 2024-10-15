from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class MedicalData(Base):
    __tablename__ = "medical_data"

    ID = Column(Integer, primary_key=True, index=True)
    Channel_Title = Column(String, index=True)
    Channel_Username = Column(String, index=True)
    Message = Column(String)
    Date = Column(DateTime)
    Media_Path = Column(String, index=True)
