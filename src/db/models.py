from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *


Base = declarative_base()


class Teachers(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer(), primary_key=True, autoincrement=True)
    firstname = Column(String(length=50), nullable=False)
    lastname = Column(String(length=50), nullable=False)


class Students(Base):
    __tablename__ = "students"

    student_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    firstname = Column(String(length=50), nullable=False)
    lastname = Column(String(length=50), nullable=False)
    group_id = Column(Integer(), ForeignKey("groups.group_id"),primary_key=True)


class Subjects(Base):
    __tablename__ = "subjects"

    subject_id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(length=65), nullable=False)


class Groups(Base):
    __tablename__ = "groups"

    group_id = Column(Integer(), primary_key=True, autoincrement=True)
    group_name = Column(String(length=30), nullable=False)


class SubjectTeacher(Base):
    __tablename__ = "subject_teachers"

    subject_id = Column(Integer(), ForeignKey("subjects.subject_id"), primary_key=True)
    teacher_id = Column(Integer(), ForeignKey("teachers.teacher_id"), primary_key=True)
    group_id = Column(Integer(), ForeignKey("groups.group_id"), primary_key=True)


class Brands(Base):
    __tablename__ = "brands"

    brand_id = Column(Integer(), primary_key=True, autoincrement=True)
    brand_student_id = Column(Integer(), ForeignKey("students.student_id"), primary_key=True)
    brand_subject_id = Column(Integer(), ForeignKey("subjects.subject_id"), primary_key=True)
    brand_date = Column(Date(), nullable=False, default=datetime.now())