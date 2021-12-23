from fastapi import FastAPI

from .routers.students import students_router
from .routers.groups import groups_router
from .routers.teachers import teachers_router
from .routers.subjects import subjects_router
from .routers.relations import relations_router


app = FastAPI()
app.include_router(students_router, prefix="/api/v1/students")
app.include_router(groups_router, prefix="/api/v1/groups")
app.include_router(teachers_router, prefix="/api/v1/teachers")
app.include_router(subjects_router, prefix="/api/v1/subjects")
app.include_router(relations_router, prefix="/api/v1/relations")