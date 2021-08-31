class BaseForm(object):
    def __init__(self, **kwargs):
        self._form_name = type(self).__name__
        self._data = kwargs

    def save(self):
        return self._data

    @staticmethod
    def load():
        return self._data

class FieldForm(object):
    def __init__(self, name, f_type=None):
        super().__init__(name=name, f_type=f_type)

class MessageForm(BaseForm):
    # basic message for sending and receiving
    def __init__(self, message_dict):
        #self.fields = fields
        super().__init__(**message_dict)

    def export_proto(self):
        pass

class ProtoForm(BaseForm):
    def __init__(self, fields):
        super().__init__(**fields)

    def create_message(self, dict):
        pass

class RecorderForm(BaseForm):
    def __init__(self, fields, model=None):
        super().__init__(**fields)
        self._model_call = model

        
    def _create_oid_recorder(self):
        # for default
        return '{}-{}'.format(round(time.time()), id(self))