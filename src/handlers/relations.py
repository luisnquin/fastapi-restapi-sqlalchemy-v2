from ..db.connection import session
from ..db.models import GroupsModel, StudentsModel, SubjectTeacherGroupModel, SubjectsModel, TeachersModel
from ..schema.schemas import AssociationSchema, AssociationSchemaList, AssociationSchemaOpt


def getStudentsAndGroups():
    table = session.query(StudentsModel.group_id, GroupsModel.name, StudentsModel.firstname, StudentsModel.lastname)\
    .join(GroupsModel, GroupsModel.id == StudentsModel.group_id)\
    .order_by(StudentsModel.group_id)

    return [row for row in table]


def getAllAssociations():
    table = session.query(SubjectsModel.title, TeachersModel.firstname, TeachersModel.lastname, GroupsModel.name)\
    .select_from(SubjectTeacherGroupModel)\
    .join(SubjectsModel, SubjectsModel.id == SubjectTeacherGroupModel.subject_id)\
    .join(TeachersModel, TeachersModel.id == SubjectTeacherGroupModel.teacher_id)\
    .join(GroupsModel, GroupsModel.id == SubjectTeacherGroupModel.group_id)

    return [row for row in table]


def getAssociationById(id:int):
    row = session.query(SubjectsModel.title, TeachersModel.firstname, TeachersModel.lastname, GroupsModel.name)\
    .select_from(SubjectTeacherGroupModel)\
    .join(SubjectsModel, SubjectsModel.id == SubjectTeacherGroupModel.subject_id)\
    .join(TeachersModel, TeachersModel.id == SubjectTeacherGroupModel.teacher_id)\
    .join(GroupsModel, GroupsModel.id == SubjectTeacherGroupModel.group_id)\
    .filter(SubjectTeacherGroupModel.id == id)

    return row


def createNewAssociation(request:AssociationSchema):
    query = SubjectTeacherGroupModel(subject_id= request.subject_id, teacher_id=request.teacher_id, group_id=request.group_id)
    session.add(query)
    session.commit()
    
    return


def createALotOfNewAssociations(request:AssociationSchemaList):
    for association in request.__root__:
        query = SubjectTeacherGroupModel(subject_id=association.subject_id, teacher_id=association.teacher_id, group_id=association.group_id)
        session.add(query)
    
    session.commit()
    return


def modifyAssociationById(request:AssociationSchemaOpt, id:int):
    if request.subject_id:
        session.query(SubjectTeacherGroupModel)\
            .filter(SubjectTeacherGroupModel.id == id)\
            .update(
                {
                    SubjectTeacherGroupModel.subject_id: request.subject_id
                }
            )

        session.commit()
        return

    if request.teacher_id:
        session.query(SubjectTeacherGroupModel)\
            .filter(SubjectTeacherGroupModel.id == id)\
            .update(
                {
                    SubjectTeacherGroupModel.teacher_id: request.teacher_id
                }
            )

        session.commit()
        return

    if request.group_id:
        session.query(SubjectTeacherGroupModel)\
            .filter(SubjectTeacherGroupModel.id == id)\
            .update(
                {
                    SubjectTeacherGroupModel.group_id: request.group_id
                }
            )

        session.commit()
        return

    return True
    

def updateAssociationById(request:AssociationSchema, id:int):
    if request.subject_id:
        session.query(SubjectTeacherGroupModel)\
            .filter(SubjectTeacherGroupModel.id == id)\
            .update(
                {
                    SubjectTeacherGroupModel.subject_id: request.subject_id
                }
            )

    if request.teacher_id:
        session.query(SubjectTeacherGroupModel)\
            .filter(SubjectTeacherGroupModel.id == id)\
            .update(
                {
                    SubjectTeacherGroupModel.teacher_id: request.teacher_id
                }
            )

    if request.group_id:
        session.query(SubjectTeacherGroupModel)\
            .filter(SubjectTeacherGroupModel.id == id)\
            .update(
                {
                    SubjectTeacherGroupModel.group_id: request.group_id
                }
            )


    session.commit()
    return


def deleteAssociationById(id:int):
    session.query(SubjectTeacherGroupModel)\
        .filter(SubjectTeacherGroupModel.id == id)\
        .order_by(SubjectTeacherGroupModel.id)\
        .delete()
    
    session.commit()
    return
    