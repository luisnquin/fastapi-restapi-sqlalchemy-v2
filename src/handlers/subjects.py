from ..db.connection import session
from ..schema.schemas import SubjectSchema, SubjectSchemaArray
from ..db.models import SubjectsModel


def getAllSubjects():
    subjects = session.query(SubjectsModel).order_by(SubjectsModel.id)

    return [subject for subject in subjects]


def getSubjectById(id:int):
    subject = session.query(SubjectsModel)\
        .filter(SubjectsModel.id == id).first()
    
    return subject


def createNewSubject(request:SubjectSchema):
    subject = SubjectsModel(title=request.title)
    session.add(subject)
    session.commit()

    return


def createALotOfSubjects(request:SubjectSchemaArray):
    for subject in request.__root__:
        new_subject = SubjectsModel(title=subject.title)
        session.add(new_subject)

    session.commit()
    return

def modifySubjectById(request:SubjectSchema, id:int):
    if request.title:
        session.query(SubjectsModel)\
            .filter(SubjectsModel.id == id)\
            .update(
            {
                SubjectsModel.title: request.title
            }
        )
        session.commit()
        return

    if request.id:
        session.query(SubjectsModel)\
            .filter(SubjectsModel.id == id)\
            .update(
            {
                SubjectsModel.id: request.id
            }
        )
        session.commit()
        return

    return True


def updateSubjectById(request:SubjectSchema, id:int):
    if request.title:
        session.query(SubjectsModel)\
            .filter(SubjectsModel.id == id)\
            .update(
            {
                SubjectsModel.title: request.title
            }
        )

    if request.id:
        session.query(SubjectsModel)\
            .filter(SubjectsModel.id == id)\
            .update(
            {
                SubjectsModel.id: request.id
            }
        )

    session.commit()
    return 


def deleteSubjectById(id:int):
    session.query(SubjectsModel)\
        .filter(SubjectsModel.id == id).first().delete()

    session.commit()
    return