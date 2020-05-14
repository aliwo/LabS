from flask import request, g
from sqlalchemy.orm.exc import NoResultFound

from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status
from api.models.terms import Term
from api.models.terms_agreement import TermsAgreement

@route
def show_terms():
    return {'term': [x.json() for x in Session().query(Term).all()]}, Status.HTTP_200_OK

@route
def settle_contract():
    '''
    약관'들'에 동의합니다.
    '''
    term_ids = request.json.get('term_ids')
    terms = Session().query(Term).filter((Term.id.in_(term_ids))).all()
    if len(terms) == 0:
        raise ClientError(f'No Term found #: {term_ids}', Status.HTTP_404_NOT_FOUND)

    for term in terms:
        Session(changed=True).add(TermsAgreement(term_id=term.id, user_id=g.user_session.user.id))
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK
