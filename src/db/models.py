from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *


Base = declarative_base()


class TeachersModel(Base):
    __tablename__ = "teachers"

    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    firstname = Column(String(length=50), nullable=False)
    lastname = Column(String(length=60), nullable=False)


class StudentsModel(Base):
    __tablename__ = "students"

    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    firstname = Column(String(length=50), nullable=False)
    lastname = Column(String(length=60), nullable=False)
    group_id = Column(Integer(), ForeignKey("groups.id"), nullable=False, onupdate="cascade")


class GroupsModel(Base):
    __tablename__ = "groups"

    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    name = Column(String(length=30), nullable=False, unique=True)


class SubjectsModel(Base):
    __tablename__ = "subjects"

    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    title = Column(String(length=65), nullable=False, unique=True)


class SubjectTeacherModel(Base):
    __tablename__ = "subject_teachers"

    subject_id = Column(Integer(), ForeignKey("subjects.id"), primary_key=True, nullable=False, onupdate="cascade")
    teacher_id = Column(Integer(), ForeignKey("teachers.id"), primary_key=True, nullable=False, onupdate="cascade")
    group_id = Column(Integer(), ForeignKey("groups.id"), primary_key=True, nullable=False, onupdate="cascade")


class BrandsModel(Base):
    __tablename__ = "brands"

    brand_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    brand_student_id = Column(Integer(), ForeignKey("students.id"), primary_key=True, nullable=False, onupdate="cascade")
    brand_subject_id = Column(Integer(), ForeignKey("subjects.id"), primary_key=True, nullable=False, onupdate="cascade")
    brand_date = Column(Date(), nullable=False, default=datetime.now())