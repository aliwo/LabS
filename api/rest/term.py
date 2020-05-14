from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from libs.database.engine import Session
from libs.route.login_required import login_required
from libs.route.router import route
from libs.status import Status
from api.models.terms import Term
from api.models.terms_agreement import TermsAgreement

@route
def show_terms():
    return {'term': [x.json() for x in Session().query(Term).all()]}, Status.HTTP_200_OK

@route
@login_required
def settle_contract(term_ids):
    '''
    약관'들'에 동의합니다.
    '''
    try:
        term = Session().query(Term).filter((Term.id.in_(term_ids))).all()
    except NoResultFound as e:
        return {'msg': f'No Term found #: {term_ids}'}, Status.HTTP_404_NOT_FOUND

    Session(changed=True).add(TermsAgreement(term_id=term.id, user_id=g.user_session.user.id))
    Session().commit()
    return {}, Status.HTTP_200_OK
