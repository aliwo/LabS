from api.models.animal import Animal
from api.models.match import Match
from api.models.user import User
from api.models.heart import Heart
from api.models.user_point import UserPoint
from api.models.sms_auth import SmsAuth
from api.models.terms import Term
from api.models.mbti_questions import MbtiQuestion
from api.models.terms_agreement import TermsAgreement
from api.models.type_group import TypeGroup
from libs.sa2swagger.convert import convert


animal = convert(Animal, 'animal.yaml')
user = convert(User, 'user.yaml', {'user':{
        'description': 'end users',
        'properties': {
            'ideal_type_groups': {
                'type': 'string',
                'description': '(comma separated)list of integers'
            },
            'body_shape': {
                'type': 'string',
                'description': 'slim tan tan :)'
            },
            'animal': {
                'type': 'object'
            }
        },
    }
})
mbti_question = convert(MbtiQuestion, 'mbti_question.yaml')
sms_auth = convert(SmsAuth, 'sms_auth.yaml')
term = convert(Term, 'term.yaml')
heart = convert(Heart, 'heart.yaml', {'heart': {
    'properties': {
        'from_user': {
            'type': 'object',
            'description': '하트 유저'
        },
        'to_user': {
            'type': 'object',
            'description': '하트 유저'
        }
    }
}})
terms_agreement = convert(TermsAgreement, 'terms_agreement.yaml')
type_group = convert(TypeGroup, 'type_group.yaml')
user_point = convert(UserPoint, 'user_point.yaml')
match = convert(Match, 'match.yaml', {'match': {
    'properties': {
        'man': {
            'type': 'object',
            'description': '매치 유저'
        },
        'woman': {
            'type': 'object',
            'description': '매치 유저'
        }
    }
}})

