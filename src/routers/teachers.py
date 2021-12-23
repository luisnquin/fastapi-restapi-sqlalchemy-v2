from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import TeacherSchemaList, TeacherSchemaOpt, TeacherSchema
from ..handlers.teachers import getAllTeachers, getTeacherById, createNewTeacher
from ..handlers.teachers import createALotOfTeachers, modifyTeacherById
from ..handlers.teachers import updateTeacherById, deleteTeacherById


teachers_router = APIRouter()

@teachers_router.get("", tags=["Teachers"])
async def get_teachers():
    teachers = getAllTeachers()

    return teachers


@teachers_router.get("/{id}", tags=["Teachers"])
async def get_one_teacher(id:int):
    teacher = getTeacherById(id)

    if teacher != None:
        return teacher

    return Response(status_code=404)


@teachers_router.post("", tags=["Teachers"])
async def create_teacher(request:TeacherSchema):
    createNewTeacher(request)

    return Response(status_code=201)


@teachers_router.post("/many", tags=["Teachers"])
async def create_a_lot_of_teachers(request:TeacherSchemaList):
    createALotOfTeachers(request)

    return Response(status_code=201)


@teachers_router.patch("/{id}", tags=["Teachers"])
async def modify_teacher(request:TeacherSchemaOpt, id:int):
    err = modifyTeacherById(request, id)

    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@teachers_router.put("/{id}", tags=["Teachers"])
async def update_teacher(request:TeacherSchema, id):
    updateTeacherById(request, id)

    return Response(status_code=202)


@teachers_router.delete("/id", tags=["Teachers"])
async def delete_teacher(id:int):
    deleteTeacherById(id)

    return Response(status_code=202)