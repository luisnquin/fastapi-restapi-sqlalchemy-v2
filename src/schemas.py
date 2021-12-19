from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class GroupSchema(BaseModel):
    group_id:Optional[int]
    name:str


class TeachersSchema(BaseModel):
    firstname:str
    lastname:str


class StudentsSchema(BaseModel):
    firstname:str
    lastname:str
    group:int


class SubjectsSchema(BaseModel):
    subject_id:Optional[int]
    title:str


class SubjectTeacher(BaseModel):
    subject_id:TeachersSchema
    teacher_id:StudentsSchema
    group_id:GroupSchema


class BrandsSchema(BaseModel):
    brand_id:int
    student:StudentsSchema
    subject:SubjectsSchema
    date:datetime