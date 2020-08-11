from flask import g
from sqlalchemy.orm.exc import NoResultFound

from api.models.coupon import Coupon
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def redeem(code):
    try:
        coupon = Session().query(Coupon).filter((Coupon.code == code)).one()
    except NoResultFound:
        raise ClientError('not found', Status.HTTP_404_NOT_FOUND)
    if coupon.user_id is not None:
        if coupon.user_id != g.user_session.user.id:
            raise ClientError('not yours', Status.HTTP_470_NOT_YOURS)
    coupon.redeem(g.user_session.user.id)
    Session().commit()
    return {'okay': True, 'hp': coupon.hp, 'mp': coupon.mp}, Status.HTTP_200_OK


