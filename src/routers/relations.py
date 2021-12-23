from fastapi import Response
from fastapi.routing import APIRouter

from ..handlers.relations import getStudentsGroups, getSubjectTeachersGroups, createUnionBetweenSubjectTeachersGroups
from ..schema.schemas import SubjectTeacherGroupSchema


relations_router = APIRouter()

@relations_router.get("/groups&students", tags=["Relations"])
def getGroupAndStudents():
    data = getStudentsGroups()

    return data


@relations_router.get("/subject-teacher-groups", tags=["Relations"])
def getAssociations():
    data = getSubjectTeachersGroups()
    
    return data


@relations_router.post("/asociate", tags=["Relations"])
def associateSubjectTeachersGroups(request:SubjectTeacherGroupSchema):
    createUnionBetweenSubjectTeachersGroups(request)

    return Response(status_code=202)