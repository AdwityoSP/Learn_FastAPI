from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import schemas
from sqlalchemy.orm import Session
from app.models.crud_db import Students
from app.configuration.database.databaseconfiguration import get_db

router = APIRouter()

@router.post('/create-new-student', status_code = 201)
def create_new_student(request: schemas.Student, db: Session = Depends(get_db)):
    new_student = Students(
        name=request.name, age=request.age, classes=request.classes)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
    
@router.get('/get-all-student', status_code= 200)
def get_all_student(db: Session = Depends(get_db)):
    all_student = db.query(Students).all()
    if all_student == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return all_student

@router.get('/get-student/{student_id}', status_code= 200)
def get_student_by_id(student_id, db:Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == student_id).first()
    if student == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return  student

@router.delete('/delete-student{student_id}', status_code=status.HTTP_202_ACCEPTED)
def delete_student(student_id, db: Session = Depends(get_db)):
    erease_student = db.query(Students).filter(Students.id == student_id).delete(synchronize_session=False)
    if erease_student == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    db.commit()
    return  erease_student

@router.put('/update-student{student_id}', status_code=status.HTTP_202_ACCEPTED)
def update_student(student_id, req:schemas.Student, db:Session =Depends(get_db)):
    edit_student = db.query(Students).filter(Students.id == student_id)
    if edit_student == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    edit_student.update(req.dict())
    db.commit()
    return  "student updated successfully"

