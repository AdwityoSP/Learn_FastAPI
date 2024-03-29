from fastapi import FastAPI, Path
from app.schemas import schemas
from typing import Optional

app = FastAPI()
students = {
    1: {
        "name": "John",
        "age": 18,
        "classes": "12-A"},
    2: {
        "name": "Zahra",
        "age": 17,
        "classes": "12-B"     
    }
}

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="Student ID", gt=0)):
    return students[student_id]

@app.get("/get-student-by-name")
def get_student_by_name(student_name: Optional[str]):
    for i in students:
        if students[i]["name"] == student_name:
            return students[i]
    return {"Data":"Not Found"}
    
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student:schemas.Student):
    if student_id in students:
        return {"Error" : "Data already exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student:schemas.UpdateStudent):
    if student_id not in students:
        return {"Error" : "Data not exist"}
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.classes != None:
        students[student_id]["classes"] = student.classes
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error": "Data not found"}
    del students[student_id]
    return {"Message": "Student deleted"}