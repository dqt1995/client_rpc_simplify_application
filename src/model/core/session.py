import weakref
from pathlib import Path
import marshal


_sessions = dict()

class project_session(object):
    cache_default_folder = Path.home().joinpath('.client_rpc_demo/')
    def __init__(self, project_name='default'):
        global _sessions
        self._project_name = project_name
        self._uid = type(self).get_uuid()
        self._models = {}
        self._cache_path = self.cache_default_folder.joinpath(self._uid).with_suffix('.ms')

        _sessions[self._uid] = weakref.ref(self)

    def add_model(self, **kwargs):
        assert any([key not in self._models for key in kwargs]), "Duplicate model registered inside this project {}!".format(self._project_name)
        self._models.update(kwargs)

    def __getitem__(self, model):
        return self._models[model]

    def __delitem__(self, model):
        del self._models[model]
        
    def __del__(self):
        # also del weakref to its
        del _sessions[self._uid]

    def copy(self, project_name=None):
        # make a copy of project by copy it's setting and model
        if project_name is None:
            project_name = self._project_name + '_copy'
        # should copy all of model inside it
        return type(self)(project_name, **self._models)

    def commit_model(self, models=[]):
        # commit models in current session (?) do we really need it?
        # will re evaluate this function and make decision in (no) future
        # in future (maybe no future) when we dump the changing part seperatedly, this will be implemented
        raise NotImplemented

    def commit(self):
        # commit all models in current session
        # for simplify, we commit and load all column, but maybe we should change into store and load changing part by generate bytes from each col
        with open(self._cache_path, 'wb') as cache_file:
            marshal.dump(self._models, cache_file)

    def rollback(self):
        with open(self._cache_path, 'rb') as cache_folder:
            self._models = marshal.load(cache_file)

    def clone(self, project_name=None):
        # make a clone of project by copy it's setting
        if project_name is None:
            project_name = self._project_name + '_clone'
        # should clone all of model inside it
        return type(self)(project_name, **self._models)

    @classmethod
    def get_uuid(cls):
        return str(round(time.time))

def get_default():
    if 'default' not in _sessions:
        return project_session()
    else:
        return _sessions['default']

def get_session(project_name="default"):
    if project_name == "default":
        return get_default()
    return _sessions.get(project_name(), None)

def create_session(project_name="default"):
    pass

def load_project(project_cache):
    pass