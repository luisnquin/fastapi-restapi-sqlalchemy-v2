from fastapi.routing import APIRouter

from schemas import *
from handlers.students import *

router = APIRouter()

@router.get("", tags=["GET"])
async def getNothing():
    return


@router.post("/group", tags=["POST"])
async def newGroup(group:Groups):
    createNewGroup(group)

    return Response(status_code=201)