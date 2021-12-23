from pydantic import BaseModel
from typing import List, Optional


class GroupSchema(BaseModel):
    name:str


class GroupSchemaOpt(BaseModel):
    name:Optional[str]


class GroupSchemaList(BaseModel):
    __root__:List[GroupSchema]


class TeacherSchema(BaseModel):
    firstname:str
    lastname:str


class TeacherSchemaOpt(BaseModel):
    firstname:Optional[str]
    lastname:Optional[str]


class TeacherSchemaList(BaseModel):
    __root__:List[TeacherSchema]


class StudentSchema(BaseModel):
    firstname:str
    lastname:str
    group:int


class StudentSchemaOpt(BaseModel):
    firstname:Optional[str]
    lastname:Optional[str]
    group:Optional[int]


class StudentSchemaList(BaseModel):
    __root__:List[StudentSchema]


class SubjectSchema(BaseModel):
    title:str


class SubjectSchemaList(BaseModel):
    __root__:List[SubjectSchema]


class AssociationSchema(BaseModel):
    subject_id:int
    teacher_id:int
    group_id:int


class AssociationSchemaOpt(BaseModel):
    subject_id:Optional[int]
    teacher_id:Optional[int]
    group_id:Optional[int]


class AssociationSchemaList(BaseModel):
    __root__:List[AssociationSchema]