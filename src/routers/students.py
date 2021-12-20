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

    if student != None:
        return student
    
    return Response(status_code=404)


@students_router.post("", tags=["Students"])
async def newStudent(student:StudentSchema):
    createNewStudent(student)

    return Response(status_code=201)


@students_router.post("/many", tags=["Students"])
async def aLotOfNewStudents(students:ListStudentSchema):
    createALotOfStudents(students)

    return Response(status_code=201)


@students_router.put("/{id}", tags=["Students"])
async def updateStudent(id:int, student:StudentSchema):
    updateStudentById(id, student)

    return Response(status_code=202)


@students_router.delete("/{id}", tags=["Students"])
async def deleteStudent(id:int):
    deleteStudentById(id)

    return Response(status_code=202)