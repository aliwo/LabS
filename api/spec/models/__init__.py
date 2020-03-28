from api.models.user import User
from libs.sa2swagger.convert import convert

user = convert(User, 'user.yaml', {'user':{
        'description': 'end users',
        'properties': {
        }
    }
})

