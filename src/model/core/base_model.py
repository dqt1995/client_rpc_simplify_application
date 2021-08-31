import grpc
import time
from collections import OrderedDict
from .session import project_session


class ModelType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print (args)
        print(kwargs)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]



class BaseModel(metaclass=ModelType):
    def __init__(self, project_name='default'):
        self.__dict__['project_name'] = project_name
        self._row = OrderedDict()

    def __getitem__(self, rid):
        # we not sure the way to interact with row
        raise NotImplemented

    def get(self, rid):
        return self._row[rid]

    def insert(self, datas):

        pass

    def create(self):
        pass

    def delete(self):
        pass

    def list(self):
        pass

if __name__ == '__main__':
    a = BaseModel()
    c = BaseModel('a')
    b = BaseModel(project_name='tes')