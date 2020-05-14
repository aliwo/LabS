from api.models.user import User
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
terms_agreement = convert(TermsAgreement, 'terms_agreement.yaml')

