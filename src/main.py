from fastapi import FastAPI

from .routers.students import students_router
from .routers.groups import group_router
from .routers.teachers import teachers_router
from .routers.subjects import subjects_router
from .routers.relations import relations_router


app = FastAPI()
app.include_router(students_router, prefix="/api/v1/students")
app.include_router(group_router, prefix="/api/v1/group")
app.include_router(teachers_router, prefix="/api/v1/teachers")
app.include_router(subjects_router, prefix="/api/v1/subjects")
app.include_router(relations_router, prefix="/api/v1/relations")