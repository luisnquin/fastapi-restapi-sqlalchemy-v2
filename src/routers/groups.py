from fastapi import Response
from fastapi.routing import APIRouter
from starlette.responses import HTMLResponse

from ..schemas import *
from ..handlers.students import *
from ..handlers.groups import *


group_router = APIRouter()


@group_router.get("", tags=["Group of students"])
async def getGroups():
    groups = getAllGroups()

    return groups


@group_router.get("/{id}", tags=["Group of students"])
async def getOneGroup(id):
    group = getGroupById(id)

    if group != None:
        return group

    return HTMLResponse(status_code=404)


@group_router.post("", tags=["Group of students"])
async def newGroup(group:GroupSchema):
    createNewGroup(group)

    return Response(status_code=201)


@group_router.post("/many", tags=["Group of students"])
async def aLotOfNewGroups(groups:ListGroupSchema):
    createALotOfGroups(groups)

    return Response(status_code=201)


@group_router.put("/{id}", tags=["Group of students"])
async def updateGroup(group:GroupSchema, id:int):
    updateGroupById(group, id)

    return Response(status_code=202)


@group_router.delete("/{id}", tags=["Group of students"])
async def deleteGroup(id:int):
    deleteGroupById(id)

    return Response(status_code=202)