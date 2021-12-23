from ..db.connection import session
from ..db.models import GroupsModel, StudentsModel, SubjectTeacherGroupModel, SubjectsModel, TeachersModel
from ..schema.schemas import SubjectTeacherGroupSchema


def getStudentsGroups():
    table = session.query(StudentsModel.group_id, GroupsModel.name, StudentsModel.firstname, StudentsModel.lastname)\
    .join(GroupsModel, GroupsModel.id == StudentsModel.group_id)\
    .order_by(StudentsModel.group_id)

    return [row for row in table]


def getSubjectTeachersGroups():
    table = session.query(SubjectsModel.title, TeachersModel.firstname, TeachersModel.lastname, GroupsModel.name)\
    .select_from(SubjectTeacherGroupModel)\
    .join(SubjectsModel, SubjectsModel.id == SubjectTeacherGroupModel.subject_id)\
    .join(TeachersModel, TeachersModel.id == SubjectTeacherGroupModel.teacher_id)\
    .join(GroupsModel, GroupsModel.id == SubjectTeacherGroupModel.group_id)

    return [row for row in table]


def createUnionBetweenSubjectTeachersGroups(request:SubjectTeacherGroupSchema):
    query = SubjectTeacherGroupModel(subject_id= request.subject_id, teacher_id=request.teacher_id, group_id=request.group_id)
    session.add(query)
    session.commit()
    
    return