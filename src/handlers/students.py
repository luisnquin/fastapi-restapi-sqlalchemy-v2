from ..db.connection import session
from ..schemas import *
from ..db.models import *


def getAllStudents():
    students = session.query(StudentsModel.id, StudentsModel.firstname, StudentsModel.lastname, StudentsModel.group_id).order_by(StudentsModel.id)
    return students


def getStudentById(id:int):
    student = session.query(StudentsModel.id, StudentsModel.firstname, StudentsModel.lastname, StudentsModel.group_id).filter(
        StudentsModel == id
        ).first()

    return student


def createNewStudent(student):
    new_student = StudentsModel(firstname=student.firstname, lastname=student.lastname, group_id=student.group)
    session.add(new_student)
    session.commit()
    return
