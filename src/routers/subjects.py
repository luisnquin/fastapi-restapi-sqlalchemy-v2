from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import SubjectSchema, SubjectSchemaList
from ..handlers.subjects import getAllSubjects, getSubjectById, createNewSubject
from ..handlers.subjects import createALotOfSubjects, modifySubjectById
from ..handlers.subjects import updateSubjectById, deleteSubjectById


subjects_router = APIRouter()


@subjects_router.get("", tags=["Subjects"])
async def get_subjects():
    subjects = getAllSubjects()

    return subjects


@subjects_router.get("/{id", tags=["Subjects"])
async def get_one_subject(id:int):
    subject = getSubjectById(id)
    if subject != None:
        return subject

    return Response(status_code=404)


@subjects_router.post("", tags=["Subjects"])
async def create_subject(request:SubjectSchema):
    createNewSubject(request)

    return Response(status_code=202)


@subjects_router.post("/many", tags=["Subjects"])
async def create_a_lot_of_subjects(request:SubjectSchemaList):
    createALotOfSubjects(request)

    return Response(status_code=201)


@subjects_router.patch("/{id}", tags=["Subjects"])
async def modify_subject(request:SubjectSchema, id:int):
    err = modifySubjectById(request, id)
    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@subjects_router.put("/{id}", tags=["Subjects"])
async def update_subject(request:SubjectSchema, id:int):
    updateSubjectById(request, id)

    return Response(status_code=202)


@subjects_router.delete("/{id}", tags=["Subjects"])
async def delete_subject(id:int):
    deleteSubjectById(id)

    return Response(status_code=202)