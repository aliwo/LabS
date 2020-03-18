from api.models.user import User
from libs.sa2swagger.convert import convert

user = convert(User, 'user.yaml',{
    'description': 'end users',
    'properties': {
        
    }
})

