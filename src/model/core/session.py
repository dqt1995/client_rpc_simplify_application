import weakref
from collections import OrderedDict

_sessions = OrderedDict()

class project_session(object):
    def __init__(self, project_name='default', **kwargs):
        global _sessions
        assert project_name not in _sessions, "Duplicate project_name registered!" + \
                " Try with other name, or use existing session if you really want to access {}".format(project_name)
        self._project_name = project_name
        self.__dict__.update(kwargs)
        _sessions[self._project_name] = weakref.ref(self)

    def add_model(self, **kwargs):
        assert any([key not in self.__dict__ for key in kwargs]), "Duplicate model registered inside this project {}!".format(self._project_name)
        self.__dict__.update(kwargs)
        
    def __del__(self):
        del _sessions[self._project_name]

def get_default():
    if 'default' not in _sessions:
        return project_session()
    else:
        return _sessions['default']

def get_session(project_name=None):
    if project_name is not None:
        return _sessions.get(project_name(), None)
    elif len(_sessions) > 0:
        session = next(reversed(_sessions))
        return next(reversed(_sessions))()
    else:
        return None