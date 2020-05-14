from api.models.user import User
from api.models.user_point import UserPoint
from api.models.sms_auth import SmsAuth
from api.models.terms import Term
from api.models.terms_agreement import TermsAgreement
from api.models.type_group import TypeGroup
from libs.sa2swagger.convert import convert

user = convert(User, 'user.yaml', {'user':{
        'description': 'end users',
        'properties': {
        }
    }
})
user_point = convert(UserPoint, 'user_point.yaml')
term = convert(Term, 'term.yaml')
type_group = convert(TypeGroup, 'type_group.yaml')
sms_auth = convert(SmsAuth, 'sms_auth.yaml')
terms_agreement = convert(TermsAgreement, 'terms_agreement.yaml')

