from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from libs.database.engine import Session
from libs.route.login_required import login_required
from libs.status import Status
from api.models.terms import Term
from api.models.terms_agreement import TermsAgreement


def show_terms():
    return {'term': [x.json() for x in Session().query(Term).all()]}, Status.HTTP_200_OK


@login_required
def settle_contract(id_):
    '''
    약관에 동의합니다.
    '''
    try:
        term = Session().query(Term).filter((Term.id == id_)).one()
    except NoResultFound as e:
        return {'msg': f'No Term found #: {id_}'}, Status.HTTP_404_NOT_FOUND

    Session(changed=True).add(TermsAgreement(term_id=term.id, user_id=g.user_session.user.id))
    Session().commit()
    return {}, Status.HTTP_200_OK
