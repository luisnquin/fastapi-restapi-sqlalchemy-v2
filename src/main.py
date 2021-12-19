from fastapi import FastAPI

from .routers.students import students_router
from .routers.groups import group_router


app = FastAPI()
app.include_router(students_router, prefix="/api/v1/students")
app.include_router(group_router, prefix="/api/v1/group")