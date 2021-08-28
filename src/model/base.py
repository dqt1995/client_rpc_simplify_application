import grpc
import time

from . import core

class BaseModel(object):
	def __init__(self, **kwargs):
		self.oid_recorder = str


	def _create_oid_recorder(self):
		# for default
		return '{}-{}'.format(round(time.time()), id(self))

	def record(self, **kwargs):

		pass

	def get(self):
		pass