from ..db.connection import session
from ..schema.schemas import GroupSchema, GroupSchemaOpt, GroupSchemaArray
from ..db.models import GroupsModel


def getAllGroups():
    groups = session.query(GroupsModel.id, GroupsModel.name).order_by(GroupsModel.id)
    
    return [group for group in groups]


def getGroupById(id):
    group = session.query(GroupsModel.id, GroupsModel.name)\
    .filter(GroupsModel.id == id).first()

    return group


def createNewGroup(request:GroupSchema):
    group = GroupsModel(name=request.name)
    session.add(group)

    session.commit()
    return


def createALotOfGroups(request:GroupSchemaArray):
    for group in request.__root__:
        new_group = GroupsModel(name=group.name)
        session.add(new_group)

    session.commit()
    return


def modifyGroupById(request:GroupSchemaOpt, id:int):
    if request.name:
        session.query(GroupsModel).filter(GroupsModel.id == id)\
        .update(
            {
                GroupsModel.name: request.name
            }
        )

        session.commit()        
        return

    if request.id:
        session.query(GroupsModel).filter(GroupsModel.id == id)\
        .update(
            {
                GroupsModel.id: request.id
            }
        )

        session.commit()
        return

    return True


def updateGroupById(request:GroupSchema, id:int):
    session.query(GroupsModel).filter(GroupsModel.id == id)\
    .update(
        {
            GroupsModel.name: request.name
        }
    )

    session.commit()
    return


def deleteGroupById(id:int):
    session.query(GroupsModel).filter(GroupsModel.id == id).first().delete()
    
    session.commit()
    return