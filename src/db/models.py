from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


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
    group_id = Column(Integer(), ForeignKey("groups.id", ondelete=None, onupdate="CASCADE"), nullable=False)


class GroupsModel(Base):
    __tablename__ = "groups"

    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    name = Column(String(length=30), nullable=False, unique=True)


class SubjectsModel(Base):
    __tablename__ = "subjects"

    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    title = Column(String(length=65), nullable=False, unique=True)


class SubjectTeacherGroupModel(Base):
    __tablename__ = "subject_teachers_groups"

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False, unique=True)
    subject_id = Column(Integer(), ForeignKey("subjects.id"), primary_key=True, nullable=False)
    teacher_id = Column(Integer(), ForeignKey("teachers.id"), primary_key=True, nullable=False)
    group_id = Column(Integer(), ForeignKey("groups.id"), primary_key=True, nullable=False)
