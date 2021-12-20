from ..db.connection import session
from ..schemas import *
from ..db.models import *


def getAllStudents():
    students = session.query(StudentsModel.id, StudentsModel.firstname, StudentsModel.lastname, StudentsModel.group_id).order_by(StudentsModel.id)
    return students


def getStudentById(id:int):
    student = session.query(StudentsModel.id, StudentsModel.firstname, StudentsModel.lastname, StudentsModel.group_id).filter(
        StudentsModel.id == id
        ).first()

    return student


def createNewStudent(student):
    new_student = StudentsModel(firstname=student.firstname, lastname=student.lastname, group_id=student.group)
    session.add(new_student)
    session.commit()
    return


def createALotOfStudents(students:ListStudentSchema):
    for student in students.__root__:
        new_student = StudentsModel(firstname=student.firstname, lastname=student.lastname, group_id=student.group)
        session.add(new_student)

    session.commit()
    return


def updateStudentById(id:int, student:StudentSchema):
    if student.firstname:
        session.query(StudentsModel).filter(
            StudentsModel.id == id
        ).update(
            {
                StudentsModel.firstname: student.firstname
            }
        )

    if student.lastname:
        session.query(StudentsModel).filter(
            StudentsModel.id == id
        ).update(
            {
                StudentsModel.lastname: student.lastname
            }
        )

    if student.group:
        session.query(StudentsModel).filter(
            StudentsModel.id == id
        ).update(
            {
                StudentsModel.group: student.group
            }
        )

    
    session.commit()
    return


def deleteStudentById(id:int):
    session.query(StudentsModel).filter (
        StudentsModel.id == id
    ).first().delete()
    session.commit()
    return
