

class BaseRPC(object):
	def __init__(self, rpc_setting):
		self.rpc_setting = rpc_setting
		self.history = {}

	def 