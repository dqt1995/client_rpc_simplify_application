import json
from .base import BaseForm

class MessageForm(BaseForm):
    # basic message for sending and receiving
    def __init__(self, message_dict):
        #self.fields = fields
        self.__dict__.update(message_dict)

    def export_proto(self):
        pass