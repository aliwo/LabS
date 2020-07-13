from admin.rest.components.admin_view import AdminView
from api.models.animal import Animal


class AnimalView(AdminView):
    Model = Animal

