from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from api.models.animal import Animal
from api.models.animal_correlation import AnimalCorrelation
from api.models.user import User
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def get_animal():
    if not request.args.getlist('id'):
        animals = Session().query(Animal).all()
    else:
        animals = Session().query(Animal).filter((Animal.id.in_(request.args.getlist('id')))).all()
    return [x.json() for x in animals], Status.HTTP_200_OK, \
           {'X-Total-Count': Session().query(Animal).count(), 'access-control-expose-headers': 'X-Total-Count'}

