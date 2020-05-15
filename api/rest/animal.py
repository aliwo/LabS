from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from api.models.animal import Animal
from api.models.user import User
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def get_animal(animal_id):
    try:
        animal = Session().query(Animal).filter((Animal.id == animal_id)).one()
    except NoResultFound:
        raise ClientError(f'No Animal Found id #{animal_id}', status_code=Status.HTTP_404_NOT_FOUND)

    return {'user': animal.json()}, Status.HTTP_200_OK
