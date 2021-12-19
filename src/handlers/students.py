from fastapi import Response

from db.connection import session
from schemas import *
import db.models as dbmodel


def createNewGroup(group:Groups):
    group_query = dbmodel.Groups(group_name=group.name)
    session.add(group_query)
    session.commit()
    return
