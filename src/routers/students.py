from fastapi import Response
from fastapi.routing import APIRouter

from ..schemas import *
from ..handlers.students import *

students_router = APIRouter()


@students_router.get("", tags=["Students"])
async def getStudents():
    students = getAllStudents()
    return [student for student in students]


@students_router.get("/{id}", tags=["Students"])
async def getOneStudent(id:int):
    student = getStudentById(id)
    return student


@students_router.post("", tags=["Students"])
async def newStudent(student:StudentsSchema):
    createNewStudent(student)

    return Response(status_code=201)