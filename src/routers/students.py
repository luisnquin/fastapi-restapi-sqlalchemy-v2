from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import StudentSchema, StudentSchemaOpt, StudentSchemaList
from ..handlers.students import getAllStudents, getStudentById, createNewStudent
from ..handlers.students import createALotOfNewStudents, modifyStudentById
from ..handlers.students import updateStudentById, deleteStudentById

students_router = APIRouter()


@students_router.get("", tags=["Students"])
async def get_students():
    students = getAllStudents()
    return students


@students_router.get("/{id}", tags=["Students"])
async def get_one_student(id:int):
    student = getStudentById(id)

    if student != None:
        return student
    
    return Response(status_code=404)


@students_router.post("", tags=["Students"])
async def create_student(student:StudentSchema):
    createNewStudent(student)

    return Response(status_code=201)


@students_router.post("/many", tags=["Students"])
async def create_a_lot_of_students(students:StudentSchemaList):
    createALotOfNewStudents(students)

    return Response(status_code=201)


@students_router.patch("/{id}", tags=["Students"])
async def modify_student(student:StudentSchemaOpt, id:int):
    err = modifyStudentById(student, id)

    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@students_router.put("/{id}", tags=["Students"])
async def update_student(id:int, student:StudentSchema):
    updateStudentById(id, student)

    return Response(status_code=202)


@students_router.delete("/{id}", tags=["Students"])
async def delete_student(id:int):
    deleteStudentById(id)

    return Response(status_code=202)