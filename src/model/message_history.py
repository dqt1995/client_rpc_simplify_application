import grpc
import datetime

from . import base
from . import core

class Histories(Base):
	req_mess = core.MessageForm
	req_time = datetime.datetime
	res_mess = core.MessageForm
	res_time = datetime.datetime
	from_protos = core.ProtoForm


	def __init__(self, fields):
		self.request_message = RequestMessage(fields)
		# get response and store it

	def record_history(self, message):
		pass

	def get_history(self, id):
		pass