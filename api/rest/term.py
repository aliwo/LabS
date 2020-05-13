from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from libs.database.engine import Session
from libs.route.login_required import login_required
from libs.status import Status
from api.models.terms import Terms
from api.models.terms_agreement import TermsAgreement


def show_terms():
    return {'okay': True, 'term': [x.json() for x in Session().query(Terms).all()]}, Status.HTTP_200_OK


@login_required
def settle_contract(id_):
    '''
    약관에 동의합니다.
    '''
    try:
        term = Session().query(Terms).filter((Terms.id == id_)).one()
    except NoResultFound as e:
        return {'okay': False, 'msg': f'No Term found #: {id_}'}, Status.HTTP_404_NOT_FOUND

    Session(changed=True).add(TermsAgreement(term_id=term.id, user_id=g.user_session.user.id))
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK
