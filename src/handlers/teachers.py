from ..db.connection import session
from ..schema.schemas import TeacherSchema, TeacherSchemaOpt, TeacherSchemaList
from ..db.models import TeachersModel


def getAllTeachers():
    teachers = session.query(TeachersModel.id, TeachersModel.firstname, TeachersModel.lastname)\
        .order_by(TeachersModel.id)

    return [teacher for teacher in teachers]


def getTeacherById(id:int):
    teacher = session.query(TeachersModel.id, TeachersModel.firstname, TeachersModel.lastname)\
        .filter(TeachersModel.id == id).first()

    return teacher


def createNewTeacher(request:TeacherSchema):
    teacher = TeachersModel(firstname=request.firstname, lastname=request.lastname)
    session.add(teacher)
    session.commit()
    
    return


def createALotOfTeachers(request:TeacherSchemaList):
    for teacher in request.__root__:
        new_teacher = TeachersModel(firstname=teacher.firstname, lastname=teacher.lastname)
        session.add(new_teacher)

    session.commit()

    return


def modifyTeacherById(request:TeacherSchemaOpt, id:int):
    if request.firstname:
        session.query(TeachersModel)\
            .filter(TeachersModel.id == id)\
            .update(
            {
                TeachersModel.firstname: request.firstname
            }
        )
        
        session.commit()
        return

    if request.lastname:
        session.query(TeachersModel)\
            .filter(TeachersModel.id == id)\
            .update(
            {
                TeachersModel.lastname: request.lastname
            }
        )
        
        session.commit()
        return

    return True


def updateTeacherById(request:TeacherSchema, id:int):
    if request.firstname:
        session.query(TeachersModel)\
            .filter(TeachersModel.id == id)\
            .update(
            {
                TeachersModel.firstname: request.firstname
            }
        )

    if request.lastname:
        session.query(TeachersModel)\
            .filter(TeachersModel.id == id)\
            .update(
            {
                TeachersModel.lastname: request.lastname
            }
        )    

    session.commit()
    return


def deleteTeacherById(id:int):
    session.query(TeachersModel)\
        .filter(TeachersModel.id == id).first().delete()
    
    session.commit()
    return