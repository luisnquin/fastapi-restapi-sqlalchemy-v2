from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import TeacherSchemaArray, TeacherSchemaOpt, TeacherSchema
from ..handlers.teachers import getAllTeachers, getTeacherById, createNewTeacher
from ..handlers.teachers import createALotOfTeachers, modifyTeacherById
from ..handlers.teachers import updateTeacherById, deleteTeacherById


teachers_router = APIRouter()

@teachers_router.get("", tags=["Teachers"])
def getTeachers():
    teachers = getAllTeachers()

    return teachers


@teachers_router.get("/{id}", tags=["Teachers"])
def getOneTeacher(id:int):
    teacher = getTeacherById(id)

    if teacher != None:
        return teacher

    return Response(status_code=404)


@teachers_router.post("", tags=["Teachers"])
def newTeacher(request:TeacherSchema):
    createNewTeacher(request)

    return Response(status_code=201)


@teachers_router.post("/many", tags=["Teachers"])
def aLotOfNewTeachers(request:TeacherSchemaArray):
    createALotOfTeachers(request)

    return Response(status_code=201)


@teachers_router.patch("/{id}", tags=["Teachers"])
def modifyTeacher(request:TeacherSchemaOpt, id:int):
    err = modifyTeacherById(request, id)

    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@teachers_router.put("/{id}", tags=["Teachers"])
def updateTeacher(request:TeacherSchema, id):
    updateTeacherById(request, id)

    return Response(status_code=202)


@teachers_router.delete("/id", tags=["Teachers"])
def deleteTeacher(id:int):
    deleteTeacherById(id)

    return Response(status_code=202)