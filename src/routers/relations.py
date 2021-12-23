from fastapi import Response
from fastapi.routing import APIRouter

from ..schema.schemas import AssociationSchema, AssociationSchemaList, AssociationSchemaOpt
from ..handlers.relations import getAssociationById, getStudentsAndGroups
from ..handlers.relations import modifyAssociationById, createALotOfNewAssociations
from ..handlers.relations import updateAssociationById, getAllAssociations
from ..handlers.relations import deleteAssociationById, createNewAssociation

relations_router = APIRouter()

@relations_router.get("/groups-students", tags=["Relations", "Groups and students"])
async def get_group_and_students():
    data = getStudentsAndGroups()

    return data


@relations_router.get("/associate", tags=["Relations", "Groups, Subjects and teachers"])
async def get_associations():
    associations = getAllAssociations()
    
    return associations


@relations_router.get("/associate/{id}", tags=["Relations", "Groups, Subjects and teachers"])
async def get_one_association(id:int):
    association = getAssociationById(id)
    
    return association


@relations_router.post("/associate", tags=["Relations", "Groups, Subjects and teachers"])
async def create_associations(request:AssociationSchema):
    createNewAssociation(request)

    return Response(status_code=202)


@relations_router.post("/associate/many", tags=["Relations", "Groups, Subjects and teachers"])
async def create_a_lot_of_associations(request:AssociationSchemaList):
    createALotOfNewAssociations(request)

    return Response(status_code=202)


@relations_router.patch("/associate/{id}", tags=["Relations", "Groups, Subjects and teachers"])
async def modify_associations(request:AssociationSchemaOpt, id:int):
    err = modifyAssociationById(request, id)

    if err:
        return Response(status_code=304)

    return Response(status_code=202)


@relations_router.put("/associate/{id}", tags=["Relations", "Groups, Subjects and teachers"])
async def update_associations(request:AssociationSchema, id:int):
    updateAssociationById(request, id)

    return Response(status_code=202)


@relations_router.delete("/associate/{id}", tags=["Relations", "Groups, Subjects and teachers"])
async def delete_associations(id:int):
    deleteAssociationById(id)

    return Response(status_code=202)