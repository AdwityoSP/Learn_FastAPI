from sqlalchemy import Column, Integer, String
from app.configuration.database.databaseconfiguration import Base

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement= True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    classes = Column(String, nullable=False)
