from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import GroupSchema, GroupSchemaOpt, GroupSchemaList
from ..handlers.groups import getAllGroups, getGroupById, createNewGroup
from ..handlers.groups import createALotOfNewGroups, modifyGroupById
from ..handlers.groups import updateGroupById, deleteGroupById

groups_router = APIRouter()


@groups_router.get("", tags=["Group of students"])
async def get_groups():
    groups = getAllGroups()

    return groups


@groups_router.get("/{id}", tags=["Group of students"])
async def get_one_group(id):
    group = getGroupById(id)

    if group != None:
        return group

    return Response(status_code=404)


@groups_router.post("", tags=["Group of students"])
async def create_group(group:GroupSchema):
    createNewGroup(group)

    return Response(status_code=201)


@groups_router.post("/many", tags=["Group of students"])
async def create_a_lot_of_groups(groups:GroupSchemaList):
    createALotOfNewGroups(groups)

    return Response(status_code=201)


@groups_router.patch("/{id}", tags=["Group of students"])
async def modify_group(group:GroupSchemaOpt, id:int):
    err = modifyGroupById(group, id)
    
    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@groups_router.put("/{id}", tags=["Group of students"])
async def update_group(group:GroupSchema, id:int):
    updateGroupById(group, id)

    return Response(status_code=202)


@groups_router.delete("/{id}", tags=["Group of students"])
async def delete_group(id:int):
    deleteGroupById(id)

    return Response(status_code=202)