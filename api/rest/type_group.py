from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from api.models.type_group import TypeGroup
from api.models.user import User
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def get_type_group(type_group_id):
    '''
    TODO: 테스트 필요
    '''
    try:
        type_group = Session().query(TypeGroup).filter((TypeGroup.id == type_group_id)).one()
    except NoResultFound:
        raise ClientError(f'No Type group Found id #{type_group_id}', status_code=Status.HTTP_404_NOT_FOUND)

    return {'type_group': type_group.json()}, Status.HTTP_200_OK


@route
def get_all_type_groups():
    return {'type_groups': [x.json() for x in Session().query(TypeGroup).all()]}, Status.HTTP_200_OK
