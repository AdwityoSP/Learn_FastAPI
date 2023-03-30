from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import schemas
from sqlalchemy.orm import Session
from app.models.crud_db import Students
from app.configuration.database.databaseconfiguration import get_db

router = APIRouter()
@router.post('/create-new-student')
def create_new_student(request: schemas.Student, db: Session = Depends(get_db)):
    new_student = Students(name=request.name, age=request.age, classes=request.classes)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
