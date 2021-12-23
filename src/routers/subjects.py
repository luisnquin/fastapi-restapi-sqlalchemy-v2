from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import SubjectSchema, SubjectSchemaArray
from ..handlers.subjects import getAllSubjects, getSubjectById, createNewSubject
from ..handlers.subjects import createALotOfSubjects, modifySubjectById
from ..handlers.subjects import updateSubjectById, deleteSubjectById


subjects_router = APIRouter()


@subjects_router.get("", tags=["Subjects"])
def getSubjects():
    subjects = getAllSubjects()

    return subjects


@subjects_router.get("/{id", tags=["Subjects"])
def getOneSubject(id:int):
    subject = getSubjectById(id)
    if subject != None:
        return subject

    return Response(status_code=404)


@subjects_router.post("", tags=["Subjects"])
def newSubject(request:SubjectSchema):
    createNewSubject(request)

    return Response(status_code=202)


@subjects_router.post("/many", tags=["Subjects"])
def aLotOfNewSubjects(request:SubjectSchemaArray):
    createALotOfSubjects(request)

    return Response(status_code=202)


@subjects_router.patch("/{id}", tags=["Subjects"])
def modifySubject(request:SubjectSchema, id:int):
    err = modifySubjectById(request, id)
    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@subjects_router.put("/{id}", tags=["Subjects"])
def updateSubject(request:SubjectSchema, id:int):
    updateSubjectById(request, id)

    return Response(status_code=202)


@subjects_router.delete("/{id}", tags=["Subjects"])
def deleteSubject(id:int):
    deleteSubjectById(id)

    return Response(status_code=202)