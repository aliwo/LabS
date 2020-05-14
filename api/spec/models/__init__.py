from api.models.user import User
from api.models.sms_auth import SmsAuth
from api.models.terms import Term
from api.models.terms_agreement import TermsAgreement
from libs.sa2swagger.convert import convert

user = convert(User, 'user.yaml', {'user':{
        'description': 'end users',
        'properties': {
        }
    }
})
term = convert(Term, 'term.yaml')
sms_auth = convert(SmsAuth, 'sms_auth.yaml')
terms_agreement = convert(TermsAgreement, 'terms_agreement.yaml')

