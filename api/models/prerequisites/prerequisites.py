from abc import ABC, abstractmethod

from flask import g

class Prerequisites(ABC):

    base_model = None

    def __init__(self):
        self.result = {}

    def on_create(self):
        pass

    def on_read(self):
        pass

    def on_update(self):
        pass

    def on_delete(self):
        pass

    def get_result(self):
        return self.result



