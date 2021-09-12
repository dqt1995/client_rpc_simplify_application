import grpc
import time
from .session import project_session

class BaseModel(object):
    def __init__(self, project_id):
        self._project_id = project_id
        self._row = dict()

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
    b = BaseModel(project_id='tes')