from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.configuration.localconfiguration import Settings

check = Settings()

database_url = f"mssql+pymssql://{check.db_user}:{check.db_password}@{check.db_server}/{check.db_name}" #MSSQL SERVER


engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()