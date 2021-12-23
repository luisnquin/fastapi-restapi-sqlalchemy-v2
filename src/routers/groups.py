from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import GroupSchema, GroupSchemaOpt, GroupSchemaArray
from ..handlers.groups import getAllGroups, getGroupById, createNewGroup
from ..handlers.groups import createALotOfGroups, modifyGroupById
from ..handlers.groups import updateGroupById, deleteGroupById

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

    return Response(status_code=404)


@group_router.post("", tags=["Group of students"])
async def newGroup(group:GroupSchema):
    createNewGroup(group)

    return Response(status_code=201)


@group_router.post("/many", tags=["Group of students"])
async def aLotOfNewGroups(groups:GroupSchemaArray):
    createALotOfGroups(groups)

    return Response(status_code=201)


@group_router.patch("/{id}", tags=["Group of students"])
async def modifyGroup(group:GroupSchemaOpt, id:int):
    err = modifyGroupById(group, id)
    
    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@group_router.put("/{id}", tags=["Group of students"])
async def updateGroup(group:GroupSchema, id:int):
    updateGroupById(group, id)

    return Response(status_code=202)


@group_router.delete("/{id}", tags=["Group of students"])
async def deleteGroup(id:int):
    deleteGroupById(id)

    return Response(status_code=202)