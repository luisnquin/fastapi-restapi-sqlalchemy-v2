from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class GroupSchema(BaseModel):
    name:str


class ListGroupSchema(BaseModel):
    __root__: List[GroupSchema]


class TeacherSchema(BaseModel):
    firstname:str
    lastname:str


class ListTeacherSchema(BaseModel):
    __root__: List[TeacherSchema]


class StudentSchema(BaseModel):
    firstname:str
    lastname:str
    group:int


class ListStudentSchema(BaseModel):
    __root__: List[StudentSchema]


class SubjectSchema(BaseModel):
    title:str


class ListSubjectSchema(BaseModel):
    __root__: List[SubjectSchema]


class SubjectTeacher(BaseModel):
    subject_id:int
    teacher_id:int
    group_id:int


class BrandsSchema(BaseModel):
    student:int
    subject:int
    date:datetime