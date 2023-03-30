from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name : str
    age : int
    classes : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    classes : Optional[str] = None