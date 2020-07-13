from admin.rest.components.admin_view import AdminView
from api.models.user import User


class UserView(AdminView):
    Model = User

