from ..db.connection import session
from ..schema.schemas import StudentSchema, StudentSchemaOpt, StudentSchemaArray
from ..db.models import StudentsModel


def getAllStudents():
    students = session.query(StudentsModel.id, StudentsModel.firstname, StudentsModel.lastname, StudentsModel.group_id).order_by(
        StudentsModel.id)

    return [student for student in students]


def getStudentById(id:int):
    student = session.query(StudentsModel.id, StudentsModel.firstname, StudentsModel.lastname, StudentsModel.group_id).filter(
        StudentsModel.id == id
    ).first()

    return student


def createNewStudent(request:StudentSchema):
    student = StudentsModel(firstname=request.firstname, lastname=request.lastname, group_id=request.group)
    session.add(student)
    session.commit()
    return


def createALotOfStudents(request:StudentSchemaArray):
    for student in request.__root__:
        new_student = StudentsModel(firstname=student.firstname, lastname=student.lastname, group_id=student.group)
        session.add(new_student)

    session.commit()
    return


def modifyStudentByid(request:StudentSchemaOpt, id:int):
    if request.firstname:
        session.query(StudentsModel)\
            .filter(StudentsModel.id == id)\
            .update(
            {
                StudentsModel.firstname: request.firstname
            }
        )
        session.commit()
        return

    if request.lastname:
        session.query(StudentsModel)\
            .filter(StudentsModel.id == id)\
            .update(
            {
                StudentsModel.lastname: request.lastname
            }
        )
        session.commit()
        return

    if request.group:
        session.query(StudentsModel)\
            .filter(StudentsModel.id == id)\
            .update(
            {
                StudentsModel.group: request.group
            }
        )
        session.commit()
        return
    
    return True


def updateStudentById(request:StudentSchema, id:int):
    if request.firstname:
        session.query(StudentsModel)\
            .filter(StudentsModel.id == id)\
            .update(
            {
                StudentsModel.firstname: request.firstname
            }
        )

    if request.lastname:
        session.query(StudentsModel)\
            .filter(StudentsModel.id == id)\
            .update(
            {
                StudentsModel.lastname: request.lastname
            }
        )

    if request.group:
        session.query(StudentsModel)\
            .filter(StudentsModel.id == id)\
            .update(
            {
                StudentsModel.group: request.group
            }
        )
    
    session.commit()
    return


def deleteStudentById(id:int):
    session.query(StudentsModel)\
        .filter(StudentsModel.id == id).first().delete()
    
    session.commit()
    return
