from flask import request
from libs.route.router import route
from flask.views import MethodView
from libs.database.engine import Session
from libs.status import Status


class AdminView(MethodView):
    decorators = [route]
    Model = None

    @classmethod
    def default_json_option(self):
        return {}

    @classmethod
    def get(cls, id_, json_option=None):
        if id_ is None:
            return cls.list()
        return Session().query(cls.Model).filter(cls.Model.id == id_).one()\
            .json(**(json_option if json_option else cls.default_json_option())), Status.HTTP_200_OK

    @classmethod
    def list(cls, json_option=None):
        return [x.json(**(json_option if json_option else cls.default_json_option())) for x in Session().query(cls.Model).all()] \
            , Status.HTTP_200_OK \
            , {'X-Total-Count': Session().query(cls.Model).count(), 'access-control-expose-headers': 'X-Total-Count'}

    def post(self):
        model = self.Model(**request.json)
        Session().add(model)
        Session().flush()
        return model

    def put(self, id_):
        model = Session().query(self.Model).filter(self.Model.id == id_).one()
        for key, value in request.json.items():
            if hasattr(model, key):
                setattr(model, key, value)

        Session().flush()
        return model

    def delete(self, id_):
        model = Session().query(self.Model).filter(self.Model.id == id_).one()
        Session(changed=True).delete(model)

    def total(self):
        return Session().query(self.Model).count()
