class BaseForm(object):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError
        
    def cache(self):
        return json.dumps(self.__dict__)

    @classmethod
    def load_cache(cls, cache_str):
        message_dict = json.loads(cache_str)
        return cls(message_dict)
