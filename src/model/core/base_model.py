import grpc
import time
from .session import project_session

class Column(object):
    # def __init__(self, col_type, **kwargs): #, primary_key=False, default='none_set', unique=False, nullable=True, onupdate=None):

    #     pass
    def __init__(self, col_type):
        self._col_type = col_type

class relationship(object):
    
    def __init__(self, col_type):
        self._col_type = col_type

class Model(object):
    def __init__(self, project_id, keep_current_keys=False, auto_add=False):
        self._project_id = project_id
        self.setting = {
            'auto_add': auto_add,
            'keep_current_keys': keep_current_keys,
            'current_keys': set(),
            'all_keys': set()
        }
        self._rows = dict()
        self._n_datas = len(self._rows)
        self.loader = {
            'auto_add': auto_add,
            'keep_current_keys': keep_current_keys
        }

    ###########################################################################################
    # setting property
    ###########################################################################################
    def _load_setting(self, loader_setting):
        if _setting in self.__dict__:
            # setting cannot be changed
            raise AttributeError
        self._setting = {
                            'keep_current_keys': loader_setting.get('keep_current_keys', False),
                            'auto_add': loader_setting.get('auto_add', False),
                            'current_keys': loader_setting.get('current_keys', set()),
                            'all_keys': loader_setting.get('all_keys', set())
                        }
        if not self._setting['keep_current_keys'] and not self._setting['auto_add']:
            self._loader = self._default_loader
        elif self._setting['keep_current_keys'] and not self._setting['auto_add']:
            self._loader = self._load_keep_current_key
        elif not self._setting['keep_current_keys'] and self._setting['auto_add']:
            self._loader = self._load_auto_add
        else:
            self._loader = self._load_keep_current_key_and_auto_add
            
        #return self._setting

    def _get_setting(self):
        return self._setting

    setting = property(_loader_setting, _get_setting)

    ###########################################################################################
    

    def __setitem__(self, row_name, row_attr):
        # we not sure the way to interact with row
        raise NotImplemented

    def get(self, rid):
        return self._row[rid]

    def insert(self, data, keep_current_keys=False, auto_add=False):
        self._row[rid]
        if keep_current_keys:
            data = {key:None for key in self._current_keys if self._current_keys}
            self._current_keys
        self._current_keys = set(data.keys())
        self._keys.update(self._current_keys)
        self._n_datas += 1
        pass

    def delete(self, rid):
        del self._row[rid]

    def list(self):
        return self._row
        pass

    def join(self):
        pass

    def where(self, **kwargs):
        pass

    def _default_loader(self, data):
        self._current_keys = set(data.keys())
        self._n_datas += 1
        self._row[self._n_datas] = data

    def _load_keep_current_key(self, data):
        raise NotImplemented

    def _load_auto_add(self, data):
        raise NotImplemented

    def _load_keep_current_key_and_auto_add(self, data):
        raise NotImplemented

if __name__ == '__main__':
    a = BaseModel()
    c = BaseModel('a')
    b = BaseModel(project_id='tes')