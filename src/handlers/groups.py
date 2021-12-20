from ..db.connection import session
from ..schemas import *
from ..db.models import *


def getAllGroups():
    groups = session.query(GroupsModel.id, GroupsModel.name).order_by(GroupsModel.id)
    return [group for group in groups]


def getGroupById(id):
    group = session.query(GroupsModel.id, GroupsModel.name).filter(
        GroupsModel.id == id
    ).first()

    return group


def createNewGroup(group:GroupSchema):
    group_query = GroupsModel(name=group.name)
    session.add(group_query)
    session.commit()
    return


def createALotOfGroups(groups:ListGroupSchema):
    for group in groups.__root__:
        group_query = GroupsModel(name=group.name)
        session.add(group_query)

    session.commit()
    return


def updateGroupById(group:GroupSchema, id:int):
    session.query(GroupsModel).filter(
        GroupsModel.id == id
        ).update(
        {
            GroupsModel.name: group.name
        }
    )
    session.commit()
    return


def deleteGroupById(id:int):
    session.query(GroupsModel).filter(
        GroupsModel.id == id
        ).first().delete()
    session.commit()
    return