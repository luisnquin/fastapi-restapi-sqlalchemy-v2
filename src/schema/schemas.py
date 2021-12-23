from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class GroupSchema(BaseModel):
    name:str


class GroupSchemaOpt(BaseModel):
    name:Optional[str]


class GroupSchemaArray(BaseModel):
    __root__: List[GroupSchema]


class TeacherSchema(BaseModel):
    firstname:str
    lastname:str


class TeacherSchemaOpt(BaseModel):
    firstname:Optional[str]
    lastname:Optional[str]


class TeacherSchemaArray(BaseModel):
    __root__: List[TeacherSchema]


class StudentSchema(BaseModel):
    firstname:str
    lastname:str
    group:int


class StudentSchemaOpt(BaseModel):
    firstname:Optional[str]
    lastname:Optional[str]
    group:Optional[int]


class StudentSchemaArray(BaseModel):
    __root__: List[StudentSchema]


class SubjectSchema(BaseModel):
    title:str


class SubjectSchemaArray(BaseModel):
    __root__: List[SubjectSchema]


class SubjectTeacherGroupSchema(BaseModel):
    subject_id:int
    teacher_id:int
    group_id:int
