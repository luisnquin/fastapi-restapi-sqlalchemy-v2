from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Groups(BaseModel):
    group_id:Optional[int]
    name:str


class Teachers(BaseModel):
    teacher_id:Optional[int]
    firstname:str
    lastname:str
    group:Groups


class Students(BaseModel):
    student_id:Optional[int]
    firstname:str
    lastname:str


class Subjects(BaseModel):
    subject_id:Optional[int]
    title:str


class SubjectTeacher(BaseModel):
    subject_id:Teachers
    teacher_id:Students
    group_id:Groups


class Brands(BaseModel):
    brand_id:int
    student:Students
    subject:Subjects
    date:datetime